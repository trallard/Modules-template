---
layout: default
title: "Dimensionality reduction"
tags:
    - Day2

permalink: "dimensionality ReductionR.html"
---
# BAD DAY 2: Dimensionality reduction

# 1. PCA
(for more examples see
http://manuals.bioinformatics.ucr.edu/home/R_BioCondManual )

Principal Component Analysis (PCA) is a data reduction technique that allows to
simplify multidimensional data sets to a lower dimensional space ( tipically
using 2 or 3 dimensions) for a first broad visual analysis of the data (via
plotting and visual variance analysis).

The `prcomp( )` and `princomp( )` R functions are devoted to PCA.

The BioConductor library `pcaMethods` provides many additional PCA functions.

We are going to use the IRIS data set to demonstrate the use of PCA.

This data was used to show that these measurements could be used to
differentiate between species of irises.

This data set contains the sepal/petal length and width measurements in
centimeters for 50 flowers from each of 3 species of iris.

The Iris species are:  **setosa, versicolor, and virginica.**


<br>
<font color ='#00bcd4'> In [2]: </font>

{% highlight R %}
# Setting the working directory
bad2dir= getwd()
setwd(bad2dir)

{% endhighlight %}

<br>
<font color ='#00bcd4'> In [3]: </font>

{% highlight R %}
# Loading the data and getting a summary
data(iris)
str(iris);
summary(iris[1:4])

#dim(iris)
{% endhighlight %}


      Sepal.Length    Sepal.Width     Petal.Length    Petal.Width   
     Min.   :4.300   Min.   :2.000   Min.   :1.000   Min.   :0.100  
     1st Qu.:5.100   1st Qu.:2.800   1st Qu.:1.600   1st Qu.:0.300  
     Median :5.800   Median :3.000   Median :4.350   Median :1.300  
     Mean   :5.843   Mean   :3.057   Mean   :3.758   Mean   :1.199  
     3rd Qu.:6.400   3rd Qu.:3.300   3rd Qu.:5.100   3rd Qu.:1.800  
     Max.   :7.900   Max.   :4.400   Max.   :6.900   Max.   :2.500  


Now we will create a scatterplot of the dimensions against each other for the
three species.

<br>
<font color ='#00bcd4'> In [4]: </font>

{% highlight R %}
# Custom chosen colours
colours = c('steelblue3',  'mediumpurple', 'midnightblue')

# Plotting
pairs(iris[1:4], main = "Iris Data", pch = 19,
      col = colours[unclass(iris$Species)], labels = colnames(iris))


# adding legend
par(xpd=TRUE)
legend(x= 0.5, y = 0, levels(iris$Species), pt.bg = colours,
       pch = 21, bty = "n", ncol = 3)
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/dimensionality%20ReductionR_files/dimensionality%20ReductionR_6_0.png)


PCA is used to create linear combinations of the original data that capture as
much information in the original data as possible.
We will use the `prcomp` function.

* If we work with standardized data (mean 0 std 1) we need to calculate the
principal components through correlation matrix.

* If we work with raw data we need to calculate the principal components through
the covariance matrix.

It is good practice to standardize our variables when these have different units
and have very different variances. If they are in the same units either of the
alteratives is appropriate.

In our example all variables are measured in centimetres but we will use the
correlation matrix for simplicity’s sake.

First, we are going to examine the variability of all the numeric values

<br>
<font color ='#00bcd4'> In [5]: </font>

{% highlight R %}
sapply(iris[1:4],var)
{% endhighlight %}


<dl class="dl-horizontal">
	<dt>Sepal.Length</dt>
		<dd>0.685693512304251</dd>
	<dt>Sepal.Width</dt>
		<dd>0.189979418344519</dd>
	<dt>Petal.Length</dt>
		<dd>3.11627785234899</dd>
	<dt>Petal.Width</dt>
		<dd>0.581006263982103</dd>
</dl>



<br>
<font color ='#00bcd4'> In [6]: </font>

{% highlight R %}
range(sapply(iris[1:4],var))
{% endhighlight %}


<ol class="list-inline">
	<li>0.189979418344519</li>
	<li>3.11627785234899</li>
</ol>



Maybe this range of variability is big in this context.
Thus, we will use the correlation matrix
For this, we must standardize our variables using the  `scale()` function:

<br>
<font color ='#00bcd4'> In [7]: </font>

{% highlight R %}
iris.stand <- as.data.frame(scale(iris[,1:4]))
sapply(iris.stand,sd) #now, standard deviations are 1

