---
layout: default
title: "Ttest"
tags:
    - Day1

permalink: "Ttest.html"
---
# BAD Day 1 : T-test



## 1. Loading the data set

<br>
<font color ='#00bcd4'> In [1]: </font>

{% highlight R %}
require(multtest)
data(golub)
{% endhighlight %}

We will be usig the Gene Expression dataset from Golub et al (1999).

Gene expression data (3051 genes and 38 tumor mRNA samples) from the leukemia
microarray study of Golub et al. (1999). Pre-processing was done as described in
Dudoit et al. (2002). The R code for pre-processing is available in the file
../doc/golub.R.
Source: Golub et al. (1999). Molecular classification of cancer: class discovery
and class prediction by gene expression monitoring, Science, Vol. 286:531-537.
http://www-genome.wi.mit.edu/MPR/ .

<br>
<font color ='#00bcd4'> In [2]: </font>

{% highlight R %}
golub.expr <- golub

# preliminar view of the data
head(golub.expr)
{% endhighlight %}


<table class="table-responsive table-striped">
<tbody>
	<tr><td>-1.45769</td><td>-1.39420</td><td>-1.42779</td><td>-1.40715</td><td>-1.42668</td><td>-1.21719</td><td>-1.37386</td><td>-1.36832</td><td>-1.47649</td><td>-1.21583</td><td>⋯       </td><td>-1.08902</td><td>-1.29865</td><td>-1.26183</td><td>-1.44434</td><td> 1.10147</td><td>-1.34158</td><td>-1.22961</td><td>-0.75919</td><td>0.84905 </td><td>-0.66465</td></tr>
	<tr><td>-0.75161</td><td>-1.26278</td><td>-0.09052</td><td>-0.99596</td><td>-1.24245</td><td>-0.69242</td><td>-1.37386</td><td>-0.50803</td><td>-1.04533</td><td>-0.81257</td><td>⋯       </td><td>-1.08902</td><td>-1.05094</td><td>-1.26183</td><td>-1.25918</td><td> 0.97813</td><td>-0.79357</td><td>-1.22961</td><td>-0.71792</td><td>0.45127 </td><td>-0.45804</td></tr>
	<tr><td> 0.45695</td><td>-0.09654</td><td> 0.90325</td><td>-0.07194</td><td> 0.03232</td><td> 0.09713</td><td>-0.11978</td><td> 0.23381</td><td> 0.23987</td><td> 0.44201</td><td>⋯       </td><td>-0.43377</td><td>-0.10823</td><td>-0.29385</td><td> 0.05067</td><td> 1.69430</td><td>-0.12472</td><td> 0.04609</td><td> 0.24347</td><td>0.90774 </td><td> 0.46509</td></tr>
	<tr><td> 3.13533</td><td> 0.21415</td><td> 2.08754</td><td> 2.23467</td><td> 0.93811</td><td> 2.24089</td><td> 3.36576</td><td> 1.97859</td><td> 2.66468</td><td>-1.21583</td><td>⋯       </td><td> 0.29598</td><td>-1.29865</td><td> 2.76869</td><td> 2.08960</td><td> 0.70003</td><td> 0.13854</td><td> 1.75908</td><td> 0.06151</td><td>1.30297 </td><td> 0.58186</td></tr>
	<tr><td> 2.76569</td><td>-1.27045</td><td> 1.60433</td><td> 1.53182</td><td> 1.63728</td><td> 1.85697</td><td> 3.01847</td><td> 1.12853</td><td> 2.17016</td><td>-1.21583</td><td>⋯       </td><td>-1.08902</td><td>-1.29865</td><td> 2.00518</td><td> 1.17454</td><td>-1.47218</td><td>-1.34158</td><td> 1.55086</td><td>-1.18107</td><td>1.01596 </td><td> 0.15788</td></tr>
	<tr><td> 2.64342</td><td> 1.01416</td><td> 1.70477</td><td> 1.63845</td><td>-0.36075</td><td> 1.73451</td><td> 3.36576</td><td> 0.96870</td><td> 2.72368</td><td>-1.21583</td><td>⋯       </td><td>-1.08902</td><td>-1.29865</td><td> 1.73780</td><td> 0.89347</td><td>-0.52883</td><td>-1.22168</td><td> 0.90832</td><td>-1.39906</td><td>0.51266 </td><td> 1.36249</td></tr>
</tbody>
</table>



 `golub.names` is a matrix containing the names of the 3051
 genes contained in `golub`. The three columns correspond to:
`index, ID and name`

