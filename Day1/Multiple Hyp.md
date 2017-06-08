---
layout: default
title: "Multiple Hypothesis testing"
tags:
    - Day1

permalink: "Multiple Hyp.html"
---
# BAD Day 1: Multiple hypothesis testing on Golub

In this tutorial we will do multiple hypothesis testing on the previsouly
studied `Golub` data set.

-  **Null Hypothesis** $H_0$ states the assumption to be tested. We begin by
assuming that the null Hypothesis is True
-  **Alternative Hypothesis** $H_1$ is the opposite of the null hypothesis

## 1. Loading the dataset

<br>
<font color ='#00bcd4'> In [1]: </font>

{% highlight R %}
require(multtest)
data(golub)
{% endhighlight %}

Gene expression data (3051 genes and 38 tumor mRNA samples) from the leukemia
microarray study of Golub et al. (1999). Pre-processing was done as described in
Dudoit et al. (2002). The R code for pre-processing is available in the file
../doc/golub.R.

<br>
<font color ='#00bcd4'> In [2]: </font>

{% highlight R %}
golub.expr<-golub
row.names(golub.expr)=golub.gnames[,3]
{% endhighlight %}

Numeric vector indicating the tumor class, 27 acute lymphoblastic leukemia (ALL)
cases (code 0) and 11 acute myeloid leukemia (AML) cases (code 1).

<br>
<font color ='#00bcd4'> In [3]: </font>

{% highlight R %}
colnames(golub.expr)= golub.cl
{% endhighlight %}

Setting the sample sizes

<br>
<font color ='#00bcd4'> In [4]: </font>

{% highlight R %}
n.ALL <- 27
n.AML <- 11
cancer.type <- c(rep("ALL", n.ALL), rep("AML", n.AML))
{% endhighlight %}

Adding the cancer type to the column name, for the display

<br>
<font color ='#00bcd4'> In [5]: </font>

{% highlight R %}
colnames(golub.expr) <-cancer.type
{% endhighlight %}

## 2. t.test with a single gene

<br>
<font color ='#00bcd4'> In [6]: </font>

{% highlight R %}
g <- 347
{% endhighlight %}

Alternatively, you can select a gene randomly

<br>
<font color ='#00bcd4'> In [7]: </font>

{% highlight R %}
## g <- sample(1:nrow(golub.expr),1)
g.profile <- as.vector(as.matrix(golub.expr[g,]))
{% endhighlight %}

Draw a barplot wiht color-coded cancer type

<br>
<font color ='#00bcd4'> In [9]: </font>

{% highlight R %}
plot.col <- c('ALL'='mediumpurple', 'AML'='midnightblue')

barplot(g.profile, main = paste("Golub (1999), gene", g),
        col = plot.col[cancer.type], border = 'white')

legend('topright', c("ALL","AML"),col = plot.col[c("ALL","AML")],
       pch = 15, bty = "o")
box()
{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/Multiple%20Hyp_files/Multiple%20Hyp_16_0.png)


Separate data in two vectors

<br>
<font color ='#00bcd4'> In [10]: </font>

{% highlight R %}
sample.ALL <- g.profile[cancer.type=="ALL"]
sample.AML <- g.profile[cancer.type=="AML"]
{% endhighlight %}

Compute **manually** the t test paramenters (not necessary, just to practice!)

Estimate the population means

<br>
<font color ='#00bcd4'> In [11]: </font>

{% highlight R %}
mean.est.ALL <- mean(sample.ALL)
mean.est.AML <- mean(sample.AML)
{% endhighlight %}

Compute the sample sd

Remember the `sd( )` function automatically computes the estimate corrected with
sqrt(n-1)

<br>
<font color ='#00bcd4'> In [12]: </font>

{% highlight R %}
sample.sd.ALL <- sd(sample.ALL) * sqrt((n.ALL-1)/n.ALL)
sample.sd.AML <- sd(sample.AML) * sqrt((n.AML-1)/n.AML)
{% endhighlight %}

Estimate the population standard deviation

<br>
<font color ='#00bcd4'> In [13]: </font>

{% highlight R %}
sd.est.ALL <- sd(sample.ALL)
sd.est.AML <- sd(sample.AML)
{% endhighlight %}

Estimate the standard errors on the mean

<br>
<font color ='#00bcd4'> In [14]: </font>

{% highlight R %}
sd.err.est.ALL <- sd(sample.ALL) / sqrt(n.ALL)
sd.err.est.AML <- sd(sample.AML) / sqrt(n.AML)
{% endhighlight %}

Estimate the standard deviation of the difference between the two means
according to Student's formula

<br>
<font color ='#00bcd4'> In [15]: </font>