#sapply(iris.stand,mean) #now, standard deviations are 1


{% endhighlight %}


<dl class="dl-horizontal">
	<dt>Sepal.Length</dt>
		<dd>1</dd>
	<dt>Sepal.Width</dt>
		<dd>1</dd>
	<dt>Petal.Length</dt>
		<dd>1</dd>
	<dt>Petal.Width</dt>
		<dd>1</dd>
</dl>



If we use the `prcomp()` function, we indicate `scale=TRUE` to use the
correlation matrix.

<br>
<font color ='#00bcd4'> In [8]: </font>

{% highlight R %}
pca <- prcomp(iris.stand, scale = T)

#similar with princomp(): princomp(iris.stand, cor=T)
pca
{% endhighlight %}


    Standard deviations:
    [1] 1.7083611 0.9560494 0.3830886 0.1439265

    Rotation:
                        PC1         PC2        PC3        PC4
    Sepal.Length  0.5210659 -0.37741762  0.7195664  0.2612863
    Sepal.Width  -0.2693474 -0.92329566 -0.2443818 -0.1235096
    Petal.Length  0.5804131 -0.02449161 -0.1421264 -0.8014492
    Petal.Width   0.5648565 -0.06694199 -0.6342727  0.5235971


<br>
<font color ='#00bcd4'> In [9]: </font>

{% highlight R %}
summary(pca)
{% endhighlight %}


    Importance of components:
                              PC1    PC2     PC3     PC4
    Standard deviation     1.7084 0.9560 0.38309 0.14393
    Proportion of Variance 0.7296 0.2285 0.03669 0.00518
    Cumulative Proportion  0.7296 0.9581 0.99482 1.00000


This gives us the standard deviation of each component, and the proportion of
variance explained by each component.
The standard deviation is stored in (see `str(pca)`):

<br>
<font color ='#00bcd4'> In [10]: </font>

{% highlight R %}
pca$sdev
{% endhighlight %}


<ol class="list-inline">
	<li>1.70836114932762</li>
	<li>0.956049408486857</li>
	<li>0.38308860015839</li>
	<li>0.143926496617611</li>
</ol>



Usually the trend is to select up to 3 components (for visualization purposes)
but we can have an indication on how many principal components should be
retained.

Usually a scree plot helps making a decision. In R we can use the `screeplot()`
function:

<br>
<font color ='#00bcd4'> In [11]: </font>

{% highlight R %}
#plot of variance of each PCA.
#It will be useful to decide how many principal components should be retained.
screeplot(pca, type = "lines", col = 'mediumpurple', lwd = 3)
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/dimensionality%20ReductionR_files/dimensionality%20ReductionR_19_0.png)


This plot together with the values of the Proportion of Variance and Cumulative
Proportion obtained by means of `summary(pca)` suggests that we can retain just
the first 2 components accounting for over 95% of the variation in the original
data!


<br>
<font color ='#00bcd4'> In [12]: </font>

{% highlight R %}
#retreive loadings for the principal components:
pca$rotation # when using princomp(): pca$loadings
{% endhighlight %}


<table class="table-responsive table-striped">
<thead><tr><th></th><th scope="col">PC1</th><th scope="col">PC2</th><th scope="col">PC3</th><th scope="col">PC4</th></tr></thead>
<tbody>
	<tr><th scope="row">Sepal.Length</th><td> 0.5210659 </td><td>-0.37741762</td><td> 0.7195664 </td><td> 0.2612863 </td></tr>
	<tr><th scope="row">Sepal.Width</th><td>-0.2693474 </td><td>-0.92329566</td><td>-0.2443818 </td><td>-0.1235096 </td></tr>
	<tr><th scope="row">Petal.Length</th><td> 0.5804131 </td><td>-0.02449161</td><td>-0.1421264 </td><td>-0.8014492 </td></tr>
	<tr><th scope="row">Petal.Width</th><td> 0.5648565 </td><td>-0.06694199</td><td>-0.6342727 </td><td> 0.5235971 </td></tr>
</tbody>
</table>



The weights of the PC1 are all similar but the one associated to Sepal.Width
variable (it is negative).
This one principal component accounts for over 72% of the variability in the
data.

All weights on the second principal component are negative. Thus the PC2 might
seem considered as an overall size measurement.  This component explain the 23%
of the variability.


The following figure show the first two components and the observations on the
same diagram, which helps to interpret the factorial axes while looking at
observations location.


