import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import networkx as nx
from final.DataStructure import Graph

# Function to preprocess the datasets
def preprocess_data():
    # Read the CSV files into DataFrames
    protected_areas_filepath = "protected_areas.csv"
    population_filepath = "population_and_demography.csv"
    iso_filepath = "iso_codes.csv"
    landdata_filepath = "land.json"
    oceandata_filepath = "ocean.json"

    protected_areas_df = pd.read_csv(protected_areas_filepath, low_memory=False)
    population_df = pd.read_csv(population_filepath)
    iso_df = pd.read_csv(iso_filepath)

    # Convert Year column in population_df to datetime format
    population_df['Year'] = pd.to_datetime(population_df['Year'], format='%Y')

    # Fill missing values
    columns_to_replace = ['GIS_M_AREA', 'GIS_AREA', 'NO_TAKE', 'MANG_PLAN', 'SUB_LOC', 'SUPP_INFO', 'CONS_OBJ']
    protected_areas_df[columns_to_replace] = protected_areas_df[columns_to_replace].fillna(np.nan)

    # Read the JSON files
    with open(landdata_filepath, 'r') as land_file:
        landdata_json = json.load(land_file)

    with open(oceandata_filepath, 'r') as ocean_file:
        oceandata_json = json.load(ocean_file)

    # Convert JSON data to DataFrame
    landdata_df = pd.DataFrame(landdata_json['data'].items(), columns=['Year', 'Land_Anomaly'])
    oceandata_df = pd.DataFrame(oceandata_json['data'].items(), columns=['Year', 'Ocean_Anomaly'])

    # Convert Land_Anomaly and Ocean_Anomaly columns to numerical data types
    landdata_df['Land_Anomaly'] = pd.to_numeric(landdata_df['Land_Anomaly'], errors='coerce')
    oceandata_df['Ocean_Anomaly'] = pd.to_numeric(oceandata_df['Ocean_Anomaly'], errors='coerce')

    # Drop rows with NaN values
    landdata_df.dropna(subset=['Land_Anomaly'], inplace=True)
    oceandata_df.dropna(subset=['Ocean_Anomaly'], inplace=True)

    # Convert Year column in landdata_df and oceandata_df to datetime format
    landdata_df['Year'] = pd.to_datetime(landdata_df['Year'], format='%Y%m')
    oceandata_df['Year'] = pd.to_datetime(oceandata_df['Year'], format='%Y%m')

    # Merge land and ocean anomaly data
    combined_df = pd.merge(landdata_df, oceandata_df, on='Year')

    # Merge Population Demographics and ISO Codes DataFrames
    population_iso_df = pd.merge(population_df, iso_df, left_on='Country name', right_on='English short name lower case', how='left')
    population_iso_df.drop(columns=['Numeric code', 'ISO 3166-2'], inplace=True)
    population_iso_df.rename(columns={'Country name': 'country_name'}, inplace=True)

    # Merge ISO codes with protected areas DataFrame
    protected_areas_df = pd.merge(protected_areas_df, iso_df, left_on='ISO3', right_on='Alpha-3 code', how='left')
    protected_areas_df.drop(columns=['Numeric code', 'ISO 3166-2'], inplace=True)
    protected_areas_df.rename(columns={'English short name lower case': 'country_name'}, inplace=True)

    return protected_areas_df, population_iso_df, combined_df

