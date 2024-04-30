**Project Name: Environmental Data Analysis**

**Description:**
This project provides a platform for analyzing and visualizing environmental data related to temperature anomalies, population demographics, and protected areas across different countries. It offers various interactions to explore and understand trends in global environmental data.

**Interactions:**
1. Get population of a country by year (1950-2021)
   - Prompt: Enter country name, Alpha-2 code, or Alpha-3 code.
   - Answer: Population of the specified country in the given year.

2. Get global temperature anomalies by year (1950-2021)
   - Prompt: Enter the year (in YYYY format).
   - Answer: Average temperature anomalies for land and ocean surfaces in the specified year.

3. Get global population by year (1950-2021)
   - Prompt: Enter the year (in YYYY format).
   - Answer: World population in the specified year.

4. Get total protected area of all countries
   - Answer: Total protected area across all countries.

5. Get total protected area of a country
   - Prompt: Enter country name, Alpha-2 code, or Alpha-3 code.
   - Answer: Total protected area of the specified country.

6. Visualize global population vs temperature anomalies
   - Graphical output: Line plot showing global population trend alongside temperature anomalies for land and ocean surfaces.

7. Visualize top countries by total protected area
   - Graphical output: Bar plot displaying the top 10 countries with the highest total protected areas.

8. Visualize population growth vs global protected area
   - Graphical output: Line plot illustrating population growth trend compared to cumulative global protected area.

9. Perform graph operations
   - **1. Add Node:** Add a country node by entering its name or code.
   - **2. Add Edge:** Connect two countries with an edge.
   - **3. Visualize Network:** View the protected areas network graph.
   - **4. Exit:** Return to the main menu.
   Simply select the desired option and follow the prompts to interact with the graph.

10. Exit: Terminate the program.

**Special Instructions:**
- Ensure all required data files (`protected_areas.csv`, `population_and_demography.csv`, `iso_codes.csv`, `land.json`, `ocean.json`) are present in the project directory.
- No API keys are needed to run the program.

**Required Python Packages:**
- pandas
- matplotlib
- seaborn
- numpy
- networkx

**Network (Graph) Organization:**
- **Nodes:** Each node represents a country.
- **Edges:** Edges represent connections between countries, indicating relationships or interactions.

---

**Data Sources**

**Land Data**
- **Origin:** NOAA Climate Monitoring - https://www.ncei.noaa.gov/monitoring
- **Format:** JSON
- **Access Method:** Direct download from the provided URL.
- **Summary:** The `land.json` file contains time-series data of temperature anomalies for land surfaces globally. It covers the period from 1850 to 2024.
- **Records Available:** Time-series data.
- **Records Retrieved:** All available records from 1850 to 2024.
- **Description:** Each record in the JSON file represents a specific year and its corresponding temperature anomaly for land surfaces. The data provides insights into the deviations in land surface temperatures from a long-term average.

**Ocean Data**
- **Origin:** NOAA Climate Monitoring - https://www.ncei.noaa.gov/monitoring
- **Format:** JSON
- **Access Method:** Direct download from the provided URL.
- **Summary:** The `ocean.json` file contains time-series data of temperature anomalies for ocean surfaces globally. It covers the period from 1850 to 2024.
- **Records Available:** Time-series data.
- **Records Retrieved:** All available records from 1850 to 2024.
- **Description:** Similar to `land.json`, each record in the JSON file represents a specific year and its corresponding temperature anomaly for ocean surfaces. The data offers insights into the deviations in ocean surface temperatures from a long-term average.

**Population and Demography Data**
- **Origin:** Our World in Data - Population and Demography - https://ourworldindata.org/explorers/population-and-demography
- **Format:** CSV
- **Access Method:** Accessed and downloaded directly from the provided URL.
- **Summary:** The `population_and_demography.csv` file contains data on population demographics across different countries from 1950 to 2021.
- **Records Available:** Country-wise population data over time.
- **Records Retrieved:** All available records.
- **Description:** Each record in the CSV file represents population statistics for a specific country and year. Important fields include country name, year, and population count. This data provides insights into global population trends and demographics.

**Protected Areas Data**
- **Origin:** World Database on Protected Areas (WDPA) - https://www.protectedplanet.net/en
- **Format:** CSV
- **Access Method:** Accessed and downloaded from the provided URL.
- **Summary:** The `protected_areas.csv` file contains information about protected areas across different countries.
- **Records Available:** Records of protected areas in various countries.
- **Records Retrieved:** All available records.
- **Description:** Each record in the CSV file represents a protected area, including attributes such as area size, country, and protection status. This data is crucial for understanding global conservation efforts and the extent of protected natural habitats.

**ISO Codes Data**
- **Origin:** Kaggle Dataset - Countries ISO Codes - https://www.kaggle.com/datasets/juanumusic/countries-iso-codes
- **Format:** CSV
- **Access Method:** Downloaded from the provided Kaggle dataset.
- **Summary:** The `iso_codes.csv` file contains ISO country codes and corresponding country names.
- **Records Available:** ISO codes and country names.
- **Records Retrieved:** All available records.
- **Description:** Each record in the CSV file represents a country along with its ISO codes (Alpha-2 and Alpha-3) and country name. This data is used to link the other datasets through ISO3 and country name for integration and analysis purposes.

---
