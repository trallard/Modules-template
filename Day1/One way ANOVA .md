---
layout: default
title: "One way ANOVA "
tags:
    - Day1
permalink: "One way ANOVA .html"
---
#  BAD Day 1: One way ANOVA


This notebook is intended to demonstrate the application of the one way ANOVA
analysis on a built in R data set: **PlantGrowth**

<br>
<font color ='#00bcd4'> In [1]: </font>

{% highlight R %}
# Getting the data set and having a peek into its content
help(PlantGrowth)
PlantGrowth
{% endhighlight %}


<table class="table-responsive table-striped">
<thead><tr><th scope="col">weight</th><th scope="col">group</th></tr></thead>
<tbody>
	<tr><td>4.17</td><td>ctrl</td></tr>
	<tr><td>5.58</td><td>ctrl</td></tr>
	<tr><td>5.18</td><td>ctrl</td></tr>
	<tr><td>6.11</td><td>ctrl</td></tr>
	<tr><td>4.50</td><td>ctrl</td></tr>
	<tr><td>4.61</td><td>ctrl</td></tr>
	<tr><td>5.17</td><td>ctrl</td></tr>
	<tr><td>4.53</td><td>ctrl</td></tr>
	<tr><td>5.33</td><td>ctrl</td></tr>
	<tr><td>5.14</td><td>ctrl</td></tr>
	<tr><td>4.81</td><td>trt1</td></tr>
	<tr><td>4.17</td><td>trt1</td></tr>
	<tr><td>4.41</td><td>trt1</td></tr>
	<tr><td>3.59</td><td>trt1</td></tr>
	<tr><td>5.87</td><td>trt1</td></tr>
	<tr><td>3.83</td><td>trt1</td></tr>
	<tr><td>6.03</td><td>trt1</td></tr>
	<tr><td>4.89</td><td>trt1</td></tr>
	<tr><td>4.32</td><td>trt1</td></tr>
	<tr><td>4.69</td><td>trt1</td></tr>
	<tr><td>6.31</td><td>trt2</td></tr>
	<tr><td>5.12</td><td>trt2</td></tr>
	<tr><td>5.54</td><td>trt2</td></tr>
	<tr><td>5.50</td><td>trt2</td></tr>
	<tr><td>5.37</td><td>trt2</td></tr>
	<tr><td>5.29</td><td>trt2</td></tr>
	<tr><td>4.92</td><td>trt2</td></tr>
	<tr><td>6.15</td><td>trt2</td></tr>
	<tr><td>5.80</td><td>trt2</td></tr>
	<tr><td>5.26</td><td>trt2</td></tr>
</tbody>
</table>



We will now use the `summary` functon to get more information about the whole
data set

<br>
<font color ='#00bcd4'> In [2]: </font>

{% highlight R %}
# Getting a basic summary of the data
summary(PlantGrowth)
{% endhighlight %}


         weight       group   
     Min.   :3.590   ctrl:10  
     1st Qu.:4.550   trt1:10  
     Median :5.155   trt2:10  
     Mean   :5.073            
     3rd Qu.:5.530            
     Max.   :6.310            


You can also get statistical information on a single attribute of the data

<br>
<font color ='#00bcd4'> In [3]: </font>

{% highlight R %}
# Computing the SD of a given attribute
sd(PlantGrowth$weight)
{% endhighlight %}


0.701191842508168


Or per groups within the data set

<br>
<font color ='#00bcd4'> In [4]: </font>

{% highlight R %}
# Compute the sd of each group for the given attribute
tapply(PlantGrowth$weight, PlantGrowth$group, sd)
{% endhighlight %}


<dl class="dl-horizontal">
	<dt>ctrl</dt>
		<dd>0.583091378392406</dd>
	<dt>trt1</dt>
		<dd>0.793675696434703</dd>
	<dt>trt2</dt>
		<dd>0.442573283322786</dd>
</dl>



The next thing we will do is creating a boxplot of the data set (as in the main
Tutorial).

<br>
<font color ='#00bcd4'> In [9]: </font>

{% highlight R %}
boxplot(weight ~ group, data =  PlantGrowth, col = 'mediumpurple',
        xlab = 'Group', ylab = 'Weight')
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/One%20way%20ANOVA%20_files/One%20way%20ANOVA%20_10_0.png)


We can also create histograms of the data. In this case we will use the lattice
plotting system:

<br>
<font color ='#00bcd4'> In [10]: </font>

{% highlight R %}
# Creating a conditional histogram of the data
par(mfrow =  c(1,3))

# We will use the lattice plotting system
library(lattice)

# Creating the histogram
histogram(~weight | group, data =  PlantGrowth, col = 'mediumpurple', type = 'count')
{% endhighlight %}




![png]({{ site.url}}{{ site.baseurl }}/notebooks/One%20way%20ANOVA%20_files/One%20way%20ANOVA%20_12_1.png)


## Our  null hypotesis is that the three groups have the same growth mean

First we will use a completely randomized design one-way ANOVA

<br>
<font color ='#00bcd4'> In [14]: </font>

{% highlight R %}
# One way ANOVA (Randomized design)
analysis <- aov(weight ~ group, data = PlantGrowth)
summary(analysis)
{% endhighlight %}


                Df Sum Sq Mean Sq F value Pr(>F)  
    group        2  3.766  1.8832   4.846 0.0159 *
    Residuals   27 10.492  0.3886                 
    ---
    Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1


Now we will build a linear model with `lm()` and will then use the `anova()`
command to analyse the fit

<br>
<font color ='#00bcd4'> In [12]: </font>

{% highlight R %}
fit <- lm(weight ~ group, data = PlantGrowth)
anova(fit)
{% endhighlight %}


<table class="table-responsive table-striped">
<thead><tr><th></th><th scope="col">Df</th><th scope="col">Sum Sq</th><th scope="col">Mean Sq</th><th scope="col">F value</th><th scope="col">Pr(&gt;F)</th></tr></thead>
<tbody>
	<tr><th scope="row">group</th><td> 2        </td><td> 3.76634  </td><td>1.8831700 </td><td>4.846088  </td><td>0.01590996</td></tr>
	<tr><th scope="row">Residuals</th><td>27        </td><td>10.49209  </td><td>0.3885959 </td><td>      NA  </td><td>        NA</td></tr>
</tbody>
</table>



As expected, both approaches provide the same results!
