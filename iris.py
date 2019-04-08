
#Import the following libraries:

import numpy as np                                                # numpy given an alias performs calculations
import pandas as pd                                               # pandas given an alias pd
import matplotlib.pyplot as plt                                   # matplotlib given an alias plt

# read the csv file
sp = pd.read_csv("iris.csv", delimiter=",")
print(sp)

# Dataframe for each species: 
# Adapted from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

setosa=sp[sp['species']=='setosa']
versicolor =sp[sp['species']=='versicolor']
virginica =sp[sp['species']=='virginica']


# Dataset Summary: 
# Check head (first) 4 for each of the species) of the dataset:

print(setosa.head(4))
print(versicolor.head(4))
print(virginica.head(4))

# Check tail (last 4 for each of the species) of the dataset:

print(setosa.tail(4))
print(versicolor.tail(4))
print(virginica.tail(4))

# Check how many rows and columns there are in our data
print(sp.shape)                                                       

# Check how many unique species of iris are in the dataset
print(sp['species'].unique())                                                

# Class distribution -number of rows that belong to each class 
print(sp.groupby('species').size())                                             

# To summarise the data for iris overall dataset
print(sp.describe())

# To summarise the data for iris overall iris setosa
summary = print(setosa.describe())

# To summarise the data for iris overall iris versicolor                                             
print(versicolor.describe())

# To summarise the data for iris overall iris virginica                                            
print(virginica.describe())





