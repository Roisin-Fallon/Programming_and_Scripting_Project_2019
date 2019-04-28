# Roisin Fallon
# Adopted from:
# Plotting the Iris dataset  https://www.machinelearningplus.com/plots/matplotlib-histogram-python-examples/

# Import the following libraries:
import pandas as pd                                                                                             # pandas given an alias pd
import matplotlib.pyplot as plt                                                                                 # matplotlib given an alias plt
import seaborn as sns                                                                                           # seaborn given as alias sns
import warnings                                                                                                 # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")

ds = pd.read_csv("iris.csv", delimiter=",")                                                                     # Read in the CSV as dataframe


f, axes = plt.subplots(2, 2, figsize=(12, 10), dpi=100)                                                         # Figsize and dpi(dot-per-inch)
plt.suptitle("Fisher Iris Distribution of Data",fontweight="bold", fontsize="12", color="g" )                   # Overall heading for the graph

plt.subplot(2,2,1)                                                                                              # Makes a top left subplot active in a 2x2 subplot layout
sns.distplot(ds.loc[ds.species=='setosa', "sepal_length"] , color="dodgerblue", label="setosa")                 # Plot setosa species sepal length
sns.distplot(ds.loc[ds.species=='virginica', "sepal_length"] , color="orange", label="virginica")               # Plot virginica species sepal length
sns.distplot(ds.loc[ds.species=='versicolor', "sepal_length"] , color="deeppink", label="versicolor")           # Plot versicolor species sepal length
plt.xlabel("Sepal Length", fontweight="bold", fontsize="12", color="b")                                         # Label of the x-axis
plt.ylabel("Count", fontweight="bold", fontsize="12", color="b")                                                # Label of the y-axis
plt.title("Iris Sepal Length Histogram", fontweight="bold", fontsize="10", color="r")                           # Label title of distplot

plt.subplot(2,2,2)                                                                                              # Makes a top right subplot active in a 2x2 subplot layout
sns.distplot( ds.loc[ds.species=='setosa', "sepal_width"] , color="dodgerblue", label="setosa")                 # Plot setosa species sepal width
sns.distplot( ds.loc[ds.species=='virginica', "sepal_width"] , color="orange", label="virginica")               # Plot virginica species sepal width
sns.distplot( ds.loc[ds.species=='versicolor', "sepal_width"] , color="deeppink", label="versicolor")           # Plot versicolor species sepal width
plt.xlabel("Sepal Width", fontweight="bold", fontsize="12", color="b")                                          # Label of the x-axis
plt.ylabel("Count", fontweight="bold", fontsize="12", color="b")                                                # Label of the y-axis
plt.title('Iris Sepal Width Histogram', fontweight="bold", fontsize="10", color="r")                            # Label title of distplot


plt.subplot(2,2,3)                                                                                              # Makes a bottom left subplot active in a 2x2 subplot layout
sns.distplot( ds.loc[ds.species=='setosa', "petal_length"] , color="dodgerblue", label="setosa")                # Plot setosa species petal length
sns.distplot( ds.loc[ds.species=='virginica', "petal_length"] , color="orange", label="virginica")              # Plot virginica species petal length
sns.distplot( ds.loc[ds.species=='versicolor', "petal_length"] , color="deeppink", label="versicolor")          # Plot versicolor species petal length
plt.xlabel("Petal Length", fontweight="bold", fontsize="12", color="b")                                         # Label of the x-axis
plt.ylabel("Count", fontweight="bold", fontsize="12", color="b")                                                # Label of the y-axis
plt.title('Iris Petal Length Histogram', fontweight="bold", fontsize="10", color="r")                           # Label title of distplot


plt.subplot(2,2,4)                                                                                             # Makes a bottom right subplot active in a 2x2 subplot layout
sns.distplot( ds.loc[ds.species=='setosa', "petal_width"] , color="dodgerblue", label="setosa")                # Plot setosa species petal width
sns.distplot( ds.loc[ds.species=='virginica', "petal_width"] , color="orange", label="virginica")              # Plot virginica species petal width
sns.distplot( ds.loc[ds.species=='versicolor', "petal_width"] , color="deeppink", label="versicolor")          # Plot versicolor species petal width
plt.xlabel("Petal Width", fontweight="bold", fontsize="12", color="b")                                         # Label of the x-axis
plt.ylabel("Count", fontweight="bold", fontsize="12", color="b")                                                # Label of the y-axis
plt.title('Iris Petal Width Histogram', fontweight="bold", fontsize="10", color="r")                           # Label title of distplot

plt.legend(bbox_to_anchor=(1,2), loc=2)                                                                        # Legend for the overall plot
plt.show()                                                                                                     # Display the distplot


