# PRODIGY_DS_05
Problem Statement: Analyze traffic accident data to identify patterns related to road conditions, weather, and time of day. Visualize accident hotspots and contributing factors.

---

# Project Workflow: Traffic Accident Data Analysis

## Step 1: Data Preprocessing
Load the traffic accident dataset and inspect its structure. This involves checking the first few rows, summary statistics, and data types for each column. The goal is to understand the data and identify any initial issues such as duplicates or missing values.

## Step 2: Handling Duplicates and Missing Values
Identify and remove any duplicate rows in the dataset. Check for columns with a significant number of missing values and decide on a strategy to handle them. For this project, columns with excessive missing data and irrelevant information are dropped. For categorical columns, missing values are filled with the most common value (mode).

## Step 3: Exploratory Data Analysis (EDA)
Explore the dataset to understand the distribution of key variables and relationships between them. Start by analyzing the distribution of accident severity to get an overview of the different severity levels in the dataset.

### Accident Severity Distribution
Create a bar plot to visualize the distribution of accident severity. This helps in understanding the proportion of accidents at different severity levels.
![Figure_1](https://github.com/adroitathena2/PRODIGY_DS_05/assets/143172958/ac8bf30b-49f6-46f2-8daf-b6dad7653bf5)

### Relationships Between Key Variables
Investigate relationships between important variables, such as the number of casualties and the number of vehicles involved in accidents. A line plot can be used to visualize this relationship, with the data categorized by accident severity.
![Figure_2](https://github.com/adroitathena2/PRODIGY_DS_05/assets/143172958/d43653cd-d939-418a-a8f4-89e1df8d1682)
![Figure_3](https://github.com/adroitathena2/PRODIGY_DS_05/assets/143172958/02a8ffcc-e180-4adf-8abc-e793fe24c9ea)

## Step 4: Correlation Analysis
Focus on the numeric columns to examine correlations between different variables. A correlation matrix provides a clear view of the relationships between numerical variables.

### Correlation Heatmap
Use a heatmap to visualize the correlation matrix. This visual representation helps to quickly identify strong correlations, indicating which variables might have a significant impact on accident outcomes.
![Figure_4](https://github.com/adroitathena2/PRODIGY_DS_05/assets/143172958/20d6ba2a-af3a-4070-9cd5-58ace32c0e69)

## Step 5: Storing Numerical and Categorical Variables
Store the names of numerical and categorical columns in separate lists for further analysis. This step ensures a clear separation between different types of data and facilitates subsequent analysis.

## Conclusion
This workflow outlines the basic steps for preprocessing and exploring traffic accident data, focusing on identifying patterns and relationships that could reveal insights into road conditions, weather, and other factors influencing accident severity. Further analysis could include deeper dives into specific correlations, predictive modeling, or accident hotspot visualization.