<br>
<font color ='#00bcd4'> In [3]: </font>

{% highlight R %}
row.names(golub.expr) = golub.gnames[,3]
{% endhighlight %}

`golub.cl` is a numeric vector indicating the tumor class, 27 acute
lymphoblastic leukemia (ALL) cases (code 0) and 11 acute myeloid leukemia (AML)
cases (code 1).

<br>
<font color ='#00bcd4'> In [4]: </font>

{% highlight R %}
colnames(golub.expr) = golub.cl
{% endhighlight %}

Now we need to set the sample sizes

<br>
<font color ='#00bcd4'> In [5]: </font>

{% highlight R %}
n.ALL <- 27
n.AML <- 11

cancer.type <- c(rep('ALL', n.ALL), rep('AML', n.AML))
{% endhighlight %}

Adding the cancer type to the column name, for the display

<br>
<font color ='#00bcd4'> In [6]: </font>

{% highlight R %}
colnames(golub.expr) <- cancer.type
{% endhighlight %}

<br>
<font color ='#00bcd4'> In [7]: </font>

{% highlight R %}
head(golub.expr)
{% endhighlight %}


<table class="table-responsive table-striped">
<thead><tr><th></th><th scope="col">ALL</th><th scope="col">ALL</th><th scope="col">ALL</th><th scope="col">ALL</th><th scope="col">ALL</th><th scope="col">ALL</th><th scope="col">ALL</th><th scope="col">ALL</th><th scope="col">ALL</th><th scope="col">ALL</th><th scope="col">⋯</th><th scope="col">AML</th><th scope="col">AML</th><th scope="col">AML</th><th scope="col">AML</th><th scope="col">AML</th><th scope="col">AML</th><th scope="col">AML</th><th scope="col">AML</th><th scope="col">AML</th><th scope="col">AML</th></tr></thead>
<tbody>
	<tr><th scope="row">AFFX-HUMISGF3A/M97935_MA_at</th><td>-1.45769</td><td>-1.39420</td><td>-1.42779</td><td>-1.40715</td><td>-1.42668</td><td>-1.21719</td><td>-1.37386</td><td>-1.36832</td><td>-1.47649</td><td>-1.21583</td><td>⋯       </td><td>-1.08902</td><td>-1.29865</td><td>-1.26183</td><td>-1.44434</td><td> 1.10147</td><td>-1.34158</td><td>-1.22961</td><td>-0.75919</td><td>0.84905 </td><td>-0.66465</td></tr>
	<tr><th scope="row">AFFX-HUMISGF3A/M97935_MB_at</th><td>-0.75161</td><td>-1.26278</td><td>-0.09052</td><td>-0.99596</td><td>-1.24245</td><td>-0.69242</td><td>-1.37386</td><td>-0.50803</td><td>-1.04533</td><td>-0.81257</td><td>⋯       </td><td>-1.08902</td><td>-1.05094</td><td>-1.26183</td><td>-1.25918</td><td> 0.97813</td><td>-0.79357</td><td>-1.22961</td><td>-0.71792</td><td>0.45127 </td><td>-0.45804</td></tr>
	<tr><th scope="row">AFFX-HUMISGF3A/M97935_3_at</th><td> 0.45695</td><td>-0.09654</td><td> 0.90325</td><td>-0.07194</td><td> 0.03232</td><td> 0.09713</td><td>-0.11978</td><td> 0.23381</td><td> 0.23987</td><td> 0.44201</td><td>⋯       </td><td>-0.43377</td><td>-0.10823</td><td>-0.29385</td><td> 0.05067</td><td> 1.69430</td><td>-0.12472</td><td> 0.04609</td><td> 0.24347</td><td>0.90774 </td><td> 0.46509</td></tr>
	<tr><th scope="row">AFFX-HUMRGE/M10098_5_at</th><td> 3.13533</td><td> 0.21415</td><td> 2.08754</td><td> 2.23467</td><td> 0.93811</td><td> 2.24089</td><td> 3.36576</td><td> 1.97859</td><td> 2.66468</td><td>-1.21583</td><td>⋯       </td><td> 0.29598</td><td>-1.29865</td><td> 2.76869</td><td> 2.08960</td><td> 0.70003</td><td> 0.13854</td><td> 1.75908</td><td> 0.06151</td><td>1.30297 </td><td> 0.58186</td></tr>
	<tr><th scope="row">AFFX-HUMRGE/M10098_M_at</th><td> 2.76569</td><td>-1.27045</td><td> 1.60433</td><td> 1.53182</td><td> 1.63728</td><td> 1.85697</td><td> 3.01847</td><td> 1.12853</td><td> 2.17016</td><td>-1.21583</td><td>⋯       </td><td>-1.08902</td><td>-1.29865</td><td> 2.00518</td><td> 1.17454</td><td>-1.47218</td><td>-1.34158</td><td> 1.55086</td><td>-1.18107</td><td>1.01596 </td><td> 0.15788</td></tr>
	<tr><th scope="row">AFFX-HUMRGE/M10098_3_at</th><td> 2.64342</td><td> 1.01416</td><td> 1.70477</td><td> 1.63845</td><td>-0.36075</td><td> 1.73451</td><td> 3.36576</td><td> 0.96870</td><td> 2.72368</td><td>-1.21583</td><td>⋯       </td><td>-1.08902</td><td>-1.29865</td><td> 1.73780</td><td> 0.89347</td><td>-0.52883</td><td>-1.22168</td><td> 0.90832</td><td>-1.39906</td><td>0.51266 </td><td> 1.36249</td></tr>