# Function to interact with the dataset
def interact_with_data(protected_areas_df, population_iso_df, combined_df, graph):
    while True:
        print("\nOptions:")
        print("1. Get population of a country by year (1950-2021)")
        print("2. Get global temperature anomalies by year (1950-2021)")
        print("3. Get global population by year (1950-2021)")
        print("4. Get total protected area of all countries")
        print("5. Get total protected area of a country")
        print("6. Visualize global population vs temperature anomalies")
        print("7. Visualize top countries by total protected area")
        print("8. Visualize population growth vs global protected area")
        print("9. Perform graph operations")
        print("10. Exit")

        choice = input("Enter your choice: ")
        
        # Validate input
        if not choice.isdigit() or int(choice) < 1 or int(choice) > 10:
            print("Invalid choice. Please enter a number between 1 and 10.")
            continue
        
        choice = int(choice)  # Convert choice to integer
        
        if choice == 1:
            get_population_by_year_and_country(protected_areas_df, population_iso_df)
        elif choice == 2:
            get_anomalies_and_population_by_year(combined_df, population_iso_df)
        elif choice == 3:
            get_world_population(combined_df, population_iso_df)
        elif choice == 4:
            get_total_protected_area_of_all_countries(protected_areas_df)
        elif choice == 5:
            get_total_protected_area_of_country(protected_areas_df)
        elif choice == 6:
            visualize_global_population_vs_anomalies(combined_df, population_iso_df)
        elif choice == 7:
            visualize_protected_areas(protected_areas_df)
        elif choice == 8:
            visualize_population_and_protected_area(population_iso_df, protected_areas_df)
        elif choice == 9:
            perform_graph_operations(graph, protected_areas_df)  # Pass protected_areas_df as an argument
        elif choice == 10:
            print("Exiting the program. Goodbye!")
            break


def perform_graph_operations(graph, protected_areas_df):
    # Create an empty graph
    G = nx.Graph()

    while True:
        print("\nAvailable Graph Operations:")
        print("1. Add node representing a country")
        print("2. Add edge representing a connection between countries")
        print("3. Visualize protected areas network")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if not choice.isdigit() or int(choice) < 1 or int(choice) > 4:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        choice = int(choice)

        if choice == 1:
            country_input = input("Enter country name, Alpha-2 code, or Alpha-3 code: ").lower().replace(" ", "")
            country = None
            for _, row in protected_areas_df.iterrows():
                if pd.notnull(row['country_name']) and pd.notnull(row['Alpha-2 code']) and pd.notnull(row['Alpha-3 code']):
                    if country_input in (str(row['country_name']).lower(), str(row['Alpha-2 code']).lower(), str(row['Alpha-3 code']).lower()):
                        country = row['country_name']
                        break
            if country:
                graph.add_node(country)
                G.add_node(country)  # Add node to NetworkX graph
                print(f"Node representing {country.capitalize()} added to the graph.")
            else:
                print("Country not found in the dataset.")
        elif choice == 2:
            country1_input = input("Enter the first country: ").lower().replace(" ", "")
            country2_input = input("Enter the second country: ").lower().replace(" ", "")
            country1, country2 = None, None
            for _, row in protected_areas_df.iterrows():
                if pd.notnull(row['country_name']) and pd.notnull(row['Alpha-2 code']) and pd.notnull(row['Alpha-3 code']):
                    if country1_input in (str(row['country_name']).lower(), str(row['Alpha-2 code']).lower(), str(row['Alpha-3 code']).lower()):
                        country1 = row['country_name']
                    if country2_input in (str(row['country_name']).lower(), str(row['Alpha-2 code']).lower(), str(row['Alpha-3 code']).lower()):
                        country2 = row['country_name']
            if country1 and country2:
                graph.add_edge(country1, country2)
                G.add_edge(country1, country2)  # Add edge to NetworkX graph
                print(f"Edge representing connection between {country1.capitalize()} and {country2.capitalize()} added to the graph.")
            else:
                print("One or both countries not found in the dataset.")
        elif choice == 3:
            # Visualize protected areas network
            plt.figure(figsize=(12, 8))
            pos = nx.spring_layout(G)  # Position nodes using spring layout
            nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=12)
            plt.title("Protected Areas Network Visualization")
            plt.show()
        elif choice == 4:
            print("Exiting graph operations.")
            break


# Helper function to format numeric values with commas
def format_with_commas(value):
    return "{:,}".format(value)


