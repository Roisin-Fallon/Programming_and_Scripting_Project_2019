# Roisin Fallon
# Import the following libraries:

import pandas as pd                                                                                         # pandas given an alias pd
import matplotlib.pyplot as plt                                                                             # matplotlib given an alias plt
import seaborn as sns                                                                                       # seaborn given as alias sns

ds = pd.read_csv("iris.csv", delimiter=",")                                                                 # Read in the CSV as dataframe

# Boxplot of the total iris dataset not specified for species
plt.figure(figsize=(12,10))                                                                                 # Resize the boxplot
sns.boxplot(data=ds)                                                                                        # Load iris datset via seaborne 
# Format of boxplot 
plt.title("Fisher Iris Species", fontweight="bold", fontsize="16", color="r")                               # Title of graph
plt.ylabel("centimeters", fontweight="bold", fontsize="12", color="b")                                      # Label of the y-axis
plt.show()                                                                                                  # Display the boxplot 

# Boxplot to represent each of the 3 species and each of the three 
# Adapted from https://stackoverflow.com/a/40242457

plt.figure(figsize=(14,10))                                                                                 # Resize the boxplot
ds_long = pd.melt(ds, id_vars='species')                                                                    # melt allows the graphs to appear together 
sns.boxplot(x='species', y='value', hue='variable', data=ds_long)                                           # ds_long refers to the format appearing as long rather than wide

plt.title("Fisher Iris Species", fontweight="bold", fontsize="16", color="r")                               # Title of graph
plt.ylabel("centimeters", fontweight="bold", fontsize="12", color="b")                                      # Label of the y-axis
plt.xlabel("Species", fontweight="bold", fontsize="12", color="b")                                          # Label of the x-axis
plt.legend(bbox_to_anchor=(1, 1), loc=2)                                                                    # Legend of the data 
plt.margins(0)                                                                                              # Margin to start at zero 
for i in range(len(ds['species'].unique())-1):                                                              # Creates a division between the 3 species
    plt.vlines(i+.5, 0, 8)                                                                                  # Adopted from: https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#26.-Box-Plot

plt.show()                                                                                                  # Display the boxplot

# Boxplot to compare each of the attributes in the 3 species:
# Adapted from:
# https://s3.amazonaws.com/assets.datacamp.com/production/course_5368/slides/chapter4.pdf
# http://www.learn4master.com/machine-learning/visualize-iris-dataset-using-python



plt.figure(figsize=(12,10))                                                                                # Figure Size
plt.suptitle("Fisher Iris dataset grouped by species",fontweight="bold", fontsize="12", color="g" )        # Title of overall graph

plt.subplot(2,2,1)
plt.title("Sepal Length", fontweight="bold", fontsize="12", color="r")                                     # Title of graph
plt.ylabel("Sepal Length", fontweight="bold", fontsize="10", color="b")                                    # Label of the y-axis
plt.xlabel("Species", fontweight="bold", fontsize="10", color="b")                                         # Label of the x-axis
sns.boxplot(x="species",y="sepal_length",data=ds)

plt.subplot(2,2,2)
plt.title("Sepal Width", fontweight="bold", fontsize="12", color="r")                                     # Title of graph
plt.ylabel("Sepal Width", fontweight="bold", fontsize="10", color="b")                                    # Label of the y-axis
plt.xlabel("Species", fontweight="bold", fontsize="10", color="b")                                        # Label of the x-axis     
sns.boxplot(x="species",y="sepal_width", data=ds)

plt.subplot(2,2,3)
plt.title("Petal Length", fontweight="bold", fontsize="12", color="r")                                    # Title of graph
plt.ylabel("Petal Length", fontweight="bold", fontsize="10", color="b")                                   # Label of the y-axis
plt.xlabel("Species", fontweight="bold", fontsize="10", color="b")                                        # Label of the x-axis  
sns.boxplot(x="species",y="petal_length",data=ds)

plt.subplot(2,2,4)
plt.title("Petal Width", fontweight="bold", fontsize="12", color="r")                                     # Title of graph
plt.ylabel("Petal Width", fontweight="bold", fontsize="10", color="b")                                    # Label of the y-axis
plt.xlabel("Species", fontweight="bold", fontsize="10", color="b")                                        # Label of the x-axis
sns.boxplot(x="species",y="petal_width",data=ds)

plt.show()                                                                                                # Display the boxplot
