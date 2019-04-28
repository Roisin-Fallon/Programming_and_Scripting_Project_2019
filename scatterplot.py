# Roisin Fallon
# Adapted from: https://seaborn.pydata.org/generated/seaborn.scatterplot.html

# Import the following libraries:
import pandas as pd                                                                                             # pandas given an alias pd
import matplotlib.pyplot as plt                                                                                 # matplotlib given an alias plt
import seaborn as sns                                                                                           # seaborn given as alias sns
import warnings                                                                                                 # current version of seaborn creates warnings this will remove them
warnings.filterwarnings("ignore")

ds = pd.read_csv("iris.csv", delimiter=",")


# Scatterplot for petal comparasion for each species 

sns.scatterplot(x="petal_length", y="petal_width", hue="species",style= ds.species, data=ds)                    # Plot petal length and width for each species 
plt.xlabel("Petal Length (cm)", fontweight="bold", fontsize="12", color="b")                                    # Format of the x-axis
plt.ylabel("Petal Width (cm)", fontweight="bold", fontsize="12", color="b")                                     # Format of the y-axis
plt.title("Petal Comparasion for each species", fontweight="bold", fontsize="12", color="r")                    # Title of graph
plt.show()

# Scatterplot for sepal comparasion for each species 

sns.scatterplot(x="sepal_length", y="sepal_width", hue="species",style=ds.species, data=ds)                     # Plot sepal length and width for each species 
plt.xlabel("Sepal Length (cm)", fontweight="bold", fontsize="12", color="b")                                    # Format of the x-axis
plt.ylabel("Sepal Width (cm)", fontweight="bold", fontsize="12", color="b")                                     # Format of the y-axis
plt.title("Sepal Comparasion for each iris species", fontweight="bold", fontsize="12", color="r")               # Title of graph

plt.show()                                                                                                      # Display the scatterplot
