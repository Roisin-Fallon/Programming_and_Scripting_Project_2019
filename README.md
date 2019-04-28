# Programming_and_Scripting_Project_2019


### Table of Contents

1. [ Introduction ](#intro)
2. [ Data Set ](#data)
3. [ Python Libraries ](#lib)
4. [ Iris dataset csv ](#lib)
5. [ Discrepancies in the Iris Dataset ](#disc)
6. [ Dataset Summary ](#sum)
7. [ Dataset Summary](#sum)
    * [Shape](#shape)
    * [ Columns ](#columns)
    * [ Info ](#info)
    * [ Unique Species ](#unique)
    * [ Null Values ](#isnull)
    * [ Class Distribution ](#class)
    * [ Head of each species ](#head)
    * [ Tail of each species ](#tail)
8. [Statistics of the Iris Dataset](#stat)
9. [Visualize the dataset](#visualize)
    * [Boxplot](#box)
    * [ Histograms ](#hist)
    * [Distplot ](#dist)
    * [ Scatterplot ](#scatter)
    * [ Pairplot ](#pair)
10. [Conclusion](#con)
11. [Bibliography](#bib)
    



<a name="intro"></a>
## Introduction:

<p align="center">
   <img src="http://people.wku.edu/charles.smith/chronob/ANDERSON.jpg" width="300" title="Edgar Anderson" > <img src="http://www.genetics.org/content/genetics/154/4/1419/F1.medium.gif " width="263" title="Ronald Fisher"> 
</p>

The iris dataset originated from research carried out by Edgar Anderson (American botanist) in 1935, whom collected three species of the iris flower with a goal to quantify the morphological variation. Two of the three species were collected in the Gaspé Peninsula "The irises of the Gaspé Peninsula".[11]. 
  
Ronald Fisher adapted Anderson data to determine if linear regression could be applied to this data set. In 1936 Fisher published a paper “maximize the ratio of the difference between the specific means to the standard deviation within species”.  [2;1]  It is important to understand that Fisher focused on the linear discrimination analysis. The Iris flower data set or Fisher’s Iris data set is a multivariate data set introduced by Sir Ronald Fisher (1936) as an example of discriminant analysis.[1] Since its publication Fisher's paper has been cited over 2000 times [12]. 
  
 <a name="data"></a>
 ## Data Set:
 <p align="center">
 <img src="https://sudaniscience.files.wordpress.com/2018/10/9.png?w=720 " width="800" title="Iris flower species"> 
</p>
 
Is dataset is multivariate which involves analysis of two or more variables


The data set consists of:

- Data size: 150 random observations
- Data distribution: 50 entries for each class
- There is no missing data
- Iris dataset is classified into 5 variables

  - Flower species- Categorical data can be divided into 3 classes
    - Iris setosa
    - Iris virginica 
    - Iris versicolor
  - 4 numeric features measure in cm
    - Petal width in cm 
    - Petal length in cm 
    - Sepal width in cm 
    - Sepal length in cm 


Image below depicts the difference between the petal and sepal.  Sepal is defined as the outermost structure of the flower, that  surround the more fragile parts of the flower .e.g. petals. Typically the petals can be  distinguished as being small and green  and the petals are colorful. However, this is not applicable to the iris flower species. Note in this image of the Iris Virginica  the sepals are larger than the petals  and are drooping, while the petals are upright.

Based on the combination of the four numeric features, the classification of the iris flower is made.  
One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.
 
 <p align="center">
<img src="https://www.oreilly.com/library/view/python-artificial-intelligence/9781789539462/assets/462dc4fa-fd62-4539-8599-ac80a441382c.png" width="263" title="Attributes measured"> 

</p>


<a name="lib"></a>
## Python Libraries:

<b> Anaconda on your device (version 3.7 +) </b>

 <a href=https://www.anaconda.com/distribution/> Download here </a>

This contains porting for the library listed below. By downloading Anaconda it removes the need to import numerous libraries seperately.
 
 <b> Pandas </b> 
 
 <a href=https://pandas.pydata.org/getpandas.html> Download here </a>
 
This is a Python package designed to strucure information in rows and columns.  It is known for quick and easy data manipulation, aggregation, and visualization.  Python takes in data via a CSV, TSV file or SQL database and creates a Python object called a data frame. Brief Introducton of Panda outlined <a href=https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673> here. </a>

<b> NumPy </b> 

<a href=http://www.numpy.org/> Download here </a>

This is a numerical library, performs many mathematical operations and handles i.  Brief introductiion outlined <a href=https://towardsdatascience.com/a-quick-introduction-to-the-numpy-library-6f61b7dee4db> here. </a>

<b> Matplotlib </b> 

<a href=https://matplotlib.org/downloads.htmll> Download here </a>

This is a plotting library, makes  2D plots  that helps in the visualisation of figures using one or multiple numeric variables. It can generate histograms, pie charts, time series, boxplot, violin plot, stack plot, stem plots and scatter plots.  It can be used in Python scripts, Jupyter notebook, and web application servers.  Brief Introduction outlined  <a href=https://towardsdatascience.com/data-visualization-using-matplotlib-16f1aae5ce70> here. </a>

<b> Seaborn </b>

This a satistical plotting library  which has more advanced data visualisation than matplotlib (both are plotting libraries). Seaborn produces nice visualizations eliminating much of the work necessary for producing similar visualizations with matplotlib. It gives a high-level interface to draw statistical graphs, making it easier to generate more complex visualizations. Brief introduction outlined <a href=https://towardsdatascience.com/data-visualization-using-seaborn-fc24db95a850> here. </a>

<b> Scikit-learn </b>

Simple and efficient tool that can be used for data miming or data analysis. It's library contains a lot of effiecient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction. It comes as part of the anaconda package Brief introduction outlined <https://scikit-learn.org/stable/install.html > here. </a>




<a name="imp"></a>

## Iris dataset csv:

 <a href=https://gist.github.com/curran/a08a1080b88344b0c8a7> Download here </a>

The iris dataset used in this project had headings added prior to its download. Hence I did not need to add headings when file was imported uisng panda. 

<details><summary>Read the iris.csv</summary>
<p>
ds = pd.read_csv("iris.csv", delimiter=",")                                                       # Read in the CSV as dataframe
 
</p>
</details>

<a name="disc"></a>
## Discrepancies in the Iris Data Set:

Steve Chadwick identified a number of discrepancies between the dataset used in this project and the data originally published by Fisher [9]. The differences are outlined below and affect the Iris Setosa species:

|Sample Number  | Iris Feature  |     FisherOriginal Data  | Data used  |
| ------------- | ------------- |  -------------  | ------------- |
|      35     	 |  petal_width  |        0.2      |       0.1     |
|      38       |  sepal_width  |        3.6      |       3.1     |
|      38       |  petal_length |        1.4      |       1.5     |

  
<a name="lib"></a>

<a name="sum"></a>
## Dataset Summary: 

<a name="shape"></a>
<b> A. Shape </b>

Confirms the shape of the iris dataset in terms of the number of rows and columns. 

<details><summary>Python Code</summary>
<p>
 
      print("Number of rows and columns:")  
      print(ds.shape)                                                       
      print("\n")
 
</p>
</details>
   
![Shape of Iris dataset](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/shape.PNG)
 
 <a name="columns"></a>
 <b> B. Columns </b>
    
 The names of the columns of your dataset. 

<details><summary>Python Code</summary>
<p>
 
      print("Name of each column in the iris dataset:")  
      print(ds.columns)                                                       
      print("\n")
 
</p>
</details>

    
![Column data type](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/columns.PNG)

<a name="info"></a>
 <b> C. Info </b>
    
 Provides information on the iris dataset including names of columns, total number of rows and columns, data type of each column, range index and memory usage.
 
<details><summary>Python Code</summary>
<p>
 
      print("Information about iris dataset:")  
      print(ds.info())                                               
      print("\n")
 
</p>
</details>
    
![Info of Iris dataset](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/info.PNG)

<a name="unique"></a>
 <b> C. Unique Species</b>
 
 Check how many unique species of iris are in the dataset.

<details><summary>Python Code</summary>
<p>

      print("Unique species:")  
      print(ds['species'].unique())                                                
      print("\n")
 
</p>
</details>
    

![Unique Species](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/uniques-species.PNG)

<a name="isnull"></a>
<b> D. Null Values </b>

Determine if there is any null values in the dataset. This confirms there is no null values in the iris dataset. 

<details><summary>Python Code</summary>
<p>

      print("Null values present:")  
      print(ds.isnull().any())                                             
      print("\n")
 
</p>
</details>

![Presence of null values](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/isnull.PNG)

<a name="class"></a>
<b> E. Class Distribution: </b>

Class distribution - number of rows that belong to each species. This shows that data is distributed equally across the 3 species.

<details><summary>Python Code</summary>
<p>
 
      print("Class Distribution:")  
      print(ds.groupby('species').size())                                             
      print("\n")
 
</p>
</details>

![Class Distribution](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/class.PNG)

<a name="head"></a>
<b> F. Head of each species: </b>

Lists the top 4 rows for setosa species.

<details><summary>Python Code</summary>
<p>

      print("First 4 setosa values:")  
      print(setosa.head(4))                                                  
      print("\n")
 
</p>
</details>


![setosa head](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/head-setosa.PNG)

Lists the top 4 rows for versicolor species.

<details><summary>Python Code</summary>
<p>

      print("First 4 versicolor values:")  
      print(versicolor.head(4))                                                  
      print("\n")

</p>
</details>


![versicolor head](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/head-versicolor.PNG)

Lists the top 4 rows for virginica species.

<details><summary>Python Code</summary>
<p>
 
      print("First 4 virginica values:")  
      print(virginica.head(4))                                                  
      print("\n")
 
</p>
</details>

![virginica head](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/head-virginica.PNG)

<a name="tail"></a>
<b> G. Tail of each species: </b>

Lists the last 4 rows for setosa species.

<details><summary>Python Code</summary>
<p>

      print("Last 4 setosa values:")  
      print(setosa.tail(4))                                                  
      print("\n")
 
</p>
</details>

![setosa tail](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/tail-setosa.PNG)

Lists the last 4 rows for versicolor species.

<details><summary>Python Code</summary>
<p>
 
      print("Last 4 versicolor values:")  
      print(versicolor.tail(4))                                                  
      print("\n")
 
</p>
</details>

![versicolor tail](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/tail-versicolor.PNG)

Lists the last 4 rows for virginica species.

<details><summary>Python Code</summary>
<p>
 
      print("Last 4 virginica values:")  
      print(virginica.tail(4))                                                   
      print("\n")
 
</p>
</details>

![virginica tail](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/tail-virginica.PNG)

<a name="stat"></a>
## Statistics of the iris dataset:

A. Summarise the data for iris overall dataset. 

There are two ways to calculate this (both outlined below). It is clear the describe function is a much more efficient, less verbose and visually pleasing method than the alternative approach of coding the mean, median, min, max and standard deviation separately. 

<details><summary>More verbose method to summarise the iris dataset</summary>
<p>
 
      # The describe method can also be coded in another way, however this is more verbose and is not visually as pleasing:

      print ("Mean of the iris datset")                   # Title 
      print(ds.mean())                                    # Mean of the iris dataset
      print("\n")                                         # Line Break

      print ("Median of the iris datset")                 # Title 
      print(ds.median())                                  # Median of the iris dataset
      print("\n")                                         # Line Break

      print ("Minimum of the iris datset")                # Title 
      print(ds.min)                                       # Minimum of the iris dataset
      print("\n")                                         # Line Break

      print ("Max of the iris datset")                    # Title 
      print(ds.max())                                     # Max of the iris dataset
      print("\n")                                         # Line Break

      print ("Standard deviation of the iris datset")     # Title 
      print(ds.std())                                     # Standard deviation of the iris dataset
      print("\n")                                         # Line Break


</p>
</details>

<details><summary>Python Code</summary>
<p>
 
      print("Summary statistics for iris entire dataset:")  
      print(ds.describe())                                          
      print("\n")
 
</p>
</details>                                                       

![describe entire iris dataset](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/describe-all.PNG)

B. Summarise the data for iris setosa.

<details><summary>Python Code</summary>
<p>
 
      print("Summary statistics for iris setosa dataset:")  
      print(setosa.describe())                                          
      print("\n")

</p>
</details>   

![describe setosa](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/describe-setosa.PNG)

C. Summarise the data for iris versicolor.

<details><summary>Python Code</summary>
<p>

      print("Summary statistics for iris versicolor dataset:")  
      print(versicolor.describe())                                          
      print("\n")

</p>
</details> 

![describe versicolor](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/describe-versicolor.PNG)

D. Summarise the data for iris virginica.

<details><summary>Python Code</summary>
<p>

      print("Summary statistics for iris virginica dataset:")  
      print(virginica.describe())                                         
      print("\n")

</p>
</details> 

![describe virginica](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/describe-virginica.PNG)


<a name="visualize"></a>
## Visualize the dataset:

<a name="box"></a>
### Boxplots:
<p>
 
 Boxplot is a grapical representation to show the distribution of data based on the five number summary:  

<img align="right" src="https://pro.arcgis.com/en/pro-app/help/analysis/geoprocessing/charts/GUID-0E2C3730-C535-40CD-8152-80D794A996A7-web.png" width=250 title="Boxplot Attributes"> 
 
 - Median – refers to the middle value in the iris dataset
- Lower quartile (Q1) - refers to the middle number between the smallest number and the median of the dataset 
- Upper quartile (Q3)- refers to the middle number between the median and the highest value  of the dataset 
- Maximum - Q3  + 1.5*IQR
- Minimum  - Q3 – 1.5*IQR

  - Interquartile range (IQR) = Upper Quartile –Lower Quartile 


<b> Advantages: </b> [3][4]

1. Clear and easy to understand
2. Shows the presence of outliers - one of very few statistical graph methods that show outliers
3. Shows the distribution of data in a dataset
4. Easily compare the different boxplots within the iris dataset
5. Handle and present summary of large amount of data

<b> Disadvantages:</b>
1. Exact values and details of the distribution results are not shown 

<i> Boxplots are best when used in combination with another statistical graph method e.g. histogram to give a  more thorough analysis of the iris dataset. </i>
</p>

<details><summary>Python Code</summary>
<p>
   
      # Boxplot of the total iris dataset not specified for species
      
      plt.figure(figsize=(10,7))                                                                        # Resize the boxplot
      sns.boxplot(data=ds)                                                                               # Load iris datset via seaborne 
      
      # Format of boxplot 
      
      plt.title("Fisher Iris Species", fontweight="bold", fontsize="16", color="r")                      # Title of graph
      plt.ylabel("centimeters", fontweight="bold", fontsize="12", color="b")                             # Label of the y-axis
      plt.show()   

</p>
</details> 
                                                                                        
![Boxplot](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/boxplot.PNG)


<details><summary>Python Code</summary>
<p>
   
      # Boxplot to represent each of the 3 species and each of the three 
      # Adapted from https://stackoverflow.com/a/40242457

      plt.figure(figsize=(14,10))                                                             # Resize the boxplot
      ds_long = pd.melt(ds, id_vars='species')                                                # melt allows the graphs to appear together 
      sns.boxplot(x='species', y='value', hue='variable', data=ds_long)                       # ds_long refers to the format appearing as long rather than wide

      plt.title("Fisher Iris Species", fontweight="bold", fontsize="16", color="r")           # Title of graph
      plt.ylabel("centimeters", fontweight="bold", fontsize="12", color="b")                  # Label of the y-axis
      plt.xlabel("Species", fontweight="bold", fontsize="12", color="b")                      # Label of the x-axis
      plt.legend(bbox_to_anchor=(1, 1), loc=2)                                                # Legend of the data 
      plt.margins(0)                                                                          # Margin to start at zero 
      for i in range(len(ds['species'].unique())-1):                                          # Creates a division between the 3 species
          plt.vlines(i+.5, 0, 8)                                                              # plot vertical lines                 

      plt.show()                                                                              # Display the boxplot

        
</p>
</details> 

![Boxplot by Species](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/boxplot2.PNG)


<details><summary>Python Code</summary>
<p>
 
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
    
</p>
</details> 

![Boxplot by Attribute](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/boxplot3.PNG)

<a name="hist"></a>
### Histograms

<p> Histograms are a graphical representation of the distribution of the data set. A histogram displays the single quantitative variable along the x axis and frequency of that variable on the y axis. Histogram basically represents how many points exist for each value on the x-axis. Each of the species are included on the same plot which is done by overlayng the histograms by setting the transparency to 0.5 it allows us to see what is behind each of the 3 plots. Histogram basically represents how many points exist for each value on the x-axis.

</p>
<p> The distinguishing feature of a histogram is that data is grouped into "bins", which are intervals on the x-axis.  Bin involves dividing the iris dataset values into a series of intervals and then count the number of values that fall into each interval [5]. By default bin size is set to 10. It is important to pick a bin size that is suitable for your data set, the goal is to have a bin number where we can see the finer information (more bins) while not losing the bigger picture (less bins) [6]. In creating this figure I decided to use the for loop as it built on knowledge gained using for loops in the Programming and Scripting module, this required the use of sklearn. 

</p>
 
 <details><summary>Python Code</summary>
            
<p>
   
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
</p>
</details> 

  ![Histogram by Attribute](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/histogram.PNG)

<a name="dist"></a>
## Distplot:

Displot combines the function of a histogram and the KDE (density) plot into the same plot using the seaborn package. The x-axis represents a feature e.g. petal length and the y-axis is a count of the number oof points that exist in the given range. Thus, we can  determine how many points are in particular regions. For the petal length we can see that a lot of the iris setosa points lie in the range 1.5 while iris versicolor points lie in the region 4.8 [14].

<details><summary>Python Code</summary>
   
      f, axes = plt.subplots(2, 2, figsize=(12, 10), dpi=100)                                                         # Figsize and dpi(dot-per-inch)
      plt.suptitle("Fisher Iris Distribution of Data",fontweight="bold", fontsize="12", color="g" )                   # Overall heading for the graph

      plt.subplot(2,2,1)                                                                                              # Makes a top left subplot active in a 2x2 subplot layout
      sns.distplot(ds.loc[ds.species=='setosa', "sepal_length"] , color="dodgerblue", label="setosa")                 # Plot setosa species sepal length
      sns.distplot(ds.loc[ds.species=='virginica', "sepal_length"] , color="orange", label="virginica")               # Plot virginica species sepal length
      sns.distplot(ds.loc[ds.species=='versicolor', "sepal_length"] , color="deeppink", label="versicolor")           # Plot versicolor species sepal length
      plt.xlabel("Sepal Length", fontweight="bold", fontsize="12", color="b")                                         # Label of the x-axis
      plt.ylabel("Frequency", fontweight="bold", fontsize="12", color="b")                                            # Label of the y-axis
      plt.title("Iris Sepal Length Histogram", fontweight="bold", fontsize="10", color="r") 

      plt.subplot(2,2,2)                                                                                              # Makes a top right subplot active in a 2x2 subplot layout
      sns.distplot( ds.loc[ds.species=='setosa', "sepal_width"] , color="dodgerblue", label="setosa")                 # Plot setosa species sepal width
      sns.distplot( ds.loc[ds.species=='virginica', "sepal_width"] , color="orange", label="virginica")               # Plot virginica species sepal width
      sns.distplot( ds.loc[ds.species=='versicolor', "sepal_width"] , color="deeppink", label="versicolor")           # Plot versicolor species sepal width
      plt.xlabel("Sepal Width", fontweight="bold", fontsize="12", color="b")                                          # Label of the x-axis
      plt.ylabel("Frequency", fontweight="bold", fontsize="12", color="b")                                            # Label of the y-axis
      plt.title('Iris Sepal Width Histogram', fontweight="bold", fontsize="10", color="r")

      plt.subplot(2,2,3)                                                                                              # Makes a bottom left subplot active in a 2x2 subplot layout
      sns.distplot( ds.loc[ds.species=='setosa', "petal_length"] , color="dodgerblue", label="setosa")                # Plot setosa species petal length
      sns.distplot( ds.loc[ds.species=='virginica', "petal_length"] , color="orange", label="virginica")              # Plot virginica species petal length
      sns.distplot( ds.loc[ds.species=='versicolor', "petal_length"] , color="deeppink", label="versicolor")          # Plot versicolor species petal length
      plt.xlabel("Petal Length", fontweight="bold", fontsize="12", color="b")                                         # Label of the x-axis
      plt.ylabel('Frequency', fontweight="bold", fontsize="12", color="b")                                            # Label of the y-axis
      plt.title('Iris Petal Length Histogram', fontweight="bold", fontsize="10", color="r")                           # Label title of distplot


      plt.subplot(2,2,4)                                                                                             # Makes a bottom right subplot active in a 2x2 subplot layout
      sns.distplot( ds.loc[ds.species=='setosa', "petal_width"] , color="dodgerblue", label="setosa")                # Plot setosa species petal width
      sns.distplot( ds.loc[ds.species=='virginica', "petal_width"] , color="orange", label="virginica")              # Plot virginica species petal width
      sns.distplot( ds.loc[ds.species=='versicolor', "petal_width"] , color="deeppink", label="versicolor")          # Plot versicolor species petal width
      plt.xlabel("Petal Width", fontweight="bold", fontsize="12", color="b")                                         # Label of the x-axis
      plt.ylabel('Frequency', fontweight="bold", fontsize="12", color="b")                                           # Label of the y-axis
      plt.title('Iris Petal Width Histogram', fontweight="bold", fontsize="10", color="r")                           # Label title of distplot

      plt.legend(bbox_to_anchor=(1,2), loc=2)                                                                       # Legend for the overall plot
      plt.show()                                                                                                     # Display the distplot

</p>
</details> 

 
![Distplots by Attribute](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/dist.PNG)

<a name="pair"></a>
## Pairplot:
<p>
 A pairplot  can be divided into 2 parts:

Below the diagonal axis represents histogram (Image 1) or distplot (Image 2) corresponding to the feature of that row . The histogram as stated above shows the univariate  distribution of the data. While thes scatterplot demonstrate the bivariate relationship between multiple pairwise features in the Iris data set [7; 8]. 

Note I have decided to code one of the pairplots using sns.pairplot function while in the second I use sns.PairGrid which demonstrates pairplots can be coded in more than one way using seaborn. The sns.PairGrid is a class and hence requires plots to be filled in manually which explains why there are more lines required to plot essentially the same figure [10]. A regression line was added to one of the scatterplots. 

 <details><summary>Python Code</summary>
<p> 
            
      # Pairplot using distplot and scatterplot   
      sns.pairplot(ds, hue="species",  kind = "reg", markers=[".", "d", "+"],  height=2.3, aspect=1.9)                                # Each species is seperated by color and marker 
      plt.suptitle("Fisher Iris Pairplot using displot and scatterplot", fontweight="bold", fontsize="12", color="g" )                # Overall heading for the graph                                                                              
      plt.subplots_adjust(top=.9)                                                                                                     # Leave space so it does not cover the figure
      plt.show()                                                                                                                      # Display the pairplot 
      </p>
</details>

![Pairplot using sns.pairplot](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/pairplot.PNG)

 <details><summary>Python Code</summary>
<p> 
   
      # PairGrid with histogram and scatterplot

      g = sns.PairGrid(ds, hue="species", hue_kws={"marker": [".", "d", "+"]}, height=2.3, aspect=1.9)                                # Each species is seperated by color and marker 
      g.map_diag(plt.hist, histtype="step", linewidth=3, bins=20)                                                                     # Histograms are created diagonally where bins, histtep was
      g.map_offdiag(plt.scatter)                                                                                                      # Scatterplots are created in the remaining figure 
      g.add_legend()                                                                                                                  # Add legend
      g.fig.suptitle("Fisher Iris Pairplot using histogram and scatterplot", fontweight="bold", fontsize="12", color="g" )            # Overall heading for the graph  
      g.fig.subplots_adjust(top=.9)                                                                                                   # Leave space so it does not cover the figure
      plt.show()                          # Display the pairplot                                                       
</p>
</details>

![Distplots by Attribute](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/pairplot2.PNG)

<a name="scatter"></a>
### Scatterplot:

Scatter plots  is a 2D visualation of the iris dataset. Its shows the bivariate relationship between 2 variables  but does not indicate the strength of the relationship between them. Each member of the dataset gets plotted as a point whose (x, y)  coordinates relates to its values for the two variables [13]. Scatter plot shows the relationship between two variable but does not indicates the strength of relationship amongst them.


<details><summary>Python Code</summary>
<p> 
    
    # Scatterplot for petal comparasion for each species 

      sns.scatterplot(x="petal_length", y="petal_width", hue="species",style= ds.species, data=ds)                    # Plot petal length and width for each species 
      plt.xlabel("Petal Length (cm)", fontweight="bold", fontsize="12", color="b")                                    # Format of the x-axis
      plt.ylabel("Petal Width (cm)", fontweight="bold", fontsize="12", color="b")                                     # Format of the y-axis
      plt.title("Petal Comparasion for each species", fontweight="bold", fontsize="12", color="r")                    # Title of graph
      plt.show()                                                                                                      # Display the scatterplot
</p>
</details>

![Scatterplots](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/scatterplot.PNG)

 
 <details><summary>Python Code</summary>
<p>      
   
      # Scatterplot for sepal comparasion for each species 

      sns.scatterplot(x="sepal_length", y="sepal_width", hue="species",style=ds.species, data=ds)                     # Plot sepal length and width for each species 
      plt.xlabel("Sepal Length (cm)", fontweight="bold", fontsize="12", color="b")                                    # Format of the x-axis
      plt.ylabel("Sepal Width (cm)", fontweight="bold", fontsize="12", color="b")                                     # Format of the y-axis
      plt.title("Sepal Comparasion for each iris species", fontweight="bold", fontsize="12", color="r")               # Title of graph

      plt.show()    
</p>
</details> 


![Scatterplots](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/scatterplot2.PNG)



<a name="con"></a>
## Conclusion:

By completing this project based on the iris data set, it has combined the knowledge that I have gained through the Programming and Scripting module provided by GMIT while allowing me to research further ways to represent a data set. This project confirms the idea that Iris Setosa is easier to distinguish from the other 2 species. This project demonstrates how to effictively visualise a dataset using a combination of plots through python code outlined above. A good understanding of your dataset with repects its deminisions is essential prior to visualising the dataset. 

### Findings:

Statistics of the iris dataset is a great way to become familiar as it gives a numerical representation of the datatset. 

### Boxplots:

The boxplot for the overall dataset where species has not been distinguished:
The sepal length and width appear to be relatively well distributed with sepal width having outliers present. The petal width and in particular petal length have a much greater spread evidenced by the bigger box size and the location of the median. 

Boxplots seperated by species: 
Iris setosa can be separated from the other species by the petal length as it has shortest petals. One of the big advantages of boxplots is it shows the presence of outliers, it is important to know this as they can impact on the result of your mean and standard deviation.

### Histograms and Distplots:

Petal length - Iris setosa can be seperated with no visible overlap with the other iris species. Iris setosa can be distinguished as a petal length <= 2. A petal length of > 2 and < 4.7 there is a higher probability it is versicolor. However, this is not definitive as some of the virginica and versicolor points overlap.

Petal width- Iris setosa can be again be seperated from the other 2 species. The other species are overlapped once again so cannot be clearly distinguished. The better of the two so far is petal length as the distribution is further in the petal length.

Sepal length – there is no clear seperation in the species as they overlap each other. Hence sepal length is not the best variable to separate the species in distplot. 

Sepal width – similar to sepal length speration of the iris species is near impossible. In fact  virginica and versicolor are almost fully overlapped.

### Scatter plots:
Petal length and width have a linear relationship which is evident as they increase proportionally. Sepal length and width do not have a linear relationship. From the scatter plots it can clearly be seen that Iris setosa occupy the higher values for sepal length while Iris Virginica occupy the highest values for sepal width.  Iris versicolour remian in the middle values for the both sepal length and the sepal width.

Iris setosa can be easily distinguished from the other species. There is some overlap between virginica and versicolor which confirms Fisher findings. 
 

<a name="bib"></a>
 ## Bibliography:
1. Kozak, Marcin & Łotocka, Barbara. (2013). What should we know about the famous Iris data?. Current science. 104. 579-580.

2. Ronald A Fisher, The Use of Multiple Measurements in Taxonomic Problems, Annals of Eugenics 7 (1936), no. 2, 179–18
 
 3. Box and Whisker Plot | Math@TutorVista.com. 2019. Box and Whisker Plot | Math@TutorVista.com. [ONLINE] Available at: https://math.tutorvista.com/statistics/box-and-whisker-plot.html.

4. Sciencing. 2019. Advantages & Disadvantages of a Box Plot | Sciencing. [ONLINE] Available at: https://sciencing.com/advantages-disadvantages-box-plot-12025269.html.

5. Wikipedia. 2019. Histogram - Wikipedia. [ONLINE] Available at: https://en.wikipedia.org/wiki/Histogram#cite_note-2.

6. George Seif. 2019. 5 Quick and Easy Data Visualizations in Python with Code. [ONLINE] Available at: https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f.

7. ZerosnOnes. 2019. Pair Plots - ZerosnOnes. [ONLINE] Available at: http://zerosnones.net/pair-plots

8. Digital Vidya. 2019. Data Visualization In Python. [ONLINE] Available at: https://www.digitalvidya.com/blog/introduction-data-visualization-in-python/.

9. UCI Machine Learning Repository: Iris Data Set. 2019. UCI Machine Learning Repository: Iris Data Set. [ONLINE] Available at: http://archive.ics.uci.edu/ml/datasets/iris.

10. Will Koehrsen. 2019. Visualizing Data with Pairs Plots in Python – Towards Data Science. [ONLINE] Available at: https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166.

11. Anderson, Edgar. 1935. “The Irises of the Gaspe Peninsula.” Bulletin of the American Iris Society 59: 2–5.

12. Suruchi Fialoke. 2019. Classification of Iris Varieties. [ONLINE] Available at: http://suruchifialoke.com/2016-10-13-machine-learning-tutorial-iris-classification/.

13. Khan Academy. 2019. Scatterplots and correlation review (article) | Khan Academy. [ONLINE] Available at: https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/introduction-to-scatterplots/a/scatterplots-and-correlation-review.

14. Nishant Bhushan. 2019. Exploratory Data Analysis on Iris Dataset – DevMins – Medium. [ONLINE] Available at: https://medium.com/devmins/exploratory-data-analysis-on-iris-dataset-7da027acca02. 
