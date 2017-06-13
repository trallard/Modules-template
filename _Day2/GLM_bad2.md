---
layout: default
title: "Generalized linear models"
tags:
    - Day2

permalink: "GLM_bad2.html"
---
#  BAD DAY 2: Generalized linear models

<br>
<font color ='#00bcd4'> In [1]: </font>

{% highlight R %}
#for more examples see: http://plantecology.syr.edu/fridley/bio793/glm.html

setwd(getwd())

{% endhighlight %}

Generalized linear models (GLMs) extend the linear modeling capability of R to
scenarios that involve non-normal error distributions or heteroscedasticity.

All other classic assumptions (particularly independent observations) still
apply.  The idea here is that linear functions of the predictor variables are
obtained by a link function.  The data are then fit in this transformed scale
(using an iterative routine based on least squares), but the expected variance
is calculated on the original scale of the predictor variables.

Simple examples of link functions are $log(y)$ [which linearizes $exp(x)$],
$sqrt(y) [x^2]$, and $1/y$.  More particularly, GLMs work for the so-called
'exponential' family of error models: Poisson, binomial, Gamma, and normal.

## Count (or count-like) response variables

<br>
<font color ='#00bcd4'> In [3]: </font>

{% highlight R %}
dat = read.csv('./Data/treedata.csv') #choose the treedata.csv dataset
head(dat)
dim(dat)
dat2 = subset(dat,dat$species=="Tsuga canadensis")


{% endhighlight %}


<table class="table-responsive table-striped">
<thead><tr><th scope="col">plotID</th><th scope="col">date</th><th scope="col">plotsize</th><th scope="col">spcode</th><th scope="col">species</th><th scope="col">cover</th><th scope="col">utme</th><th scope="col">utmn</th><th scope="col">elev</th><th scope="col">tci</th><th scope="col">streamdist</th><th scope="col">disturb</th><th scope="col">beers</th></tr></thead>
<tbody>
	<tr><td>ATBN-01-0403 </td><td>08-28-2001   </td><td> 1000        </td><td>ABIEFRA      </td><td>Abies fraseri</td><td>1            </td><td>275736       </td><td>3942439      </td><td>1660         </td><td>5.701460     </td><td>490.9        </td><td>CORPLOG      </td><td>0.22442864   </td></tr>
	<tr><td>ATBN-01-0532 </td><td>07-24-2002   </td><td> 1000        </td><td>ABIEFRA      </td><td>Abies fraseri</td><td>8            </td><td>302847       </td><td>3942772      </td><td>1712         </td><td>3.823586     </td><td>454.0        </td><td>VIRGIN       </td><td>0.83408785   </td></tr>
	<tr><td>ATBN-01-0533 </td><td>07-24-2002   </td><td> 1000        </td><td>ABIEFRA      </td><td>Abies fraseri</td><td>3            </td><td>303037       </td><td>3943039      </td><td>1722         </td><td>3.893762     </td><td>453.4        </td><td>LT-SEL       </td><td>1.33325863   </td></tr>
	<tr><td>ATBN-01-0536 </td><td>07-25-2002   </td><td> 1000        </td><td>ABIEFRA      </td><td>Abies fraseri</td><td>3            </td><td>273927       </td><td>3935488      </td><td>1754         </td><td>3.145527     </td><td>492.5        </td><td>SETTLE       </td><td>1.47124839   </td></tr>
	<tr><td>ATBP-01-0001 </td><td>05-11-1999   </td><td>10000        </td><td>ABIEFRA      </td><td>Abies fraseri</td><td>8            </td><td>273857       </td><td>3937870      </td><td>1945         </td><td>5.682065     </td><td>492.4        </td><td>VIRGIN       </td><td>1.64377141   </td></tr>
	<tr><td>ATBP-01-0005 </td><td>08-25-1999   </td><td>10000        </td><td>ABIEFRA      </td><td>Abies fraseri</td><td>4            </td><td>273876       </td><td>3935462      </td><td>1751         </td><td>5.417182     </td><td>545.9        </td><td>SETTLE       </td><td>0.00032873   </td></tr>
</tbody>
</table>




<ol class="list-inline">
	<li>8971</li>
	<li>13</li>
</ol>



<br>
<font color ='#00bcd4'> In [5]: </font>

{% highlight R %}
mean(dat2$cover)
{% endhighlight %}


4.65951742627346


<br>
<font color ='#00bcd4'> In [6]: </font>

{% highlight R %}
var(dat2$cover)
{% endhighlight %}


4.471835471508