The first component discriminate on one side the Sepal.Width and on the other
side the rest of variables (see biplot).
According to the second component, When the iris has larger sepal and petal
values than average, the PC2 will be smaller than average.

<br>
<font color ='#00bcd4'> In [13]: </font>

{% highlight R %}
unique(iris$Species)
as.numeric(unique(iris$Species))+1
{% endhighlight %}


<ol class="list-inline">
	<li>setosa</li>
	<li>versicolor</li>
	<li>virginica</li>
</ol>




<ol class="list-inline">
	<li>2</li>
	<li>3</li>
	<li>4</li>
</ol>



<br>
<font color ='#00bcd4'> In [14]: </font>

{% highlight R %}
# biplot of first two principal components
biplot(pca, cex = 0.8)
abline(h = 0, v = 0, lty = 2, col = 8)
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/dimensionality%20ReductionR_files/dimensionality%20ReductionR_24_0.png)


<br>
<font color ='#00bcd4'> In [15]: </font>

{% highlight R %}
plot(pca$x, col = colours, pch = 19)

legend("topright", legend = unique(iris$Species), col = colours, pch= 19)
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/dimensionality%20ReductionR_files/dimensionality%20ReductionR_25_0.png)


# 2. TSNE and comparison with PCA

The t-Distributed Stochastic Neighbor Embedding (t-SNE algorithm), by Laurens
van der Maaten and Geoffrey Hinton, is a NON LINEAR dimensionality reduction
algorithm.
It enebles to represent high-dimensional data in two or three dimensions and
allows visualization via scatter plots.

Barnes-Hut-SNE is a further improvement of the algorithm by Laurens van der
Maaten, which uses Barnes-Hut approximations to significantly improve
computational speed (O(N log N) instead of O(N2)). This makes it feasible to
apply the algorithm to larger data sets.

We will follow the example proposed oh github https://github.com/lmweber/Rtsne-
example using "Rtsne", a package by Jesse Krijthe provides an R wrapper function
for the C++ implementation of the Barnes-Hut-SNE algorithm.

The data set used in this example is the healthy human bone marrow data set
"Marrow1".

<br>
<font color ='#00bcd4'> In [16]: </font>

{% highlight R %}
# fist of all, just as an example, apply tsne on the IRIS dataset
library(Rtsne) # Load package
iris_unique <- unique(iris) # Remove duplicates
set.seed(42) # Sets seed for reproducibility
tsne_out <- Rtsne(as.matrix(iris_unique[,1:4])) # Run TSNE

plot(tsne_out$Y , col = colours, pch= 19) # Plot the result

legend("bottomright", legend = unique(iris$Species), col = colours, pch = 19)



{% endhighlight %}


    Error in library(Rtsne): there is no package called ‘Rtsne’
    Traceback:


    1. library(Rtsne)

    2. stop(txt, domain = NA)


Here we will follow  the example on GITHUB  https://github.com/lmweber/Rtsne-
example.
The Marrow1 dataset is made of cells from different cell populations (types). We
will see how tsne will be able to  group them as distinct clusters of points in
the 2-dimensional projection. There is clear visual separation between clusters.
Amir et al. (2013) also independently verified the interpretation of the
clusters using "manual gating" methods (visual inspection of 2-dimensional
scatter plots), confirming that several clusters represent well-known cell types
from immunology.

<br>
<font color ='#00bcd4'> In [17]: </font>

{% highlight R %}
#install flowCore package from Bioconductor (to read FCS files)
source("https://bioconductor.org/biocLite.R")
biocLite("flowCore")

# install Rtsne package from CRAN (R implementation of Barnes-Hut-SNE algorithm)

install.packages("Rtsne")

# load packages

library(flowCore)

{% endhighlight %}

<br>
<font color ='#00bcd4'> In [21]: </font>

{% highlight R %}
data <- exprs(read.FCS("./Rtsne-example-master/data/visne_marrow1.fcs", transformation = FALSE))
head(data)

unname(colnames(data))  # isotope and marker (protein) names

{% endhighlight %}


