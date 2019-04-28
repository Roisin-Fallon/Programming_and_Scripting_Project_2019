# Roisin Fallon
# Adapted from: https://seaborn.pydata.org/generated/seaborn.pairplot.html; https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid

# Import the following libraries:
import matplotlib.pyplot as plt                                                                                                 # matplotlib given an alias plt
import seaborn as sns                                                                                                           # seaborn given as alias sns                                                                                              
import pandas as pd                                                                                                             # pandas given an alias of pd 
import warnings                                                                                                                 # current version of seaborn creates warnings this will remove them
warnings.filterwarnings("ignore")

ds = pd.read_csv("iris.csv", delimiter=",")                                                                                     # Load iris dataset

# Pairplot using distplot and scatterplot   
sns.pairplot(ds, hue="species",  kind = "reg", markers=[".", "d", "+"],  height=2.3, aspect=1.9)                                # Each species is seperated by color and marker 
plt.suptitle("Fisher Iris Pairplot using displot and scatterplot", fontweight="bold", fontsize="12", color="g" )                # Overall heading for the graph                                                                              
plt.subplots_adjust(top=.9)                                                                                                     # Leave space so it does not cover the figure
plt.show()                                                                                                                      # Display the pairplot 


# PairGrid with histogram and scatterplot

g = sns.PairGrid(ds, hue="species", hue_kws={"marker": [".", "d", "+"]}, height=2.3, aspect=1.9)                                # Each species is seperated by color and marker 
g.map_diag(plt.hist, histtype="step", linewidth=3, bins=20)                                                                     # Histograms are created diagonally where bins, histtep was
g.map_offdiag(plt.scatter)                                                                                                      # Scatterplots are created in the remaining figure 
g.add_legend()                                                                                                                  # Add legend
g.fig.suptitle("Fisher Iris Pairplot using histogram and scatterplot", fontweight="bold", fontsize="12", color="g" )            # Overall heading for the graph  
g.fig.subplots_adjust(top=.9)                                                                                                   # Leave space so it does not cover the figure
plt.show()                                                                                                                      # Display the pairplot 