<br>
<font color ='#00bcd4'> In [7]: </font>

{% highlight R %}
table(dat2$cover)
{% endhighlight %}



      1   2   3   4   5   6   7   8   9  10
     39  71 166 110  92  80 108  60  19   1


If these counts were distributed exactly from a Poisson process, what would they
look like, assuming the same mean (and variance)?



<br>
<font color ='#00bcd4'> In [12]: </font>

{% highlight R %}
bar1 = barplot(as.vector(table(dat2$cover)),names.arg=seq(1:10), col = 'lightblue2',
              border = 'white')

points(bar1,dpois(seq(1,10),4.66)*sum(table(dat2$cover)),

     cex=1,type="b", col = 'mediumpurple', lwd = 3, pch = 19)
#?dpois

box()
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/GLM_bad2_files/GLM_bad2_9_0.png)


<br>
<font color ='#00bcd4'> In [13]: </font>

{% highlight R %}
#?glm
{% endhighlight %}

As you can see, the data look Poisson-ish but they're not perfect.  (One reason
you've probably already guessed: our data are bounded at 10, so variance should
actually go down for the highest values.)

Now let's fit a GLM to these data with just an intercept (overall mean):



<br>
<font color ='#00bcd4'> In [14]: </font>

{% highlight R %}
glm1 = glm(cover~1,data=dat2,family=poisson)

summary(glm1)
{% endhighlight %}



    Call:
    glm(formula = cover ~ 1, family = poisson, data = dat2)

    Deviance Residuals:
        Min       1Q   Median       3Q      Max  
    -2.0594  -0.8229  -0.3132   1.0085   2.1430  

    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  1.53891    0.01696   90.73   <2e-16 ***
    ---
    Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

    (Dispersion parameter for poisson family taken to be 1)

        Null deviance: 749.25  on 745  degrees of freedom
    Residual deviance: 749.25  on 745  degrees of freedom
    AIC: 3212.2

    Number of Fisher Scoring iterations: 4



Let's add a continuous predictor variable like elevation to generate a simple
Poisson regression.  First we'll graph it:


And then we'll fit the new glm and test it against a model with only an
intercept:



<br>
<font color ='#00bcd4'> In [16]: </font>

{% highlight R %}
with(dat2,plot(elev,cover,main="Hemlock cover vs. elevation",      
               cex = 1.5, col = 'midnightblue', pch = 19))
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/GLM_bad2_files/GLM_bad2_14_0.png)


<br>
<font color ='#00bcd4'> In [17]: </font>

{% highlight R %}
#Note the chi-squared test is typically recommended for models with 'known deviance' (Poisson and binomial).  Here the model with elevation adds no explanatory power (fairly obvious from the graph), but we can still add the predicted trend line to our graph:

x = seq(0,1660)
#plot.new()
#lines(predict(glm2,list(elev=x),type="response"),lwd=2,col="orange")

#What is crucial here is the type argument to predict: "response" re-calculates the coefficients to be on the same scale as the original response variable, rather than the scale of the link function.  Let's now try an ANOVA with Poisson error, using disturbance as our predictor:

glm3 = glm(cover~disturb, data = dat2, family = poisson)

summary(glm3)
anova(glm1, glm3, test = "Chisq")

{% endhighlight %}



    Call:
    glm(formula = cover ~ disturb, family = poisson, data = dat2)

    Deviance Residuals:
        Min       1Q   Median       3Q      Max  
    -2.1794  -0.7763  -0.1980   0.8523   2.2006  

    Coefficients:
                  Estimate Std. Error z value Pr(>|z|)    
    (Intercept)    1.48367    0.03838  38.661   <2e-16 ***
    disturbLT-SEL  0.03204    0.04685   0.684    0.494    
    disturbSETTLE  0.08957    0.05485   1.633    0.103    
    disturbVIRGIN  0.12184    0.05277   2.309    0.021 *  
    ---
    Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

    (Dispersion parameter for poisson family taken to be 1)

        Null deviance: 749.25  on 745  degrees of freedom
    Residual deviance: 742.32  on 742  degrees of freedom
    AIC: 3211.3

    Number of Fisher Scoring iterations: 4




<table class="table-responsive table-striped">
<thead><tr><th scope="col">Resid. Df</th><th scope="col">Resid. Dev</th><th scope="col">Df</th><th scope="col">Deviance</th><th scope="col">Pr(&gt;Chi)</th></tr></thead>
<tbody>
	<tr><td>745       </td><td>749.2497  </td><td>NA        </td><td>      NA  </td><td>        NA</td></tr>
	<tr><td>742       </td><td>742.3237  </td><td> 3        </td><td>6.926019  </td><td>0.07429355</td></tr>