<table class="table-responsive table-striped">
<thead><tr><th scope="col">Event#</th><th scope="col">Time</th><th scope="col">Cell Length</th><th scope="col">191-DNA</th><th scope="col">193-DNA</th><th scope="col">115-CD45</th><th scope="col">110,111,112,114-CD3</th><th scope="col">139-CD45RA</th><th scope="col">141-pPLCgamma2</th><th scope="col">142-CD19</th><th scope="col">⋯</th><th scope="col">166-IkBalpha</th><th scope="col">167-CD38</th><th scope="col">168-pH3</th><th scope="col">170-CD90</th><th scope="col">169-pP38</th><th scope="col">171-pBtk/Itk</th><th scope="col">172-pS6</th><th scope="col">174-pSrcFK</th><th scope="col">176-pCREB</th><th scope="col">175-pCrkL</th></tr></thead>
<tbody>
	<tr><td> 22933     </td><td> 42448     </td><td>14.39525   </td><td>321.2244   </td><td> 434.9970  </td><td>142.39886  </td><td> 18.5329704</td><td>117.579620 </td><td> 4.8356605 </td><td>50.8025017 </td><td>⋯          </td><td> 2.019981  </td><td>32.1595116 </td><td>14.3242693 </td><td> 8.78977966</td><td>53.843872  </td><td>82.910294  </td><td> 6.8211913 </td><td> 5.774820  </td><td>12.3001671 </td><td> 1.4769655 </td></tr>
	<tr><td>228744     </td><td>667323     </td><td>41.27012   </td><td>209.3467   </td><td> 563.6180  </td><td> 50.66235  </td><td>  0.2076987</td><td> 19.171650 </td><td>-1.3943130 </td><td>10.0177841 </td><td>⋯          </td><td> 4.779097  </td><td>-0.5546998 </td><td> 1.5282539 </td><td>-0.26177970</td><td>17.979921  </td><td> 1.054635  </td><td> 5.0797348 </td><td> 7.080018  </td><td>-1.7290312 </td><td>-1.0569905 </td></tr>
	<tr><td>230819     </td><td>549730     </td><td>28.91957   </td><td>829.5733   </td><td>1408.7177  </td><td>503.61078  </td><td>294.2422791</td><td>  5.135233 </td><td> 0.8516778 </td><td>-0.1638297 </td><td>⋯          </td><td>12.946030  </td><td>47.7583084 </td><td>18.4628849 </td><td> 0.54432803</td><td>37.236912  </td><td>38.177971  </td><td>79.4033279 </td><td> 2.626387  </td><td>23.7090988 </td><td>-1.4266791 </td></tr>
	<tr><td>131780     </td><td>359184     </td><td>26.11232   </td><td>643.0649   </td><td> 992.3835  </td><td>178.37289  </td><td>359.2935181</td><td> 79.340591 </td><td>-0.2172089 </td><td> 5.7050629 </td><td>⋯          </td><td>24.191151  </td><td>49.7774315 </td><td> 5.1872330 </td><td>-0.07430215</td><td> 6.879214  </td><td>11.992647  </td><td>-0.2527083 </td><td> 9.006838  </td><td>-0.6766897 </td><td>-0.4470886 </td></tr>
	<tr><td> 32212     </td><td> 56694     </td><td>36.61685   </td><td>713.0907   </td><td>1131.0656  </td><td> 34.13390  </td><td>-12.1336746</td><td>  1.377896 </td><td> 3.1527698 </td><td>-0.2193382 </td><td>⋯          </td><td> 3.426270  </td><td>42.7431793 </td><td>-0.8187979 </td><td> 9.73161793</td><td>10.562280  </td><td>26.534126  </td><td>-0.7640409 </td><td>50.811363  </td><td>16.6444397 </td><td> 3.9240763 </td></tr>
	<tr><td>403958     </td><td>834589     </td><td>29.39848   </td><td>638.0286   </td><td> 968.7856  </td><td>288.91412  </td><td> 65.9604187</td><td>  6.649710 </td><td>-0.7853550 </td><td>-1.4377729 </td><td>⋯          </td><td> 1.359477  </td><td>89.9450684 </td><td>15.9464016 </td><td> 3.46092296</td><td> 4.090930  </td><td>51.456581  </td><td> 7.6963782 </td><td>28.520178  </td><td> 5.2173581 </td><td>-0.3729125 </td></tr>
</tbody>
</table>