</tbody>
</table>



## 2. t.test with a single gene (step-by-step)

We will select the gene 347 for this example

<br>
<font color ='#00bcd4'> In [8]: </font>

{% highlight R %}
g <- 347
{% endhighlight %}

Alternatively, you can select a gene randomly

<br>
<font color ='#00bcd4'> In [9]: </font>

{% highlight R %}
# g <- sample(1:nrow(golub.expr),1)
g.profile <- as.vector(as.matrix(golub.expr[g,]))
{% endhighlight %}

Draw a barplot with color-coded cancer type

<br>
<font color ='#00bcd4'> In [10]: </font>

{% highlight R %}
plot.col <- c('ALL'='midnightblue', 'AML'='mediumpurple')

barplot(g.profile, main=paste("Golub (1999), gene", g),
        col=plot.col[cancer.type])
legend('topright', c("ALL","AML"),col=plot.col[c("ALL","AML")],
       pch=15, bty="o", bg='white')
box()
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/Ttest_files/Ttest_20_0.png)


Separating the data in two vectors

<br>
<font color ='#00bcd4'> In [11]: </font>

{% highlight R %}
sample.ALL <- g.profile[cancer.type=="ALL"]
sample.AML <- g.profile[cancer.type=="AML"]
{% endhighlight %}

**Compute manually ** the t test parameters (not necessary, just to practice!)

Estimate the population means

<br>
<font color ='#00bcd4'> In [12]: </font>

{% highlight R %}
mean.est.ALL <- mean(sample.ALL)
mean.est.AML <- mean(sample.AML)
{% endhighlight %}

Compute the sample standard deviations
The sd() function automatically computes the estimate corrected with sqrt(n-1)

<br>
<font color ='#00bcd4'> In [13]: </font>

{% highlight R %}
sample.sd.ALL <- sd(sample.ALL) * sqrt((n.ALL-1)/n.ALL)
sample.sd.AML <- sd(sample.AML) * sqrt((n.AML-1)/n.AML)
{% endhighlight %}

Estimate the population standard deviation


<br>
<font color ='#00bcd4'> In [14]: </font>

{% highlight R %}
sd.est.ALL <- sd(sample.ALL)
sd.est.AML <- sd(sample.AML)
{% endhighlight %}

Estimate the standard deviations on the means

<br>
<font color ='#00bcd4'> In [15]: </font>

{% highlight R %}
sd.err.est.ALL <- sd(sample.ALL) / sqrt(n.ALL)
sd.err.est.AML <- sd(sample.AML) / sqrt(n.AML)
{% endhighlight %}

Estimate the standard deviation of the difference between two means, according
to Student's formula

<br>
<font color ='#00bcd4'> In [16]: </font>

{% highlight R %}
diff.sd.est <- sqrt((n.ALL*sample.sd.ALL^2 + n.AML*sample.sd.AML^2) * (1/n.ALL + 1/n.AML) /(n.ALL+n.AML-2))
{% endhighlight %}

Compute t.obs

<br>
<font color ='#00bcd4'> In [17]: </font>

{% highlight R %}
d <- abs(mean.est.ALL - mean.est.AML)
t.obs.Student <- d / diff.sd.est
{% endhighlight %}

Compute the P- vale.
Since we are performing the two-tail test, the single-tail probability has to be
multiplied by 3 in order to obtai the alpha risk

<br>
<font color ='#00bcd4'> In [18]: </font>

