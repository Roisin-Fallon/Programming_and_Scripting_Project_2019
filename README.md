# Programming_and_Scripting_Project_2019


### Table of Contents
- Libaries 
- Introduction 

 
### Libraries required:

- Numpy <a href=http://www.numpy.org/>Download here</a>

- Pandas <a href=https://pandas.pydata.org/getpandas.html>Download here</a>

- Matplotlib <a href=https://matplotlib.org/downloads.htmll>Download here</a>

- anaconda on your device (version 3.7 +) <a href=https://www.anaconda.com/distribution/>Download here</a>


### Introduction:

 <img src="http://people.wku.edu/charles.smith/chronob/ANDERSON.jpg" width="300" title="Edgar Anderson" > <img src="http://www.genetics.org/content/genetics/154/4/1419/F1.medium.gif " width="263" title="Ronald Fisher"> 
<p>
The iris dataset originated from research carried out by Edgar Anderson (American botanist) in 1935, whom collected three species of the iris flower with a goal to quantify the morphological variation.  In 1936 Ronald Fisher adapted this data published a paper “maximize the ratio of the difference between the specific means to the standard deviation within species”.  adapted Anderson data to determine if linear regression could be used/applied  
 The iris dataset originated from research carried out by Edgar Anderson (American botanist) in 1935, whom collected three species of the iris flower with a goal to quantify the morphological variation. Two of the three species were collected in the  Gaspé Peninsula ”The irises of the Gaspé Peninsula". 
 </p> 
  
<p>
Ronald Fisher adapted Anderson data to determine if linear regression could be used/applied . In 1936 Fisher published a paper “maximize the ratio of the difference between the specific means to the standard deviation within species”.  [2;1]  It is important to understand that Fisher focused on the linear discrimination analysis. The Iris flower data set or Fisher’s Iris data set is a multivariate data set introduced by Sir Ronald Fisher (1936) as an example of discriminant analysis.[1]
  </p> 
 
 ## Data Set:
 
 <img src="https://sudaniscience.files.wordpress.com/2018/10/9.png?w=720 " width="800" title="Iris flower species"> 
 
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


Image below depicts the difference between the petal and sepal.  Sepal is defined as the outermost structure of the flower, that  surround the more fragile parts of the flower .e.g. petals. Typically the petals can be  distinguished as being small and green  and the petals are colorful. However, this is not applicable to the iris flower species. Note in this image of the Iris Virginica  the sepals are larger than the petals  and are drooping, while the petals are upright.​

Based on the combination of the four numeric features, the classification of the iris flower is made.  
One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.
 
 <img src="https://www.oreilly.com/library/view/python-artificial-intelligence/9781789539462/assets/462dc4fa-fd62-4539-8599-ac80a441382c.png" width="263" title="Attributes measured"> 
     
# Dataset Summary: 

<b> A. Shape </b>

Cofirms the shape of the iris dataset in terms of the number of rows and columns. 

    print("Number of rows and columns:")  
    print(ds.shape)                                                       
    print("\n")
    
   ![Shape of Iris dataset](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/shape.PNG)
 
 <b> B. Columns </b>
    
 The names of the columns of your dataset. 
    
    print("Name of each column in the iris dataset:")  
    print(ds.columns)                                                       
    print("\n")
    
![Column data type](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/columns.PNG)

 <b> C. Info </b>
    
 Provides information on the iris dataset including names of columns, total number of rows and columns, data type of each column, range index and memory usage.
 
    print("Information about iris dataset:") 
    print(ds.info())
    print("\n")
    
![Info of Iris dataset](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/info.PNG)


 <b> C. Unique </b>
 
 Check how many unique species of iris are in the dataset.
    
    print("Unique species:")  
    print(ds['species'].unique())                                                
    print("\n")

![Unique Species](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/uniques-species.PNG)

<b> D. IsNull </b>

Determine if there is any null values in the dataset. This confirms there is no null values in the iris dataset. 

    print("Null values present:")
    print(ds.isnull().any())
    print("\n")

![Presence of null values](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/isnull.PNG)

<b> E. Class Distribution: </b>

Class distribution - number of rows that belong to each species. This shows that data is distributed equally across the 3 species.
    
    print("Class Distribution:")  
    print(ds.groupby('species').size())                                             
    print("\n")

![Class Distribution](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/class.PNG)

<b> F. Head of each species: </b>

Lists the top 4 rows for setosa species.

    print("First 4 setosa values:") 
    print(setosa.head(4))
    print("\n")
    
![setosa head](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/head-setosa.PNG)

Lists the top 4 rows for versicolor species.

    print("First 4 versicolor values:") 
    print(versicolor.head(4))
    print("\n")

![versicolor head](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/head-versicolor.PNG)

Lists the top 4 rows for virginica species.

    print("First 4 virginica values:") 
    print(virginica.head(4))
    print("\n")

![virginica head](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/head-virginica.PNG)

<b> G. Tail of each species: </b>

Lists the last 4 rows for setosa species.

    print("Last 4 setosa values:")  
    print(setosa.tail(4))
    print("\n")

![setosa tail](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/tail-setosa.PNG)