<ol class="list-inline">
	<li>'Event#'</li>
	<li>'Time'</li>
	<li>'Cell Length'</li>
	<li>'191-DNA'</li>
	<li>'193-DNA'</li>
	<li>'115-CD45'</li>
	<li>'110,111,112,114-CD3'</li>
	<li>'139-CD45RA'</li>
	<li>'141-pPLCgamma2'</li>
	<li>'142-CD19'</li>
	<li>'144-CD11b'</li>
	<li>'145-CD4'</li>
	<li>'146-CD8'</li>
	<li>'148-CD34'</li>
	<li>'150-pSTAT5'</li>
	<li>'147-CD20'</li>
	<li>'152-Ki67'</li>
	<li>'154-pSHP2'</li>
	<li>'151-pERK1/2'</li>
	<li>'153-pMAPKAPK2'</li>
	<li>'156-pZAP70/Syk'</li>
	<li>'158-CD33'</li>
	<li>'160-CD123'</li>
	<li>'159-pSTAT3'</li>
	<li>'164-pSLP-76'</li>
	<li>'165-pNFkB'</li>
	<li>'166-IkBalpha'</li>
	<li>'167-CD38'</li>
	<li>'168-pH3'</li>
	<li>'170-CD90'</li>
	<li>'169-pP38'</li>
	<li>'171-pBtk/Itk'</li>
	<li>'172-pS6'</li>
	<li>'174-pSrcFK'</li>
	<li>'176-pCREB'</li>
	<li>'175-pCrkL'</li>
</ol>



<br>
<font color ='#00bcd4'> In [22]: </font>

{% highlight R %}
# select markers to use in calculation of t-SNE projection
# CD11b, CD123, CD19, CD20, CD3, CD33, CD34, CD38, CD4, CD45, CD45RA, CD8, CD90
# (see Amir et al. 2013, Supplementary Tables 1 and 2)

colnames_proj <- unname(colnames(data))[c(11, 23, 10, 16, 7, 22, 14, 28, 12, 6, 8, 13, 30)]
colnames_proj  # check carefully!


# arcsinh transformation
# (see Amir et al. 2013, Online Methods, "Processing of mass cytometry data")

asinh_scale <- 5
data <- asinh(data / asinh_scale)  # transforms all columns! including event number etc


# subsampling

nsub <- 10000
set.seed(123)  # set random seed
data <- data[sample(1:nrow(data), nsub), ]

dim(data)
{% endhighlight %}


<ol class="list-inline">
	<li>'144-CD11b'</li>
	<li>'160-CD123'</li>
	<li>'142-CD19'</li>
	<li>'147-CD20'</li>
	<li>'110,111,112,114-CD3'</li>
	<li>'158-CD33'</li>
	<li>'148-CD34'</li>
	<li>'167-CD38'</li>
	<li>'145-CD4'</li>
	<li>'115-CD45'</li>
	<li>'139-CD45RA'</li>
	<li>'146-CD8'</li>
	<li>'170-CD90'</li>
</ol>




<ol class="list-inline">
	<li>10000</li>
	<li>36</li>
</ol>



<br>
<font color ='#00bcd4'> In [23]: </font>

{% highlight R %}
# prepare data for Rtsne

data <- data[, colnames_proj]      # select columns to use
data <- data[!duplicated(data), ]  # remove rows containing duplicate values within rounding

dim(data)
{% endhighlight %}


<ol class="list-inline">
	<li>9902</li>
	<li>13</li>
</ol>



<br>
<font color ='#00bcd4'> In [24]: </font>

{% highlight R %}
# Exporting the subsample data in TXT format

file <- paste("./Rtsne-example-master/data/viSNE_Marrow1_nsub", nsub,".txt", sep = "")
write.table(data, file = file, row.names = FALSE, quote = FALSE, sep = "\t")



{% endhighlight %}

Running the Rtsne (Barnes-Hut_SNE algorithm) without PCA step (see Amir et al.
2013, Online Methods, "viSNE analysis")

<br>
<font color ='#00bcd4'> In [25]: </font>

{% highlight R %}
set.seed(123)  # set random seed
rtsne_out <- Rtsne(as.matrix(data), pca = FALSE, verbose = TRUE)
{% endhighlight %}


    Error in eval(expr, envir, enclos): could not find function "Rtsne"
    Traceback:



<br>
<font color ='#00bcd4'> In [26]: </font>

{% highlight R %}
# plot 2D t-SNE projection

# Uncomment the lines below if you want to save to a separate .PNG file
# file_plot <- paste("./Rtsne-example-master/plots/Rtsne_viSNE_Marrow1_nsub", nsub, ".png", sep = "")
# png(file_plot, width = 900, height = 900)

plot(rtsne_out$Y, asp =1, pch = 21, col = 'mediumpurple',
     cex = 0.75, cex.axis = 1.25, cex.lab = 1.25, cex.main = 1.5,
     xlab = "t-SNE dimension 1", ylab = "t-SNE dimension 2",
     main = "2D t-SNE projection")