{% highlight R %}
diff.sd.est <- sqrt((n.ALL*sample.sd.ALL^2 + n.AML*sample.sd.AML^2) * (1/n.ALL + 1/n.AML) /(n.ALL+n.AML-2))
{% endhighlight %}

Compute `t.obs`

<br>
<font color ='#00bcd4'> In [16]: </font>

{% highlight R %}
d <- abs(mean.est.ALL - mean.est.AML)
t.obs.Student <- d/diff.sd.est
{% endhighlight %}

Compute the P- vale.
Since we are performing the two-tail test, the single-tail probability has to be
multiplied by 3 in order to obtai the alpha risk

<br>
<font color ='#00bcd4'> In [17]: </font>

{% highlight R %}
P.val.Student <- 2 * pt(q = t.obs.Student, df = n.ALL + n.AML-2, lower.tail = F)
{% endhighlight %}

### This is what you should be doing... FAST!

## 3. Apply the Student-Fischer t-test (this assumes that the two populations
have equal variance).


<br>
<font color ='#00bcd4'> In [18]: </font>

{% highlight R %}
t.student <- t.test(sample.ALL,sample.AML, var.equal=TRUE)
print(t.student)
{% endhighlight %}

## 4. Apply the Welch t-test (this does not assume that the two populations have
equal variance)

<br>
<font color ='#00bcd4'> In [19]: </font>

{% highlight R %}
t.welch <- t.test(sample.ALL,sample.AML, var.equal=FALSE)
print(t.welch)
{% endhighlight %}

**We want to test all the genes, so we could just loop over what was written
before ... (note it can take some time)**


<br>
<font color ='#00bcd4'> In [20]: </font>

{% highlight R %}
t.statistics <- vector()
P.values <- vector()
for (g in 1:nrow(golub.expr)) {
  #  print(paste("Testing gene", g))
  g.profile <- as.vector(golub.expr[g,])
  sample.ALL <- g.profile[cancer.type=="ALL"]
  sample.AML <- g.profile[cancer.type=="AML"]
  t <- t.test(sample.ALL,sample.AML)
  t.statistics <- append(t.statistics, t$statistic)
  P.values <- append(P.values, t$p.value)
}
{% endhighlight %}

<br>
<font color ='#00bcd4'> In [21]: </font>

{% highlight R %}
 print(P.values)
{% endhighlight %}

#### For a more efficient way, you can use apply

<br>
<font color ='#00bcd4'> In [22]: </font>

{% highlight R %}
Data=cbind(golub.expr,P.values)
colnames(Data)[39]='Raw.p'
{% endhighlight %}

Order data by pvalue

<br>
<font color ='#00bcd4'> In [23]: </font>

{% highlight R %}
Data = Data[order(Data[,'Raw.p']),]
{% endhighlight %}

Perform p-value adjustments and add to the data frame

<br>
<font color ='#00bcd4'> In [24]: </font>

{% highlight R %}
Datadf <- as.data.frame(Data)
{% endhighlight %}

<br>
<font color ='#00bcd4'> In [25]: </font>

{% highlight R %}
Datadf$Bonferroni =
  p.adjust(Datadf$Raw.p,
           method = "bonferroni")

Datadf$BH =
  p.adjust(Datadf$Raw.p,
           method = "BH")

Datadf$Holm =
  p.adjust(Datadf$ Raw.p,
           method = "holm")

Datadf$Hochberg =
  p.adjust(Datadf$ Raw.p,
           method = "hochberg")

Datadf$Hommel =
  p.adjust(Datadf$ Raw.p,
           method = "hommel")

Datadf$BY =
  p.adjust(Datadf$ Raw.p,
           method = "BY")
{% endhighlight %}

## 5. Plotting the obtained data

<br>
<font color ='#00bcd4'> In [26]: </font>

{% highlight R %}
X = Datadf$Raw.p
Y = cbind(Datadf$Bonferroni,
          Datadf$BH,
          Datadf$Holm,
          Datadf$Hochberg,
          Datadf$Hommel,
          Datadf$BY)
{% endhighlight %}

<br>
<font color ='#00bcd4'> In [27]: </font>

{% highlight R %}
matplot(X, Y,
        xlab="Raw p-value",
        ylab="Adjusted p-value",
        type="l",
        asp=1,
        col=1:6,
        lty=1,
        lwd=2)

legend('bottomright',
       legend = c("Bonferroni", "BH", "Holm", "Hochberg", "Hommel", "BY"),
       col = 1:6,
       cex = 1,    
       pch = 16)

abline(0, 1,
       col=1,
       lty=2,
       lwd=1)


{% endhighlight %}


![png]({{ site.url}}{{ site.baseurl }}/notebooks/Multiple%20Hyp_files/Multiple%20Hyp_50_0.png)