# Helper functions to get data
def get_world_population(combined_df, population_iso_df):
    year_input = input("Enter the year (in YYYY format): ")
    
    try:
        year = int(year_input)
    except ValueError:
        print("Invalid input. Please enter a valid year in YYYY format.")
        return
    
    # Filter population data for the specified year and for the "World" country
    world_population = population_iso_df[(population_iso_df['country_name'] == 'World') & 
                                          (population_iso_df['Year'].dt.year == year)]['Population'].sum()
    
    if not pd.isnull(world_population):
        print(f"World population in {year}: {format_with_commas(int(world_population))}")
    else:
        print(f"No population data available for the World in {year}.")


def get_population_by_year_and_country(protected_areas_df, population_iso_df):
    country_input = input("Enter country name, Alpha-2 code, or Alpha-3 code: ").lower().replace(" ", "")
    year_input = input("Enter the year (in YYYY format): ")
    try:
        year = int(year_input)
    except ValueError:
        print("Invalid input. Please enter a valid year in YYYY format.")
        return
    country = None
    for _, row in protected_areas_df.iterrows():
        if pd.notnull(row['country_name']) and pd.notnull(row['Alpha-2 code']) and pd.notnull(row['Alpha-3 code']):
            if country_input in (str(row['country_name']).lower(), str(row['Alpha-2 code']).lower(), str(row['Alpha-3 code']).lower()):
                country = row['country_name']
                break
    if country:
        population_for_year = population_iso_df[(population_iso_df['country_name'] == country) & (population_iso_df['Year'].dt.year == year)]['Population'].sum()
        if population_for_year:
            print(f"Population of {country.capitalize()} in {year}: {format_with_commas(population_for_year)}")
        else:
            print(f"No population data available for {country.capitalize()} in {year}.")
    else:
        print("Country not found in the dataset.")


def get_total_protected_area_of_country(protected_areas_df):
    country_input = input("Enter country name, Alpha-2 code, or Alpha-3 code: ").lower().replace(" ", "")
    country = None
    for _, row in protected_areas_df.iterrows():
        if country_input in (row['country_name'].lower(), row['Alpha-2 code'].lower(), row['Alpha-3 code'].lower()):
            country = row['country_name']
            break
    if country:
        total_area = protected_areas_df[protected_areas_df['country_name'] == country]['REP_AREA'].sum()
        print(f"Total protected area of {country.capitalize()}: {format_with_commas(total_area)} sq km")
    else:
        print("Country not found in the dataset.")


def get_total_protected_area_of_all_countries(protected_areas_df):
    total_area = protected_areas_df['REP_AREA'].sum()
    print(f"Total protected area of all countries: {format_with_commas(total_area)} sq km")


def get_anomalies_and_population_by_year(combined_df, population_iso_df):
    year_input = input("Enter the year (in YYYY format): ")

    try:
        year = int(year_input)
    except ValueError:
        print("Invalid input. Please enter a valid year in YYYY format.")
        return

    anomalies_for_year = combined_df[combined_df['Year'].dt.year == year]

    # Convert anomaly data to numeric values using .loc
    anomalies_for_year.loc[:, 'Land_Anomaly'] = anomalies_for_year['Land_Anomaly'].apply(lambda x: pd.to_numeric(x.split()))
    anomalies_for_year.loc[:, 'Ocean_Anomaly'] = anomalies_for_year['Ocean_Anomaly'].apply(lambda x: pd.to_numeric(x.split()))

    # Calculate average anomalies
    average_land_anomaly = anomalies_for_year['Land_Anomaly'].mean().item()
    average_ocean_anomaly = anomalies_for_year['Ocean_Anomaly'].mean().item()

    print(f"Temperature anomalies for the year {year}:")
    print(f"Average Land Anomaly: {round(float(average_land_anomaly), 2)}")
    print(f"Average Ocean Anomaly: {round(float(average_ocean_anomaly), 2)}")