Lists the last 4 rows for versicolor species.

    print("Last 4 versicolor values:")  
    print(versicolor.tail(4))
    print("\n")

![versicolor tail](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/tail-versicolor.PNG)

Lists the last 4 rows for virginica species.

    print("Last 4 virginica values:")  
    print(virginica.tail(4))
    print("\n")

![virginica tail](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/tail-virginica.PNG)

## Statistics of the iris dataset:

I. Summarise the data for iris overall dataset. This is a more efficient method than coding median, mean, min, max, standard deviation separately.

    print("Summary statistics for iris entire dataset:")
    print(ds.describe())
    print("\n")                                                            

![describe entire iris dataset](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/describe-all.PNG)

II. Summarise the data for iris setosa.

    print("Summary statistics for iris setosa dataset:")
    summary = print(setosa.describe())
    print("\n")

![describe setosa](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/describe-setosa.PNG)

III. Summarise the data for iris versicolor.

    print("Summary statistics for iris versicolor dataset:")                                         
    print(versicolor.describe())
    print("\n")

![describe versicolor](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/describe-versicolor.PNG)

IV. Summarise the data for iris virginica.

    print("Summary statistics for iris virginica dataset:")                                          
    print(virginica.describe())
    print("\n")

![describe virginica](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/Summary%20images/describe-virginica.PNG)
 
### Visualize the dataset:

### Boxplots:
<p>
Boxplot is a grapical representation to show the distribution of data based on the five number summary: 

- Median – refers to the middle value in the iris dataset
- Lower quartile (Q1) - refers to the middle number between the smallest number and the median of the dataset 
- Upper quartile (Q3)- refers to the middle number between the median and the highest value  of the dataset 
- Maximum - Q3  + 1.5*IQR
- Minimum  - Q3 – 1.5*IQR
  - Interquartile range (IQR) – Upper Quartile –Lower Quartile 

<b> Advantages: </b> https://sciencing.com/advantages-disadvantages-box-plot-12025269.html; https://math.tutorvista.com/statistics/box-and-whisker-plot.html

1. Clear and easy to understand
2. Shows the presence of outliers - one of very few statistical graph methods that show outliers
3. Shows the distribution of data in a dataset
4. Easily compare the different boxplots within the iris dataset
5. Handle and present summary of large amount of data

<b> Disadvantages:</b>
1. Exact values and details of the distribution results are not shown 

<i> Boxplots are best when used in combination with another statistical graph method e.g. histogram to give a  more thorough analysis of the iris dataset. </i>
</p>

         plt.figure(figsize=(12,10))                                                            
         sns.boxplot(data=ds)                                                                   
         # Format of boxplot 
         plt.title("Fisher Iris Species", fontweight="bold", fontsize="16", color="r")          
         plt.ylabel("centimeters", fontweight="bold", fontsize="12", color="b")                
         plt.show()                                                                                                             

![Boxplot](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/boxplot.PNG)

        plt.figure(figsize=(14,10))                                                                               
        ds_long = pd.melt(ds, id_vars='species')                                               
        sns.boxplot(x='species', y='value', hue='variable', data=ds_long)                      

        plt.title("Fisher Iris Species", fontweight="bold", fontsize="16", color="r")          
        plt.ylabel("centimeters", fontweight="bold", fontsize="12", color="b")                 
        plt.xlabel("Species", fontweight="bold", fontsize="12", color="b")                     
        plt.legend(bbox_to_anchor=(1, 1), loc=2)                                               
        plt.margins(0)                                                                        
        for i in range(len(ds['species'].unique())-1):                                        
            plt.vlines(i+.5, 0, 8)                                                                                

        plt.show()     

![Boxplot by Species](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/boxplot2.PNG)

    plt.figure(figsize=(12,10))                                                                                
    plt.suptitle("Fisher Iris dataset grouped by species",fontweight="bold", fontsize="12", color="g" )        

    plt.subplot(2,2,1)
    plt.title("Sepal Length", fontweight="bold", fontsize="12", color="r")                                    
    plt.ylabel("Sepal Length", fontweight="bold", fontsize="10", color="b")                                    
    plt.xlabel("Species", fontweight="bold", fontsize="10", color="b")                                        
    sns.boxplot(x="species",y="sepal_length",data=ds)

    plt.subplot(2,2,2)
    plt.title("Sepal Width", fontweight="bold", fontsize="12", color="r")                                    
    plt.ylabel("Sepal Width", fontweight="bold", fontsize="10", color="b")                                    
    plt.xlabel("Species", fontweight="bold", fontsize="10", color="b")                                            
    sns.boxplot(x="species",y="sepal_width", data=ds)

    plt.subplot(2,2,3)
    plt.title("Petal Length", fontweight="bold", fontsize="12", color="r")                                    
    plt.ylabel("Petal Length", fontweight="bold", fontsize="10", color="b")                                   
    plt.xlabel("Species", fontweight="bold", fontsize="10", color="b")                                        
    sns.boxplot(x="species",y="petal_length",data=ds)

    plt.subplot(2,2,4)
    plt.title("Petal Width", fontweight="bold", fontsize="12", color="r")                                     
    plt.ylabel("Petal Width", fontweight="bold", fontsize="10", color="b")                                     
    plt.xlabel("Species", fontweight="bold", fontsize="10", color="b")                                        
    sns.boxplot(x="species",y="petal_width",data=ds)

    plt.show()    
  