# Uncomment if saving to a pgn file
#dev(off)
{% endhighlight %}


    Error in plot(rtsne_out$Y, asp = 1, pch = 21, col = "mediumpurple", cex = 0.75, : object 'rtsne_out' not found
    Traceback:


    1. plot(rtsne_out$Y, asp = 1, pch = 21, col = "mediumpurple", cex = 0.75,
     .     cex.axis = 1.25, cex.lab = 1.25, cex.main = 1.5, xlab = "t-SNE dimension 1",
     .     ylab = "t-SNE dimension 2", main = "2D t-SNE projection")


### Compare to PCA

<br>
<font color ='#00bcd4'> In [27]: </font>

{% highlight R %}
pca_data = princomp(as.matrix(data))$scores[,1:2]
plot(pca_data, col= 'steelblue3')

#text(pca_iris, labels=iris$Species,col=colors[iris$Species])
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/dimensionality%20ReductionR_files/dimensionality%20ReductionR_38_0.png)


# About the interpretation of TSNE
SOME EXAMPLES FROM
https://gist.github.com/mikelove/74bbf5c41010ae1dc94281cface90d32
on the delicate interpretation of tsne when the underlyng structure of the data
is LINEAR

Explore tsne on linear data. First install (if needed) and load the required
packages.

<br>
<font color ='#00bcd4'> In [37]: </font>

{% highlight R %}
library(rafalib)
library(RColorBrewer)
library(Rtsne)
library(tsne)
library(pracma)
{% endhighlight %}

<br>
<font color ='#00bcd4'> In [42]: </font>

{% highlight R %}
par(mfrow=c(1, 2))

for (i in 2:5) {
  set.seed(i)
  x <- runif(n, -1, 1)
  cols <- brewer.pal(11, "PuOr")[as.integer(cut(x, 11))]
  ortho <- randortho(m)
  X <- cbind(x, matrix(0,ncol=m-1,nrow=n)) %*% ortho
  res <- tsne(X)
  plot(res, col=cols, pch=20, xlab="", ylab="", main="tsne")
  res <- Rtsne(X)
  plot(res$Y, col=cols, pch=20, xlab="", ylab="", main="Rtsne")
}
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/dimensionality%20ReductionR_files/dimensionality%20ReductionR_42_1.png)



![png]({{ site.url}}{{ site.baseurl }}/notebooks/dimensionality%20ReductionR_files/dimensionality%20ReductionR_42_3.png)



![png]({{ site.url}}{{ site.baseurl }}/notebooks/dimensionality%20ReductionR_files/dimensionality%20ReductionR_42_4.png)



![png]({{ site.url}}{{ site.baseurl }}/notebooks/dimensionality%20ReductionR_files/dimensionality%20ReductionR_42_5.png)


<br>
<font color ='#00bcd4'> In [41]: </font>

{% highlight R %}
n <- 200
m <- 40
set.seed(1)

x <- runif(n, -1, 1)

bigpar(2,2,mar=c(3,3,3,1))

cols <- brewer.pal(11, "PuOr")[as.integer(cut(x, 11))]

plot(x, rep(0,n), ylim=c(-1,1), yaxt="n", xlab="", ylab="",
col=cols, pch=20, main="underlying data")

ortho <- randortho(m)

X <- cbind(x, matrix(0,ncol=m-1,nrow=n)) %*% ortho
plot(X[,1:2], asp=1, col=cols, pch=20, xlab="", ylab="", main="embed in higher dim")

res <- tsne(X)
plot(res, col=cols, pch=20, xlab="", ylab="", main="t-SNE")
bigpar(2,2,mar=c(3,3,1,1))

for (i in 2:5) {
    set.seed(i)
    x <- runif(n, -1, 1)
    cols <- brewer.pal(11, "PuOr")[as.integer(cut(x, 11))]
    ortho <- randortho(m)
    X <- cbind(x, matrix(0,ncol=m-1,nrow=n)) %*% ortho
    res <- tsne(X);
    plot(res, col=cols, pch=20, xlab="", ylab="")
}
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/dimensionality%20ReductionR_files/dimensionality%20ReductionR_43_1.png)



![png]({{ site.url}}{{ site.baseurl }}/notebooks/dimensionality%20ReductionR_files/dimensionality%20ReductionR_43_2.png)


<br>
<font color ='#00bcd4'> In [None]: </font>

{% highlight R %}

{% endhighlight %}
