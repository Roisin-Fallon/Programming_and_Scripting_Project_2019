# Roisin Fallon
# Adapted from: https://stackoverflow.com/a/45721331

import matplotlib.pyplot as plt
from sklearn import datasets

ds= datasets.load_iris()                                                                                                                      # Load the iris data set   

fig, axes = plt.subplots(2, 2, figsize=(12, 10), dpi=100)                                                                                     # plot the figures 2 rows and 2 columns on the same plot
plt.suptitle("Fisher Iris data set represented using Histograms ",fontweight="bold", fontsize="12", color="g" )                               # Title for the overall graph
colors= ['dodgerblue', 'orange', 'deeppink']                                                                                                  # colors given to each species                                                        

for i, ax in enumerate(axes.flat):                                                                                                            #  for statement to produce four histograms in a facetted 2 x 2 grid.
    for label, color in zip(range(len(ds.target_names)), colors):                                                                             # Iterates through the for loop to add below contents
        ax.hist(ds.data[ds.target==label, i], label=ds.target_names[label], color=color, bins=20, edgecolor='black', alpha = 0.7)
        ax.set_xlabel(ds.feature_names[i], fontweight="bold", fontsize="10", color="b")                                                       # Label of the x-axis
        ax.set_ylabel("Frequency", fontweight="bold", fontsize="10", color="b")                                                               # Label of the y-axis
        ax.legend()                                                                                                                           # Add legend to the histogram                                                                                                                                                                             
plt.show()                                                                                                                                    # Display the boxplot