{% highlight R %}
P.val.Student <- 2 * pt(q = t.obs.Student, df = n.ALL + n.AML-2, lower.tail = F)
{% endhighlight %}

## 3. T-test the fast way

 **This is what you should be doing... **

 Suppose that the gene expression data from two groups of patients
(experimental) are availaeble and that the that the hypothesis is about the
difference
between the population means $\mu_1$ and $\mu_2$.

Thus $H_0: \mu_1 = \mu_2$ is to be tested against  $H_0: \mu_1 \neq \mu_2$. If
the gene expression data are $\left( x_1...x_n \right)$ and
$\left(y_1...y_n\right)$ for the first and second group, respectively.

With the mean and variances of the first and the second groups being $\bar{x}$,
$\bar{y}$ , $s_1^2$,$s_2^2$.

Then the t-statistic can be formulated as:

$$ t =
\frac{(\bar{x}-\bar{y})-(\mu_1-\mu_2)}{\sqrt{\frac{s_1^2}{n}+\frac{s_2^2}{m}}}$$


**Note**: the t-value is large if the difference between $\bar{x}$ and $\bar{y}$
is large and the standard deviations $s_1$ and $s_2$ are small. This corresponds
to the **Welch two-sample t-test**.

### 3.2 Two-samples t-test with unequal variances (Welch t-test)


Golub et al. (1999) argue that gene CCND3 Cyclin D3 plays
an important role with respect to discriminating ALL from AML patients. We
previously generated the boxplots for this gene, which suggests that the  `ALL`
population means differs from that of the `AML`. The null hypothesis of equal
means can be tested by using the appropriate factor and specification `var.equal
= FALSE`.

<br>
<font color ='#00bcd4'> In [22]: </font>

{% highlight R %}
#t.test(sample.ALL,sample.AML, var.equal=FALSE)

# creating the gol.fac
gol.fac <-  factor(golub.cl, levels = 0:1, labels = c("AML", "ALL"))
t.test(golub[1042, ] ~ gol.fac, var.equal = FALSE)
{% endhighlight %}



    	Welch Two Sample t-test

    data:  golub[1042, ] by gol.fac
    t = 6.3186, df = 16.118, p-value = 9.871e-06
    alternative hypothesis: true difference in means is not equal to 0
    95 percent confidence interval:
     0.8363826 1.6802008
    sample estimates:
    mean in group AML mean in group ALL
            1.8938826         0.6355909



The *t* value is significantly large, meaning that the two means differ largely
with respect to the corresponding (standard error). As the *p* value is very
small,the conclusion is to reject the
null-hypothesis of equal means. The data provide strong evidence that the
population means do differ.

### 3.1 Two-samples Student-Fischer t-test (samples with equal variances).

Suppose the same setup as in the above example. In this case, however, the
variances $\sigma_1^2$ and $\sigma_2^2$ for the two groups are known to be
equal. To test $H_0: \mu_1 = \mu_2$ against $H_1: \mu_1 \neq \mu_2$ there is a
t-test which is based on the pooled sample variance $s_p^2$. The latter is
defined by the weighted sum of the sample variances $s_1^2$ and $s_2^2$ e.g.

$$ s_p^2 = \frac{(n-1)s_1^2+(m-1)s_2^2}{n+m-2}$$


Then the t-value will be

$$t = \frac{\bar{x}-\bar{y}-(\mu_1-\mu_2)}{s_p \sqrt{\frac{1}{n}+\frac{1}{m}}}
$$

The null hypothesis for gene CCND3 Cyclin D3 that the mean of ALL differs from
that of AML patients can be tested by the two-sample t-test using:

<br>
<font color ='#00bcd4'> In [23]: </font>

{% highlight R %}
#t.test(sample.ALL,sample.AML, var.equal=TRUE)


t.test(golub[1042, ] ~ gol.fac, var.equal = TRUE)
{% endhighlight %}



    	Two Sample t-test

    data:  golub[1042, ] by gol.fac
    t = 6.7983, df = 36, p-value = 6.046e-08
    alternative hypothesis: true difference in means is not equal to 0
    95 percent confidence interval:
     0.8829143 1.6336690
    sample estimates:
    mean in group AML mean in group ALL
            1.8938826         0.6355909



From the p-value $6.046 \times 10^{-8}$, the conclusion is to reject the null
hypothesis
of equal population means. Note that the p-value is slightly smaller than
that of the previous test.

<br>
<font color ='#00bcd4'> In [None]: </font>

{% highlight R %}

{% endhighlight %}
