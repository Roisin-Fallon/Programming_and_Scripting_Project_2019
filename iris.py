# Roisin Fallon

# Import the following libraries:
# Adopted from: https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python ; https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

import pandas as pd                                               # pandas given an alias pd

# read the csv file
ds = pd.read_csv("iris.csv", delimiter=",")

# Dataframe for each species: 
# Adapted from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# https://www.kaggle.com/prashantsaraswat123/iris-species-dataset-analysis
setosa=ds[ds['species']=='setosa']
versicolor =ds[ds['species']=='versicolor']
virginica =ds[ds['species']=='virginica']


# Dataset Summary: 

# Check how many rows and columns there are in our data
print("Number of rows and columns:")  
print(ds.shape)                                                       
print("\n")

# Check how many rows and columns there are in our data
print("Name of each column in the iris dataset:")  
print(ds.columns)                                                       
print("\n")

# Determine data columns data type:
print("Information about iris dataset:") 
print(ds.info())
print("\n")

# Check how many unique species of iris are in the dataset
print("Unique species:")  
print(ds['species'].unique())                                                
print("\n")

# Determine if there is any null values in the dataset
print("Null values present:")
print(ds.isnull().any())
print("\n")

# Class distribution -number of rows that belong to each class 
print("Class Distribution:")  
print(ds.groupby('species').size())                                             
print("\n")

# Check head (first) 4 for each of the species) of the dataset:

print("First 4 setosa values:") 
print(setosa.head(4))
print("\n")

print("First 4 versicolor values:") 
print(versicolor.head(4))
print("\n")

print("First 4 virginica values:") 
print(virginica.head(4))
print("\n")

# Check tail (last 4 for each of the species) of the dataset:

print("Last 4 setosa values:")  
print(setosa.tail(4))
print("\n")

print("Last 4 versicolor values:")  
print(versicolor.tail(4))
print("\n")

print("Last 4 virginica values:")  
print(virginica.tail(4))
print("\n")

# To summarise the data for iris overall dataset
print("Summary statistics for iris entire dataset:")
print(ds.describe())
print("\n")                                                             # Line Break

# To summarise the data for iris overall iris setosa
print("Summary statistics for iris setosa dataset:")
summary = print(setosa.describe())
print("\n")

# To summarise the data for iris overall iris versicolor 
print("Summary statistics for iris versicolor dataset:")                                            
print(versicolor.describe())
print("\n")

# To summarise the data for iris overall iris virginica  
print("Summary statistics for iris virginica dataset:")                                          
print(virginica.describe())
print("\n")