![Boxplot by Attribute](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/boxplot3.PNG)

### Histograms

    f, axes = plt.subplots(2, 2, figsize=(12, 10), dpi=100)                                                         
    plt.suptitle("Fisher Iris Distribution of Data",fontweight="bold", fontsize="12", color="g" )                   

    plt.subplot(2,2,1)                                                                                              
    sns.distplot(ds.loc[ds.species=='setosa', "sepal_length"] , color="dodgerblue", label="setosa")                 
    sns.distplot(ds.loc[ds.species=='virginica', "sepal_length"] , color="orange", label="virginica")              
    sns.distplot(ds.loc[ds.species=='versicolor', "sepal_length"] , color="deeppink", label="versicolor")           
    plt.xlabel("Sepal Length", fontweight="bold", fontsize="12", color="b")                                         
    plt.ylabel("Frequency", fontweight="bold", fontsize="12", color="b")                                          
    plt.title("Iris Sepal Length Histogram", fontweight="bold", fontsize="10", color="r") 

    plt.subplot(2,2,2)                                                                                              
    sns.distplot( ds.loc[ds.species=='setosa', "sepal_width"] , color="dodgerblue", label="setosa")                  
    sns.distplot( ds.loc[ds.species=='virginica', "sepal_width"] , color="orange", label="virginica")               
    sns.distplot( ds.loc[ds.species=='versicolor', "sepal_width"] , color="deeppink", label="versicolor")           
    plt.xlabel("Sepal Width", fontweight="bold", fontsize="12", color="b")                                         
    plt.ylabel("Frequency", fontweight="bold", fontsize="12", color="b")                                           
    plt.title('Iris Sepal Width Histogram', fontweight="bold", fontsize="10", color="r")


    plt.subplot(2,2,3)                                                                                              
    sns.distplot( ds.loc[ds.species=='setosa', "petal_length"] , color="dodgerblue", label="setosa")               
    sns.distplot( ds.loc[ds.species=='virginica', "petal_length"] , color="orange", label="virginica")              
    sns.distplot( ds.loc[ds.species=='versicolor', "petal_length"] , color="deeppink", label="versicolor")          
    plt.xlabel("Petal Length", fontweight="bold", fontsize="12", color="b")                                         
    plt.ylabel('Frequency', fontweight="bold", fontsize="12", color="b")                                            
    plt.title('Iris Petal Length Histogram', fontweight="bold", fontsize="10", color="r")                           


    plt.subplot(2,2,4)                                                                                              
    sns.distplot( ds.loc[ds.species=='setosa', "petal_width"] , color="dodgerblue", label="setosa")               
    sns.distplot( ds.loc[ds.species=='virginica', "petal_width"] , color="orange", label="virginica")              
    sns.distplot( ds.loc[ds.species=='versicolor', "petal_width"] , color="deeppink", label="versicolor")          
    plt.xlabel("Petal Width", fontweight="bold", fontsize="12", color="b")                                         
    plt.ylabel('Frequency', fontweight="bold", fontsize="12", color="b")                                          
    plt.title('Iris Petal Width Histogram', fontweight="bold", fontsize="10", color="r")                           
    plt.legend(bbox_to_anchor=(1,2), loc=2)                                                                       
    plt.show()                                                                                                    

![Distplots by Attribute](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/dist.PNG)

### Scatterplots:

    plt.figure(figsize=(12,10))  
    
    # Scatterplot for petal comparasion for each species 
    
    plt.subplot(2,2,1)                                                                                              
    ax = sns.scatterplot(x="petal_length", y="petal_width", hue="species",style= ds.species, data=ds)               
    plt.xlabel("Petal Length (cm)", fontweight="bold", fontsize="12", color="b")                                    
    plt.ylabel("Petal Width (cm)", fontweight="bold", fontsize="12", color="b")                                     
    plt.title("Petal Comparasion for each species", fontweight="bold", fontsize="12", color="r")                    

    # Scatterplot for sepal comparasion for each species
    
    plt.subplot(2,2,2)                                                                                              
    ax = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species",style=ds.species, data=ds)                
    plt.xlabel("Sepal Length (cm)", fontweight="bold", fontsize="12", color="b")                                    
    plt.ylabel("Sepal Width (cm)", fontweight="bold", fontsize="12", color="b")                                     
    plt.title("Sepal Comparasion for each iris species", fontweight="bold", fontsize="12", color="r")              

    plt.show()        

![Scatterplots](https://github.com/Roisin-Fallon/Programming_and_Scripting_Project_2019/blob/master/scatterplot.PNG)
 ## Bibliography:
1. Kozak, Marcin & Łotocka, Barbara. (2013). What should we know about the famous Iris data?. Current science. 104. 579-580.

2. Ronald A Fisher, The Use of Multiple Measurements in Taxonomic Problems, Annals of Eugenics 7 (1936), no. 2, 179–18
 