</tbody>
</table>



<br>
<font color ='#00bcd4'> In [18]: </font>

{% highlight R %}
glm2 = glm(cover~elev, data = dat2, family = poisson)
summary(glm2)
anova(glm1,glm2,test="Chisq")
{% endhighlight %}



    Call:
    glm(formula = cover ~ elev, family = poisson, data = dat2)

    Deviance Residuals:
        Min       1Q   Median       3Q      Max  
    -2.0673  -0.8250  -0.3048   0.9991   2.1347  

    Coefficients:
                  Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  1.546e+00  5.135e-02  30.115   <2e-16 ***
    elev        -8.448e-06  5.471e-05  -0.154    0.877    
    ---
    Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

    (Dispersion parameter for poisson family taken to be 1)

        Null deviance: 749.25  on 745  degrees of freedom
    Residual deviance: 749.23  on 744  degrees of freedom
    AIC: 3214.2

    Number of Fisher Scoring iterations: 4




<table class="table-responsive table-striped">
<thead><tr><th scope="col">Resid. Df</th><th scope="col">Resid. Dev</th><th scope="col">Df</th><th scope="col">Deviance</th><th scope="col">Pr(&gt;Chi)</th></tr></thead>
<tbody>
	<tr><td>745       </td><td>749.2497  </td><td>NA        </td><td>        NA</td><td>       NA </td></tr>
	<tr><td>744       </td><td>749.2259  </td><td> 1        </td><td>0.02384893</td><td>0.8772699 </td></tr>
</tbody>
</table>



<br>
<font color ='#00bcd4'> In [19]: </font>

{% highlight R %}
glm4 = glm(cover~disturb*elev,data=dat2,family=poisson)

summary(glm4)
{% endhighlight %}



    Call:
    glm(formula = cover ~ disturb * elev, family = poisson, data = dat2)

    Deviance Residuals:
        Min       1Q   Median       3Q      Max  
    -2.4042  -0.7782  -0.2072   0.8090   2.0888  

    Coefficients:
                         Estimate Std. Error z value Pr(>|z|)    
    (Intercept)         1.445e+00  1.396e-01  10.352   <2e-16 ***
    disturbLT-SEL       2.546e-01  1.639e-01   1.554   0.1203    
    disturbSETTLE      -3.702e-01  2.275e-01  -1.628   0.1036    
    disturbVIRGIN       9.283e-02  2.625e-01   0.354   0.7236    
    elev                3.540e-05  1.243e-04   0.285   0.7758    
    disturbLT-SEL:elev -2.788e-04  1.651e-04  -1.689   0.0912 .  
    disturbSETTLE:elev  7.319e-04  2.943e-04   2.487   0.0129 *  
    disturbVIRGIN:elev  2.278e-05  2.269e-04   0.100   0.9200    
    ---
    Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

    (Dispersion parameter for poisson family taken to be 1)

        Null deviance: 749.25  on 745  degrees of freedom
    Residual deviance: 729.06  on 738  degrees of freedom
    AIC: 3206

    Number of Fisher Scoring iterations: 4



<br>
<font color ='#00bcd4'> In [20]: </font>

{% highlight R %}
step(glm4)
{% endhighlight %}



    Call:  glm(formula = cover ~ disturb * elev, family = poisson, data = dat2)

    Coefficients:
           (Intercept)       disturbLT-SEL       disturbSETTLE       disturbVIRGIN  
             1.445e+00           2.546e-01          -3.702e-01           9.283e-02  
                  elev  disturbLT-SEL:elev  disturbSETTLE:elev  disturbVIRGIN:elev  
             3.540e-05          -2.788e-04           7.319e-04           2.278e-05  

    Degrees of Freedom: 745 Total (i.e. Null);  738 Residual
    Null Deviance:	    749.2
    Residual Deviance: 729.1 	AIC: 3206


The ANOVA contrasts suggest a significant difference in slope with elevation in
the plots of prior settlement:
disturbSETTLE:elev  0.0129 *;
the step function shows that the interaction is necessary (large increase in AIC
when the interaction is removed).

<br>
<font color ='#00bcd4'> In [1]: </font>

{% highlight R %}
#?step


{% endhighlight %}

<br>
<font color ='#00bcd4'> In [2]: </font>

{% highlight R %}
#st=step(glm4)
{% endhighlight %}

<br>
<font color ='#00bcd4'> In [3]: </font>

{% highlight R %}
#st$anova
{% endhighlight %}
