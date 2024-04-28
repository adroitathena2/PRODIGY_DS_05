import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#DATA PRE-PROCESSING
df=pd.read_csv('C:\\Users\\archi\\Documents\\INTERNSHIPS\\PRODIGY INFOTECH\\Task 5\\Accident.csv')
df.head()
df.describe
df.shape
df.info()

#HANDLING MISSING AND DUPLICATE VALUES
df.duplicated().sum() #finding duplicate values

#dropping columns which has more than 2500 missing values and Time column
df.drop(['Service_year_of_vehicle','Defect_of_vehicle','Work_of_casuality', 'Fitness_of_casuality','Time'],
        axis = 1, inplace = True)
df.head()

#storing categorical column names to a new variable
categorical=[i for i in df.columns if df[i].dtype=='O']
print('Categorical variables:',categorical)
     

#for categorical values we can replace the null values with its Mode
for i in categorical:
    df[i].fillna(df[i].mode()[0],inplace=True)

#checking the current null values
df.isna().sum()

#EXPLORATORY DATA ANALYSIS
#Distribution of Accident severity
df['Accident_severity'].value_counts()
     
#Bar plot for accident severity distribution
sns.countplot(x=df['Accident_severity'], palette='Paired')
plt.title('Distribution of Accident severity')
plt.show()


sns.lineplot(x=df['Number_of_casualties'], y=df['Number_of_vehicles_involved'], hue=df['Accident_severity'])
plt.title('Relationship between Number of Casualties and Number of Vehicles Involved')
plt.xlabel('Number of Casualties')
plt.ylabel('Number of Vehicles Involved')
plt.show()

# Calculate mean values
mean_values = df.groupby('Number_of_casualties')['Number_of_vehicles_involved'].mean().reset_index()

# Plotting line chart
plt.plot(mean_values['Number_of_casualties'], mean_values['Number_of_vehicles_involved'], marker='o', linestyle='-')
plt.title('No. of Vehicles Involved vs No. of Casualties')
plt.xlabel('No. of Casualties')
plt.ylabel('No. of Vehicles Involved')
plt.grid(True)
plt.show()

# Drop non-numeric columns
numeric_df = df.select_dtypes(include=['number'])

# Calculate correlation
correlation_matrix = numeric_df.corr()

# Display correlation matrix
print(correlation_matrix)


#plotting the correlation using heatmap
# Select only numeric columns
numeric_df = df.select_dtypes(include=['number'])

# Calculate correlation matrix
correlation_matrix = numeric_df.corr()

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="Spectral", fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

#storing numerical column names to a variable
numerical=[i for i in df.columns if df[i].dtype!='O']
print('The numerical variables are',numerical)

