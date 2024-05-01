### Environmental Data Analysis
by dyel

**Description:**
This project provides a platform for analyzing and visualizing environmental data related to temperature anomalies, population demographics, and protected areas across different countries. It offers various interactions to explore and understand trends in global environmental data.

**Interactions:**
1. **Get population of a country by year (1950-2021):**
   - Prompt: Enter country name, Alpha-2 code, or Alpha-3 code.
   - Answer: Population of the specified country in the given year.

2. **Get global temperature anomalies by year (1950-2021):**
   - Prompt: Enter the year (in YYYY format).
   - Answer: Average temperature anomalies for land and ocean surfaces in the specified year.

3. **Get global population by year (1950-2021):**
   - Prompt: Enter the year (in YYYY format).
   - Answer: World population in the specified year.

4. **Get total protected area of all countries:**
   - Answer: Total protected area across all countries.

5. **Get total protected area of a country:**
   - Prompt: Enter country name, Alpha-2 code, or Alpha-3 code.
   - Answer: Total protected area of the specified country.

6. **Visualize global population vs temperature anomalies:**
   - Graphical output: Line plot showing global population trend alongside temperature anomalies for land and ocean surfaces.

7. **Visualize top countries by total protected area:**
   - Graphical output: Bar plot displaying the top 10 countries with the highest total protected areas.

8. **Visualize population growth vs global protected area:**
   - Graphical output: Line plot illustrating population growth trend compared to cumulative global protected area.

9. **Perform clustering and visualize clusters:**
   - Graphical output: Scatter plot showing clusters of countries based on population and total protected area.

10. **Exit:** Terminate the program.

**Special Instructions:**
- Ensure all required data files (`protected_areas.csv`, `population_and_demography.csv`, `iso_codes.csv`, `land.json`, `ocean.json`) are present in the project directory.
- No API keys are needed to run the program.

**Required Python Packages:**
- pandas
- matplotlib
- seaborn
- numpy
- networkx
- sklearn

**Network (Graph) Organization:**
- **Nodes:** Each node represents a country.
- **Edges:** Edges represent connections between countries, indicating relationships or interactions.