# Visualization function
def visualize_global_population_vs_anomalies(combined_df, population_iso_df):
    # Get interpolated global population data
    global_population = population_iso_df[population_iso_df['country_name'] == 'World'].set_index('Year')['Population'].interpolate()

    # Filter combined_df to include only years present in the global population data
    combined_df_filtered = combined_df[combined_df['Year'].dt.year >= min(global_population.index.year)]

    # Create a graph object
    graph = Graph()

    # Add nodes and edges to the graph based on the filtered data
    for index, row in combined_df_filtered.iterrows():
        graph.add_edge(row['Land_Anomaly'], row['Ocean_Anomaly'])  # Adding edges between land anomaly and ocean anomaly

    # Plotting temperature anomalies
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Year')
    ax1.set_ylabel('Temperature Anomalies (°C)', color='tab:red')
    ax1.plot(combined_df_filtered['Year'], combined_df_filtered['Land_Anomaly'], color='tab:red', label='Land Anomaly')
    ax1.plot(combined_df_filtered['Year'], combined_df_filtered['Ocean_Anomaly'], color='tab:blue', label='Ocean Anomaly')
    ax1.tick_params(axis='y', labelcolor='tab:red')

    # Creating a second y-axis for global population
    ax2 = ax1.twinx()
    ax2.set_ylabel('Global Population (Billions)', color='tab:green')  # Adjusted title
    ax2.plot(global_population.index, global_population.values, color='tab:green', label='Global Population')  # Adjusted data
    ax2.tick_params(axis='y', labelcolor='tab:green')

    # Set the y-axis limits for temperature anomalies
    max_anomaly = max(combined_df_filtered['Land_Anomaly'].abs().max(), combined_df_filtered['Ocean_Anomaly'].abs().max())
    ax1.set_ylim(-max_anomaly, max_anomaly)

    # Set major ticks on the left y-axis to be symmetric around zero and show only a specific range of values
    tick_values = np.arange(-2, 4, 1)  # Adjust as needed
    ax1.set_yticks(tick_values)

    fig.tight_layout()
    plt.title('Global Population vs Temperature Anomalies')  # Adjusted title
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

    plt.show()


# Function to visualize population growth vs global protected area
def visualize_population_and_protected_area(population_iso_df, protected_areas_df):
    # Group protected areas data by year and sum the total protected area
    protected_area_by_year = protected_areas_df.groupby(protected_areas_df['STATUS_YR'])['REP_AREA'].sum().cumsum()

    # Group population data by year and sum the global population
    global_population_by_year = population_iso_df.groupby(population_iso_df['Year'].dt.year)['Population'].sum()

    # Filter population data to match the range of years in the protected areas data
    global_population_by_year = global_population_by_year.loc[protected_area_by_year.index.min():]

    # Plotting population growth vs global protected area
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(global_population_by_year.index, global_population_by_year.values, label='Global Population', color='blue')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Global Population (Billions)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(protected_area_by_year.index, protected_area_by_year.values, label='Global Protected Area', color='green')
    ax2.set_ylabel('Cumulative Global Protected Area (sq km)', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    plt.title('Population Growth vs Cumulative Global Protected Area')
    fig.tight_layout()
    plt.grid(True)
    plt.xlim(1950, protected_area_by_year.index.max())  # Adjust x-axis range
    plt.show()


# Function to visualize protected areas
def visualize_protected_areas(protected_areas_df):
    # Aggregate total protected area for each country
    aggregated_df = protected_areas_df.groupby('country_name')['REP_AREA'].sum().reset_index()
    
    # Sort the aggregated DataFrame by total protected area
    sorted_df = aggregated_df.sort_values(by='REP_AREA', ascending=False)
    
    # Take the top 10 countries
    top_10_df = sorted_df.head(10)
    
    # Plotting protected areas
    plt.figure(figsize=(10, 8))  # Adjusted figure size
    sns.barplot(x='REP_AREA', y='country_name', data=top_10_df, palette='viridis', orient='h')  # Horizontal bar plot
    plt.title('Top 10 Countries with Highest Total Protected Area')
    plt.xlabel('Total Protected Area (sq km)')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    protected_areas_df, population_iso_df, combined_df = preprocess_data()
    graph = Graph()  # Initialize a graph object
    interact_with_data(protected_areas_df, population_iso_df, combined_df, graph)
