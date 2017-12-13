---
layout: notebook
title: "Tutorial"
tags:
update_date:
code_version: 1
validation_pass:
---
<br />
# BAD Day 1: Tutorial  

# 0. Source/install the needed packages


<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[1]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># In case you need to install the packages</span>
 install.packages<span class="p">(</span><span class="s">&quot;xlsx&quot;</span><span class="p">)</span>
 install.packages<span class="p">(</span><span class="s">&quot;gdata&quot;</span><span class="p">)</span>
 install.packages<span class="p">(</span><span class="s">&quot;ape&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>
The downloaded binary packages are in
	/var/folders/1q/xdx6qpy905dbx01t7cfv36280000gn/T//RtmpMbXbxh/downloaded_packages

The downloaded binary packages are in
	/var/folders/1q/xdx6qpy905dbx01t7cfv36280000gn/T//RtmpMbXbxh/downloaded_packages

The downloaded binary packages are in
	/var/folders/1q/xdx6qpy905dbx01t7cfv36280000gn/T//RtmpMbXbxh/downloaded_packages
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[2]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="kn">source</span><span class="p">(</span><span class="s">&quot;http://bioconductor.org/biocLite.R&quot;</span><span class="p">);</span>
biocLite<span class="p">(</span><span class="s">&quot;multtest&quot;</span><span class="p">);</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>Bioconductor version 3.4 (BiocInstaller 1.24.0), ?biocLite for help
A new version of Bioconductor is available after installing the most recent
  version of R; see http://bioconductor.org/install
BioC_mirror: https://bioconductor.org
Using Bioconductor 3.4 (BiocInstaller 1.24.0), R 3.3.2 (2016-10-31).
Installing package(s) ‘multtest’
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>
The downloaded binary packages are in
	/var/folders/1q/xdx6qpy905dbx01t7cfv36280000gn/T//RtmpMbXbxh/downloaded_packages
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>Old packages: &#39;backports&#39;, &#39;devtools&#39;, &#39;jsonlite&#39;, &#39;knitr&#39;, &#39;pbdZMQ&#39;, &#39;R6&#39;,
  &#39;Rcpp&#39;, &#39;RcppArmadillo&#39;, &#39;tibble&#39;, &#39;tidyr&#39;
</pre>
</div>
</div>

</div>
</div>

</div>

# 1. Exploratory data analysis

We will be usig the Gene Expression dataset from **Golub et al (1999)**. The gene expression data collected by Golub et al. (1999) are among the most classical in bioinformatics. A selection of the set is called `golub` which is contained in the `multtest` package loaded before. 


The data consist of gene expression values of 3051 genes (rows) from 38 leukemia patients Pre-processing was done as described in Dudoit et al. (2002). The R code for pre-processing is available in the file ../doc/golub.R.

**Source**: 
Golub et al. (1999). Molecular classification of cancer: class discovery and class prediction by gene expression monitoring, Science, Vol. 286:531-537. (http://www-genome.wi.mit.edu/MPR/).

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[3]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="kn">require</span><span class="p">(</span>multtest<span class="p">);</span>

<span class="c1"># Usage</span>
data<span class="p">(</span>golub<span class="p">);</span>

<span class="c1"># If you need more information on the data set just</span>
<span class="c1"># uncomment the line below</span>
<span class="c1"># ?golub</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>Loading required package: multtest
Loading required package: BiocGenerics
Loading required package: parallel

Attaching package: ‘BiocGenerics’

The following objects are masked from ‘package:parallel’:

    clusterApply, clusterApplyLB, clusterCall, clusterEvalQ,
    clusterExport, clusterMap, parApply, parCapply, parLapply,
    parLapplyLB, parRapply, parSapply, parSapplyLB

The following objects are masked from ‘package:stats’:

    IQR, mad, xtabs

The following objects are masked from ‘package:base’:

    anyDuplicated, append, as.data.frame, cbind, colnames, do.call,
    duplicated, eval, evalq, Filter, Find, get, grep, grepl, intersect,
    is.unsorted, lapply, lengths, Map, mapply, match, mget, order,
    paste, pmax, pmax.int, pmin, pmin.int, Position, rank, rbind,
    Reduce, rownames, sapply, setdiff, sort, table, tapply, union,
    unique, unsplit, which, which.max, which.min

Loading required package: Biobase
Welcome to Bioconductor

    Vignettes contain introductory material; view with
    &#39;browseVignettes()&#39;. To cite Bioconductor, see
    &#39;citation(&#34;Biobase&#34;)&#39;, and for packages &#39;citation(&#34;pkgname&#34;)&#39;.

</pre>
</div>
</div>

</div>
</div>

</div>
Data set values:
- `golub`: matrix of gene expression levels for the 38 tumor mRNA samples, rows correspond to genes (3051 genes) and columns to mRNA samples.
- `golub.cl`: numeric vector indicating the tumor class, 27 acute lymphoblastic leukemia (ALL) cases (code 0) and 11 acute myeloid leukemia (AML) cases (code 1).
- `golub.names`: a matrix containing the names of the 3051 genes for the expression matrix golub. The three columns correspond to the gene index, ID, and Name, respectively.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[4]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Checking the dimension of the data</span>
<span class="kp">dim</span><span class="p">(</span>golub<span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<ol>
<li>3051</li>
<li>38</li>
</ol>


</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[5]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># we will have a look at the first rows contained in the data set</span>
<span class="kp">head</span><span class="p">(</span>golub<span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<p>| -1.45769 | -1.39420 | -1.42779 | -1.40715 | -1.42668 | -1.21719 | -1.37386 | -1.36832 | -1.47649 | -1.21583 | ⋯        | -1.08902 | -1.29865 | -1.26183 | -1.44434 |  1.10147 | -1.34158 | -1.22961 | -0.75919 | 0.84905  | -0.66465 | 
| -0.75161 | -1.26278 | -0.09052 | -0.99596 | -1.24245 | -0.69242 | -1.37386 | -0.50803 | -1.04533 | -0.81257 | ⋯        | -1.08902 | -1.05094 | -1.26183 | -1.25918 |  0.97813 | -0.79357 | -1.22961 | -0.71792 | 0.45127  | -0.45804 | 
|  0.45695 | -0.09654 |  0.90325 | -0.07194 |  0.03232 |  0.09713 | -0.11978 |  0.23381 |  0.23987 |  0.44201 | ⋯        | -0.43377 | -0.10823 | -0.29385 |  0.05067 |  1.69430 | -0.12472 |  0.04609 |  0.24347 | 0.90774  |  0.46509 | 
|  3.13533 |  0.21415 |  2.08754 |  2.23467 |  0.93811 |  2.24089 |  3.36576 |  1.97859 |  2.66468 | -1.21583 | ⋯        |  0.29598 | -1.29865 |  2.76869 |  2.08960 |  0.70003 |  0.13854 |  1.75908 |  0.06151 | 1.30297  |  0.58186 | 
|  2.76569 | -1.27045 |  1.60433 |  1.53182 |  1.63728 |  1.85697 |  3.01847 |  1.12853 |  2.17016 | -1.21583 | ⋯        | -1.08902 | -1.29865 |  2.00518 |  1.17454 | -1.47218 | -1.34158 |  1.55086 | -1.18107 | 1.01596  |  0.15788 | 
|  2.64342 |  1.01416 |  1.70477 |  1.63845 | -0.36075 |  1.73451 |  3.36576 |  0.96870 |  2.72368 | -1.21583 | ⋯        | -1.08902 | -1.29865 |  1.73780 |  0.89347 | -0.52883 | -1.22168 |  0.90832 | -1.39906 | 0.51266  |  1.36249 |</p>


</div>

</div>
</div>

</div>
The gene names are collected in the matrix `golub.gnames` of which the columns correspond to the gene index, ID, and Name, respectively.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[6]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Adding 3051 gene names</span>
<span class="kp">row.names</span><span class="p">(</span>golub<span class="p">)</span> <span class="o">=</span> golub.gnames<span class="p">[,</span><span class="m">3</span><span class="p">]</span>

<span class="kp">head</span><span class="p">(</span>golub<span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<p>| AFFX-HUMISGF3A/M97935_MA_at | -1.45769 | -1.39420 | -1.42779 | -1.40715 | -1.42668 | -1.21719 | -1.37386 | -1.36832 | -1.47649 | -1.21583 | ⋯        | -1.08902 | -1.29865 | -1.26183 | -1.44434 |  1.10147 | -1.34158 | -1.22961 | -0.75919 | 0.84905  | -0.66465 | 
| AFFX-HUMISGF3A/M97935_MB_at | -0.75161 | -1.26278 | -0.09052 | -0.99596 | -1.24245 | -0.69242 | -1.37386 | -0.50803 | -1.04533 | -0.81257 | ⋯        | -1.08902 | -1.05094 | -1.26183 | -1.25918 |  0.97813 | -0.79357 | -1.22961 | -0.71792 | 0.45127  | -0.45804 | 
| AFFX-HUMISGF3A/M97935_3_at |  0.45695 | -0.09654 |  0.90325 | -0.07194 |  0.03232 |  0.09713 | -0.11978 |  0.23381 |  0.23987 |  0.44201 | ⋯        | -0.43377 | -0.10823 | -0.29385 |  0.05067 |  1.69430 | -0.12472 |  0.04609 |  0.24347 | 0.90774  |  0.46509 | 
| AFFX-HUMRGE/M10098_5_at |  3.13533 |  0.21415 |  2.08754 |  2.23467 |  0.93811 |  2.24089 |  3.36576 |  1.97859 |  2.66468 | -1.21583 | ⋯        |  0.29598 | -1.29865 |  2.76869 |  2.08960 |  0.70003 |  0.13854 |  1.75908 |  0.06151 | 1.30297  |  0.58186 | 
| AFFX-HUMRGE/M10098_M_at |  2.76569 | -1.27045 |  1.60433 |  1.53182 |  1.63728 |  1.85697 |  3.01847 |  1.12853 |  2.17016 | -1.21583 | ⋯        | -1.08902 | -1.29865 |  2.00518 |  1.17454 | -1.47218 | -1.34158 |  1.55086 | -1.18107 | 1.01596  |  0.15788 | 
| AFFX-HUMRGE/M10098_3_at |  2.64342 |  1.01416 |  1.70477 |  1.63845 | -0.36075 |  1.73451 |  3.36576 |  0.96870 |  2.72368 | -1.21583 | ⋯        | -1.08902 | -1.29865 |  1.73780 |  0.89347 | -0.52883 | -1.22168 |  0.90832 | -1.39906 | 0.51266  |  1.36249 |</p>


</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[7]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Let&#39;s just have a look at the top 20 genes ID&#39;s contained in golub.gnames</span>
<span class="kp">head</span><span class="p">(</span>golub.gnames<span class="p">[,</span><span class="m">2</span><span class="p">],</span> n <span class="o">=</span> <span class="m">20</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<ol>
<li>'AFFX-HUMISGF3A/M97935_MA_at (endogenous control)'</li>
<li>'AFFX-HUMISGF3A/M97935_MB_at (endogenous control)'</li>
<li>'AFFX-HUMISGF3A/M97935_3_at (endogenous control)'</li>
<li>'AFFX-HUMRGE/M10098_5_at (endogenous control)'</li>
<li>'AFFX-HUMRGE/M10098_M_at (endogenous control)'</li>
<li>'AFFX-HUMRGE/M10098_3_at (endogenous control)'</li>
<li>'AFFX-HUMGAPDH/M33197_5_at (endogenous control)'</li>
<li>'AFFX-HUMGAPDH/M33197_M_at (endogenous control)'</li>
<li>'AFFX-HSAC07/X00351_5_at (endogenous control)'</li>
<li>'AFFX-HSAC07/X00351_M_at (endogenous control)'</li>
<li>'AFFX-HUMTFRR/M11507_5_at (endogenous control)'</li>
<li>'AFFX-HUMTFRR/M11507_M_at (endogenous control)'</li>
<li>'AFFX-HUMTFRR/M11507_3_at (endogenous control)'</li>
<li>'AFFX-M27830_5_at (endogenous control)'</li>
<li>'AFFX-M27830_M_at (endogenous control)'</li>
<li>'AFFX-M27830_3_at (endogenous control)'</li>
<li>'AFFX-HSAC07/X00351_3_st (endogenous control)'</li>
<li>'AFFX-HUMGAPDH/M33197_M_st (endogenous control)'</li>
<li>'AFFX-HUMGAPDH/M33197_3_st (endogenous control)'</li>
<li>'AFFX-HSAC07/X00351_M_st (endogenous control)'</li>
</ol>


</div>

</div>
</div>

</div>
Twenty-seven patients are diagnosed as acute lymphoblastic leukemia (ALL) and eleven as acute myeloid leukemia (AML). The tumor class is given by the numeric vector golub.cl, where ALL is indicated by 0 and AML by 1. 

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[8]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="kp">colnames</span><span class="p">(</span>golub<span class="p">)</span> <span class="o">=</span> golub.cl

<span class="kp">head</span><span class="p">(</span>golub<span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<table>
<thead><tr>
<th><!--/--></th>
<th>0</th>
<th>0</th>
<th>0</th>
<th>0</th>
<th>0</th>
<th>0</th>
<th>0</th>
<th>0</th>
<th>0</th>
<th>0</th>
<th>⋯</th>
<th>1</th>
<th>1</th>
<th>1</th>
<th>1</th>
<th>1</th>
<th>1</th>
<th>1</th>
<th>1</th>
<th>1</th>
<th>1</th>
</tr>
</thead>
<tbody>
<tr>
<td>AFFX-HUMISGF3A/M97935_MA_at</td>
<td>-1.45769</td>
<td>-1.39420</td>
<td>-1.42779</td>
<td>-1.40715</td>
<td>-1.42668</td>
<td>-1.21719</td>
<td>-1.37386</td>
<td>-1.36832</td>
<td>-1.47649</td>
<td>-1.21583</td>
<td>⋯</td>
<td>-1.08902</td>
<td>-1.29865</td>
<td>-1.26183</td>
<td>-1.44434</td>
<td>1.10147</td>
<td>-1.34158</td>
<td>-1.22961</td>
<td>-0.75919</td>
<td>0.84905</td>
<td>-0.66465</td>
</tr>
<tr>
<td>AFFX-HUMISGF3A/M97935_MB_at</td>
<td>-0.75161</td>
<td>-1.26278</td>
<td>-0.09052</td>
<td>-0.99596</td>
<td>-1.24245</td>
<td>-0.69242</td>
<td>-1.37386</td>
<td>-0.50803</td>
<td>-1.04533</td>
<td>-0.81257</td>
<td>⋯</td>
<td>-1.08902</td>
<td>-1.05094</td>
<td>-1.26183</td>
<td>-1.25918</td>
<td>0.97813</td>
<td>-0.79357</td>
<td>-1.22961</td>
<td>-0.71792</td>
<td>0.45127</td>
<td>-0.45804</td>
</tr>
<tr>
<td>AFFX-HUMISGF3A/M97935_3_at</td>
<td>0.45695</td>
<td>-0.09654</td>
<td>0.90325</td>
<td>-0.07194</td>
<td>0.03232</td>
<td>0.09713</td>
<td>-0.11978</td>
<td>0.23381</td>
<td>0.23987</td>
<td>0.44201</td>
<td>⋯</td>
<td>-0.43377</td>
<td>-0.10823</td>
<td>-0.29385</td>
<td>0.05067</td>
<td>1.69430</td>
<td>-0.12472</td>
<td>0.04609</td>
<td>0.24347</td>
<td>0.90774</td>
<td>0.46509</td>
</tr>
<tr>
<td>AFFX-HUMRGE/M10098_5_at</td>
<td>3.13533</td>
<td>0.21415</td>
<td>2.08754</td>
<td>2.23467</td>
<td>0.93811</td>
<td>2.24089</td>
<td>3.36576</td>
<td>1.97859</td>
<td>2.66468</td>
<td>-1.21583</td>
<td>⋯</td>
<td>0.29598</td>
<td>-1.29865</td>
<td>2.76869</td>
<td>2.08960</td>
<td>0.70003</td>
<td>0.13854</td>
<td>1.75908</td>
<td>0.06151</td>
<td>1.30297</td>
<td>0.58186</td>
</tr>
<tr>
<td>AFFX-HUMRGE/M10098_M_at</td>
<td>2.76569</td>
<td>-1.27045</td>
<td>1.60433</td>
<td>1.53182</td>
<td>1.63728</td>
<td>1.85697</td>
<td>3.01847</td>
<td>1.12853</td>
<td>2.17016</td>
<td>-1.21583</td>
<td>⋯</td>
<td>-1.08902</td>
<td>-1.29865</td>
<td>2.00518</td>
<td>1.17454</td>
<td>-1.47218</td>
<td>-1.34158</td>
<td>1.55086</td>
<td>-1.18107</td>
<td>1.01596</td>
<td>0.15788</td>
</tr>
<tr>
<td>AFFX-HUMRGE/M10098_3_at</td>
<td>2.64342</td>
<td>1.01416</td>
<td>1.70477</td>
<td>1.63845</td>
<td>-0.36075</td>
<td>1.73451</td>
<td>3.36576</td>
<td>0.96870</td>
<td>2.72368</td>
<td>-1.21583</td>
<td>⋯</td>
<td>-1.08902</td>
<td>-1.29865</td>
<td>1.73780</td>
<td>0.89347</td>
<td>-0.52883</td>
<td>-1.22168</td>
<td>0.90832</td>
<td>-1.39906</td>
<td>0.51266</td>
<td>1.36249</td>
</tr>
</tbody>
</table>


</div>

</div>
</div>

</div>
Note that sometimes it is better to construct a factor which indicates the tumor class of the patients. Such a factor could be used for instance to separate the tumor groups for plotting purposes.  The factor (`gol.fac`) can be contructed as follows.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[9]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>gol.fac <span class="o">&lt;-</span>  <span class="kp">factor</span><span class="p">(</span>golub.cl<span class="p">,</span> levels <span class="o">=</span> <span class="m">0</span><span class="o">:</span><span class="m">1</span><span class="p">,</span> labels <span class="o">=</span> <span class="kt">c</span><span class="p">(</span><span class="s">&quot;AML&quot;</span><span class="p">,</span> <span class="s">&quot;ALL&quot;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

</div>
The labels correspond to the two tumor classes. The evaluation of gol.fac=="ALL" returns
TRUE for the first twenty-seven values and FALSE for the remaining eleven,
which is useful as a column index for selecting the expression values of the
ALL patients. The expression values of gene CCND3 Cyclin D3 from the
ALL patients can now be printed to the screen, as follows.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[10]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>golub<span class="p">[</span><span class="m">1042</span><span class="p">,</span> gol.fac <span class="o">==</span> <span class="s">&quot;ALL&quot;</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<p>1
:   0.889411
:   1.450141
:   0.429041
:   0.826671
:   0.636371
:   1.02251
:   0.127581
:   -0.743331
:   0.737841
:   0.49471
:   1.12058</p>


</div>

</div>
</div>

</div>
## Creating the exploratory plots

### 1.1\. Plotting the value of gene (CCND3) in all nRNA samples (M92287_at)

We shall first have a look at the expression values of a gener with manufacurer name `M92278_at`, which is known in biology as "CCND3 Cyclin D3".

The expression values of this gene are collected in row 1042 of golub. To load the data and to obtain the relevant information from row 1042 of golub.gnames, use the following:

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[11]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>mygene <span class="o">&lt;-</span> golub<span class="p">[</span><span class="m">1042</span><span class="p">,</span> <span class="p">]</span>
</pre></div>

</div>
</div>
</div>

</div>
The data has now been stored in the `golub` matrix. We will now plot the expression values od the gene CCND3 Cyclin D3.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[12]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>plot<span class="p">(</span>mygene<span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_21_0.png"
>
</div>

</div>

</div>
</div>

</div>
In the previous plot we just used the default plotting preferences within R base plotting.We can do some improvements so that the plot is easily understood.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[13]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>plot<span class="p">(</span>mygene<span class="p">,</span> pch <span class="o">=</span> <span class="m">15</span><span class="p">,</span> col <span class="o">=</span> <span class="s">&#39;slateblue&#39;</span><span class="p">,</span> ylab <span class="o">=</span> <span class="s">&#39;Expression value of gene: CCND3&#39;</span><span class="p">,</span> 
    main <span class="o">=</span> <span class="s">&#39; Gene expression values of CCND3 Cyclin D3&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_23_0.png"
>
</div>

</div>

</div>
</div>

</div>
In this plot the vertical axis corresponds to the size of the expression values and the horizontal axis the index of the patients. 

### 1.2\. Gene expression between patient 1 (ALL) and patient 38 (AML) 

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[14]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>plot<span class="p">(</span>golub<span class="p">[,</span><span class="m">1</span><span class="p">],</span> golub<span class="p">[,</span><span class="m">38</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_26_0.png"
>
</div>

</div>

</div>
</div>

</div>
Adding diagonal lines to the plot and changing axes labels


<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[15]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>plot<span class="p">(</span>golub<span class="p">[,</span><span class="m">1</span><span class="p">],</span> golub<span class="p">[,</span><span class="m">38</span><span class="p">],</span> xlab <span class="o">=</span> <span class="s">&#39;Patient 1 (ALL)&#39;</span><span class="p">,</span> ylab <span class="o">=</span> <span class="s">&#39;Patient 38 (AML)&#39;</span><span class="p">)</span> 
abline<span class="p">(</span>a <span class="o">=</span> <span class="m">0</span><span class="p">,</span> b <span class="o">=</span> <span class="m">1</span><span class="p">,</span> col <span class="o">=</span> <span class="s">&#39;mediumpurple&#39;</span><span class="p">,</span> lwd <span class="o">=</span><span class="m">3</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_28_0.png"
>
</div>

</div>

</div>
</div>

</div>
### 1.3\. Scatter plots to detect independence


<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[16]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>mysamplist <span class="o">&lt;-</span> golub<span class="p">[,</span> <span class="kt">c</span><span class="p">(</span><span class="m">1</span><span class="o">:</span><span class="m">15</span><span class="p">)]</span>
<span class="kp">colnames</span><span class="p">(</span>mysamplist<span class="p">)</span> <span class="o">=</span> <span class="kt">c</span><span class="p">(</span><span class="m">1</span><span class="o">:</span><span class="m">15</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[17]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>plot<span class="p">(</span><span class="kp">as.data.frame</span><span class="p">(</span>mysamplist<span class="p">),</span> pch<span class="o">=</span><span class="s">&#39;.&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_31_0.png"
>
</div>

</div>

</div>
</div>

</div>
### 1.4\. Bar plot of 4 cyclin genes expression values in 3 ALL and AML patients

We will analyse the expression values of the `D13639_at, M92287_at, U11791_at, Z36714_AT` genes in three chosen AML and ALL patients

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[18]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>mygenelist <span class="o">&lt;-</span> golub<span class="p">[</span><span class="kt">c</span><span class="p">(</span><span class="m">85</span><span class="p">,</span> <span class="m">1042</span><span class="p">,</span> <span class="m">1212</span><span class="p">,</span> <span class="m">2240</span><span class="p">),</span> <span class="kt">c</span><span class="p">(</span><span class="m">1</span><span class="o">:</span><span class="m">3</span><span class="p">,</span> <span class="m">36</span><span class="o">:</span><span class="m">38</span><span class="p">)]</span>

<span class="c1"># having a look at the data set chosen</span>
mygenelist
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<table>
<thead><tr>
<th><!--/--></th>
<th>0</th>
<th>0</th>
<th>0</th>
<th>1</th>
<th>1</th>
<th>1</th>
</tr>
</thead>
<tbody>
<tr>
<td>D13639_at</td>
<td>2.09511</td>
<td>1.71953</td>
<td>-1.46227</td>
<td>-0.92935</td>
<td>-0.11091</td>
<td>1.15591</td>
</tr>
<tr>
<td>M92287_at</td>
<td>2.10892</td>
<td>1.52405</td>
<td>1.96403</td>
<td>0.73784</td>
<td>0.49470</td>
<td>1.12058</td>
</tr>
<tr>
<td>U11791_at</td>
<td>-0.11439</td>
<td>-0.72887</td>
<td>-0.39674</td>
<td>-0.94364</td>
<td>0.05047</td>
<td>0.05905</td>
</tr>
<tr>
<td>Z36714_at</td>
<td>-1.45769</td>
<td>-1.39420</td>
<td>-1.46227</td>
<td>-1.39906</td>
<td>-1.34579</td>
<td>-1.32403</td>
</tr>
</tbody>
</table>


</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[19]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>barplot<span class="p">(</span>mygenelist<span class="p">)</span>
box<span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_34_0.png"
>
</div>

</div>

</div>
</div>

</div>
The plot is not very easy to read, so we will add some colours and a legend so that we know which gene each bar segment corresponds to.


<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[20]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># custom colours </span>
colours <span class="o">=</span> <span class="kt">c</span><span class="p">(</span><span class="s">&#39;lightblue2&#39;</span><span class="p">,</span>   <span class="s">&#39;slateblue&#39;</span><span class="p">,</span> <span class="s">&#39;#BD7BB8&#39;</span><span class="p">,</span> <span class="s">&#39;#2B377A&#39;</span><span class="p">)</span>

barplot<span class="p">(</span>mygenelist<span class="p">,</span> col <span class="o">=</span> colours<span class="p">,</span> legend <span class="o">=</span> <span class="kc">TRUE</span><span class="p">,</span> border <span class="o">=</span> <span class="s">&#39;white&#39;</span><span class="p">)</span>
box<span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_36_0.png"
>
</div>

</div>

</div>
</div>

</div>
In this case the patients are indicated on the `X` axis (0 and 1 respectively) while the gene expression level is indicate on the `Y` axis. 

We can make some improvements to the plots.
Let's have a look at the `barplot` arguments:

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[21]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="o">?</span>barplot
</pre></div>

</div>
</div>
</div>

</div>
We are going to focus on only a few of the histgram arguments:
- `beside`: `TRUE` for the bars to be displayed as justapoxed bars, `FALSE` for stacked bars
- `horiz` : `FALSE` bars displayed vertically with the first bar to the left, `TRUE` bars are displayed horizontally with the first at the bottom.
- `ylim`, `xlim` :  limits for the y and x axes
- `col`: colour choices

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[22]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>barplot<span class="p">(</span>mygenelist<span class="p">,</span> horiz <span class="o">=</span> <span class="kc">TRUE</span><span class="p">,</span> col <span class="o">=</span> colours<span class="p">,</span> legend <span class="o">=</span> <span class="kc">TRUE</span><span class="p">,</span>
       ylab <span class="o">=</span> <span class="s">&#39;Patient&#39;</span><span class="p">,</span> border <span class="o">=</span> <span class="s">&#39;white&#39;</span><span class="p">,</span> 
        xlab <span class="o">=</span> <span class="s">&#39;Gene expression level&#39;</span><span class="p">,</span> main  <span class="o">=</span> <span class="s">&#39;Cycline genes expression&#39;</span><span class="p">)</span>
box<span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_40_0.png"
>
</div>

</div>

</div>
</div>

</div>
In the plot above we presented the barplots horizontally and added some colours, which makes it easier to understand the data presented.
You can also use the barplots to represent the mean and standard error which we will be doing in the following sections.

### 1.5\. Plotting the mean

In the following we will compute the mean for the expression values of both the ALL and AML patients. We will be using the same 4 cycline genes used in the example above.

First we will compute the ALL and AML for all the patients. Once the means are computed they are combined into a single data frame. 

Finally, the means are plotted using the `barplot` function.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[23]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Calculating the mean of the chosen genes from patient 1 to 27 and 28 to 38</span>
ALLmean <span class="o">&lt;-</span> <span class="kp">rowMeans</span><span class="p">(</span>golub<span class="p">[</span><span class="kt">c</span><span class="p">(</span><span class="m">85</span><span class="p">,</span><span class="m">1042</span><span class="p">,</span><span class="m">1212</span><span class="p">,</span><span class="m">2240</span><span class="p">),</span><span class="kt">c</span><span class="p">(</span><span class="m">1</span><span class="o">:</span><span class="m">27</span><span class="p">)])</span>
AMLmean <span class="o">&lt;-</span> <span class="kp">rowMeans</span><span class="p">(</span>golub<span class="p">[</span><span class="kt">c</span><span class="p">(</span><span class="m">85</span><span class="p">,</span><span class="m">1042</span><span class="p">,</span><span class="m">1212</span><span class="p">,</span><span class="m">2240</span><span class="p">),</span><span class="kt">c</span><span class="p">(</span><span class="m">28</span><span class="o">:</span><span class="m">38</span><span class="p">)])</span>

<span class="c1"># Combining the mean matrices previously calculated</span>
dataheight <span class="o">&lt;-</span> <span class="kp">cbind</span><span class="p">(</span>ALLmean<span class="p">,</span> AMLmean<span class="p">)</span>

<span class="c1"># Plotting </span>
barx <span class="o">&lt;-</span> barplot<span class="p">(</span>dataheight<span class="p">,</span> beside<span class="o">=</span><span class="bp">T</span><span class="p">,</span> horiz<span class="o">=</span><span class="bp">F</span><span class="p">,</span> col<span class="o">=</span> colours<span class="p">,</span> ylim<span class="o">=</span><span class="kt">c</span><span class="p">(</span><span class="m">-2</span><span class="p">,</span><span class="m">2.5</span><span class="p">),</span>
                legend <span class="o">=</span> <span class="kc">TRUE</span><span class="p">,</span>border <span class="o">=</span> <span class="s">&#39;white&#39;</span> <span class="p">,</span>
                ylab <span class="o">=</span> <span class="s">&#39;Gene expression level&#39;</span><span class="p">,</span> main <span class="o">=</span> <span class="s">&#39;Cycline genes mean expression</span>
<span class="s">in AML and ALL patients&#39;</span><span class="p">)</span>
box<span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_43_0.png"
>
</div>

</div>

</div>
</div>

</div>
### 1.6\. Adding error bars to the previous plot


In the previous section we computed the mean expression level for 4 cycline genes between the AML and ALL patients. Sometimes it is useful to add error bars to the plots (as the one above) to convey the uncertainty in the data presented. 

For such a purpose we often use the **Standard Deviation**:


$$ \sigma = \sqrt{\frac{\sum_{i=1}^{n}\left(x_i -\mu \right)^2}{N}}$$


which in turn tells us how much the values in a certain group tend to deviate from their mean value. 

Let's start calculating the Standard Deviation of the data.



<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[24]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Calculating the SD</span>
ALLsd <span class="o">&lt;-</span> <span class="kp">apply</span><span class="p">(</span>golub<span class="p">[</span><span class="kt">c</span><span class="p">(</span><span class="m">85</span><span class="p">,</span><span class="m">1042</span><span class="p">,</span><span class="m">1212</span><span class="p">,</span><span class="m">2240</span><span class="p">),</span><span class="kt">c</span><span class="p">(</span><span class="m">1</span><span class="o">:</span><span class="m">27</span><span class="p">)],</span> <span class="m">1</span><span class="p">,</span> sd<span class="p">)</span>
nALL<span class="o">=</span><span class="kp">length</span><span class="p">(</span><span class="kt">c</span><span class="p">(</span><span class="m">1</span><span class="o">:</span><span class="m">27</span><span class="p">))</span>
AMLsd <span class="o">&lt;-</span> <span class="kp">apply</span><span class="p">(</span>golub<span class="p">[</span><span class="kt">c</span><span class="p">(</span><span class="m">85</span><span class="p">,</span><span class="m">1042</span><span class="p">,</span><span class="m">1212</span><span class="p">,</span><span class="m">2240</span><span class="p">),</span><span class="kt">c</span><span class="p">(</span><span class="m">28</span><span class="o">:</span><span class="m">38</span><span class="p">)],</span> <span class="m">1</span><span class="p">,</span> sd<span class="p">)</span>
nAML<span class="o">=</span><span class="kp">length</span><span class="p">(</span><span class="kt">c</span><span class="p">(</span><span class="m">28</span><span class="o">:</span><span class="m">38</span><span class="p">))</span>

<span class="c1"># Combining the data</span>
datasd <span class="o">&lt;-</span> <span class="kp">cbind</span><span class="p">(</span>ALLsd<span class="p">,</span> AMLsd<span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
Another measure used to quantify the deviation is the **standard error**, which qutifies the variability in the **_means_** of our groups instead of reporting the variability among the data points.

A relatively straigtforward way to compute this is by assuming if we were to repeat a  given experiment many many times, then it would roughly follow a normal distribution. **Note – this is a big assumption**.  hence, if we assuemt hat the means follow a nosmal distribution, then the standard error (_a.k.a. variability of group means_) can be defined as:

$$ SE  = \frac{SD}{\sqrt{n}} $$

which in layman terms can be read as  “take the general variability of the points around their group means (the standard deviation), and scale this number by the number of points that you’ve collected”. 

Since we have already computed the SD we can now compute the standard error (SE).

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[25]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>datase <span class="o">&lt;-</span> <span class="kp">cbind</span><span class="p">(</span>ALLsd<span class="o">/</span><span class="kp">sqrt</span><span class="p">(</span>nALL<span class="p">),</span> AMLsd<span class="o">/</span><span class="kp">sqrt</span><span class="p">(</span>nAML<span class="p">))</span>
</pre></div>

</div>
</div>
</div>

</div>
Now we can create a plot of the mean data as well as the SE and SD.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[26]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># creating a panel of 2 plots displayed in 1 row</span>
par<span class="p">(</span>mfrow <span class="o">=</span> <span class="kt">c</span><span class="p">(</span><span class="m">1</span><span class="p">,</span><span class="m">2</span><span class="p">))</span>

<span class="c1"># Plot with the SD</span>
datasdend<span class="o">&lt;-</span><span class="kp">abs</span><span class="p">(</span>dataheight<span class="p">)</span> <span class="o">+</span> <span class="kp">abs</span><span class="p">(</span>datasd<span class="p">)</span>
datasdend<span class="p">[</span><span class="kt">c</span><span class="p">(</span><span class="m">3</span><span class="p">,</span><span class="m">4</span><span class="p">),]</span> <span class="o">=</span> <span class="o">-</span> datasdend<span class="p">[</span><span class="kt">c</span><span class="p">(</span><span class="m">3</span><span class="p">,</span><span class="m">4</span><span class="p">),]</span>
barx <span class="o">&lt;-</span> barplot<span class="p">(</span>dataheight<span class="p">,</span> beside<span class="o">=</span><span class="bp">T</span><span class="p">,</span> horiz<span class="o">=</span><span class="bp">F</span><span class="p">,</span> col <span class="o">=</span> colours<span class="p">,</span> ylim<span class="o">=</span><span class="kt">c</span><span class="p">(</span><span class="m">-2</span><span class="p">,</span><span class="m">2.5</span><span class="p">),</span>
               main <span class="o">=</span> <span class="s">&#39;Data +  SD&#39;</span><span class="p">,</span> border <span class="o">=</span> <span class="s">&#39;white&#39;</span><span class="p">)</span>
abline<span class="p">(</span>a <span class="o">=</span> <span class="m">0</span> <span class="p">,</span> b <span class="o">=</span> <span class="m">0</span><span class="p">,</span> h <span class="o">=</span> <span class="m">0</span><span class="p">)</span>
arrows<span class="p">(</span>barx<span class="p">,</span> dataheight<span class="p">,</span> barx<span class="p">,</span> datasdend<span class="p">,</span> angle<span class="o">=</span><span class="m">90</span><span class="p">,</span> lwd <span class="o">=</span> <span class="m">2</span><span class="p">,</span> length <span class="o">=</span> <span class="m">0.15</span><span class="p">,</span> 
       col <span class="o">=</span> <span class="s">&#39;navyblue&#39;</span><span class="p">)</span>
box<span class="p">()</span>

<span class="c1"># Plot with the se: error associated to the mean!</span>
datasdend<span class="o">&lt;-</span><span class="kp">abs</span><span class="p">(</span>dataheight<span class="p">)</span> <span class="o">+</span> <span class="kp">abs</span><span class="p">(</span>datase<span class="p">)</span>
datasdend<span class="p">[</span><span class="kt">c</span><span class="p">(</span><span class="m">3</span><span class="p">,</span><span class="m">4</span><span class="p">),]</span> <span class="o">=</span> <span class="o">-</span>datasdend<span class="p">[</span><span class="kt">c</span><span class="p">(</span><span class="m">3</span><span class="p">,</span><span class="m">4</span><span class="p">),]</span>
barx <span class="o">&lt;-</span> barplot<span class="p">(</span>dataheight<span class="p">,</span> beside<span class="o">=</span><span class="bp">T</span><span class="p">,</span> horiz<span class="o">=</span><span class="bp">F</span><span class="p">,</span> col <span class="o">=</span> colours<span class="p">,</span> ylim<span class="o">=</span><span class="kt">c</span><span class="p">(</span><span class="m">-2</span><span class="p">,</span><span class="m">2.5</span><span class="p">),</span>
               main <span class="o">=</span> <span class="s">&#39;Data + SE&#39;</span><span class="p">,</span> border <span class="o">=</span> <span class="s">&#39;white&#39;</span><span class="p">)</span>
abline<span class="p">(</span>a <span class="o">=</span> <span class="m">0</span> <span class="p">,</span> b <span class="o">=</span> <span class="m">0</span><span class="p">,</span> h <span class="o">=</span> <span class="m">0</span><span class="p">)</span>
arrows<span class="p">(</span>barx<span class="p">,</span> dataheight<span class="p">,</span> barx<span class="p">,</span> datasdend<span class="p">,</span> angle<span class="o">=</span><span class="m">90</span><span class="p">,</span> lwd <span class="o">=</span> <span class="m">2</span><span class="p">,</span> length <span class="o">=</span> <span class="m">0.15</span><span class="p">,</span>
       col <span class="o">=</span> <span class="s">&#39;navyblue&#39;</span><span class="p">)</span>
box<span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_49_0.png"
>
</div>

</div>

</div>
</div>

</div>
Note that the error bars for the SE are smaller than those for the SD. This is no coincidence! 

As we increase N (in the SE equation), we will decrease the error. Hence the standard error will **always** be smaller than the SD.

## 2. Data representation
This section presents some essential manners to display and visualize  data. 

### 2.1 Frequency table 
Discrete data occur when the values naturally fall into categories. A frequency table simply gives the number of occurrences within a category.

A gene consists of a sequence of nucleotides (A; C; G; T)

The number of each nucleotide can be displayed in a frequency table.

This will be illustrated by the Zyxin gene which plays an important role in cell adhesion The accession number (X94991.1) of one of its variants can be found in a data base like NCBI (UniGene). The code below illustrates how to read the sequence ”X94991.1” of the species homo sapiens from GenBank, to construct a
pie from a frequency table of the four nucleotides .

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[27]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="kn">library</span><span class="p">(</span><span class="s">&#39;ape&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[29]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>v <span class="o">=</span> read.GenBank<span class="p">(</span><span class="kt">c</span><span class="p">(</span><span class="s">&quot;X94991.1&quot;</span><span class="p">),</span>as.character <span class="o">=</span> <span class="kc">TRUE</span><span class="p">)</span>

pie<span class="p">(</span><span class="kp">table</span><span class="p">(</span>v<span class="o">$</span>X94991.1<span class="p">),</span> col <span class="o">=</span> colours<span class="p">,</span> border <span class="o">=</span> <span class="s">&#39;white&#39;</span><span class="p">)</span>

<span class="c1"># prints the data as a table </span>
<span class="kp">table</span><span class="p">(</span>read.GenBank<span class="p">(</span><span class="kt">c</span><span class="p">(</span><span class="s">&quot;X94991.1&quot;</span><span class="p">),</span>as.character<span class="o">=</span><span class="kc">TRUE</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>
  a   c   g   t 
410 789 573 394 </pre>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_53_1.png"
>
</div>

</div>

</div>
</div>

</div>
### 2.2 Stripcharts

An elementary method to visualize data is by using a so-called stripchart,
by which the values of the data are represented as e.g. small boxes
it is useful in combination with a factor that distinguishes members from
different experimental conditions or patients groups.

Once again we use the CCND3 Cyclin D3 data to generate the plots.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[30]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># data(golub, package = &quot;multtest&quot;)</span>
gol.fac <span class="o">&lt;-</span> <span class="kp">factor</span><span class="p">(</span>golub.cl<span class="p">,</span>levels<span class="o">=</span><span class="m">0</span><span class="o">:</span><span class="m">1</span><span class="p">,</span> labels<span class="o">=</span> <span class="kt">c</span><span class="p">(</span><span class="s">&quot;ALL&quot;</span><span class="p">,</span><span class="s">&quot;AML&quot;</span><span class="p">))</span>

stripchart<span class="p">(</span>golub<span class="p">[</span><span class="m">1042</span><span class="p">,]</span> <span class="o">~</span> gol.fac<span class="p">,</span> method <span class="o">=</span> <span class="s">&quot;jitter&quot;</span><span class="p">,</span> 
           col <span class="o">=</span> <span class="kt">c</span><span class="p">(</span><span class="s">&#39;slateblue&#39;</span><span class="p">,</span> <span class="s">&#39;darkgrey&#39;</span><span class="p">),</span> pch <span class="o">=</span> <span class="m">16</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_55_0.png"
>
</div>

</div>

</div>
</div>

</div>
From the above figure, it can be observed that the CCND3 Cyclin D3 expression values of the ALL patients tend to have larger expression values than those of the AML patient.


### 2.3 Histograms 

Another method to visualize data is by dividing the range of data values into
a number of intervals and to plot the frequency per interval as a bar. Such
a plot is called a histogram.

We will now generate a histogram of the expression values of gene CCND3 Cyclin D3 as well as all the genes for the AML and ALL patients contained in the Golub dataset.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[31]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>par<span class="p">(</span>mfrow<span class="o">=</span><span class="kt">c</span><span class="p">(</span><span class="m">2</span><span class="p">,</span><span class="m">2</span><span class="p">))</span>

hist<span class="p">(</span>golub<span class="p">[</span><span class="m">1042</span><span class="p">,</span> gol.fac <span class="o">==</span> <span class="s">&quot;ALL&quot;</span><span class="p">],</span> 
     col <span class="o">=</span> <span class="s">&#39;slateblue&#39;</span><span class="p">,</span> border <span class="o">=</span> <span class="s">&#39;white&#39;</span><span class="p">,</span>
    main <span class="o">=</span> <span class="s">&#39;Golub[1042], ALL&#39;</span><span class="p">,</span> xlab <span class="o">=</span> <span class="s">&#39;ALL&#39;</span><span class="p">)</span>
box<span class="p">()</span>

hist<span class="p">(</span>golub<span class="p">,</span>breaks <span class="o">=</span> <span class="m">10</span><span class="p">,</span> 
    col <span class="o">=</span> <span class="s">&#39;slateblue&#39;</span><span class="p">,</span> border <span class="o">=</span> <span class="s">&#39;white&#39;</span><span class="p">,</span>
    main <span class="o">=</span>  <span class="s">&#39;Golub&#39;</span><span class="p">)</span>
box<span class="p">()</span>

hist<span class="p">(</span>golub<span class="p">[,</span> gol.fac <span class="o">==</span> <span class="s">&quot;AML&quot;</span><span class="p">],</span>breaks <span class="o">=</span> <span class="m">10</span><span class="p">,</span> 
     col <span class="o">=</span> <span class="s">&#39;slateblue&#39;</span><span class="p">,</span> border <span class="o">=</span> <span class="s">&#39;white&#39;</span><span class="p">,</span>
    main <span class="o">=</span> <span class="s">&#39;Golub, AML&#39;</span><span class="p">,</span> xlab <span class="o">=</span> <span class="s">&#39;AML&#39;</span><span class="p">)</span>
box<span class="p">()</span>

hist<span class="p">(</span>golub<span class="p">[,</span> gol.fac <span class="o">==</span> <span class="s">&quot;ALL&quot;</span><span class="p">],</span>breaks <span class="o">=</span> <span class="m">10</span><span class="p">,</span>
     col <span class="o">=</span> <span class="s">&#39;slateblue&#39;</span><span class="p">,</span> border <span class="o">=</span> <span class="s">&#39;white&#39;</span><span class="p">,</span>
    main <span class="o">=</span> <span class="s">&#39;Golub, ALL&#39;</span><span class="p">,</span> xlab <span class="o">=</span> <span class="s">&#39;ALL&#39;</span><span class="p">)</span>
box<span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_58_0.png"
>
</div>

</div>

</div>
</div>

</div>
### 2.3 Boxplots

A popular method to display data is by
drawing a box around the 1st and the 3rd quartile (a bold line segment                                                     for the median), and the smaller line segments (whiskers) for the smallest and
the largest data values. 

Such a data display is known as a box-and-whisker plot. 

We will start by creating a vector with gene expression values sorted in ascending order (using the `sort` function). 

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[32]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Sort the values of one gene</span>
x <span class="o">&lt;-</span> <span class="kp">sort</span><span class="p">(</span>golub<span class="p">[</span><span class="m">1042</span><span class="p">,</span> gol.fac<span class="o">==</span><span class="s">&quot;ALL&quot;</span><span class="p">],</span> decreasing <span class="o">=</span> <span class="kc">FALSE</span><span class="p">)</span>

<span class="c1"># printing the first five values</span>
x<span class="p">[</span><span class="m">1</span><span class="o">:</span><span class="m">5</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<p>0
:   0.458270
:   1.105460
:   1.276450
:   1.325510
:   1.36844</p>


</div>

</div>
</div>

</div>
A view on the distribution of the gene expression values of the `ALL` and `AML` patients on gene CCND3 Cyclin D3 can be obtained by  generating two separate boxplots adjacent to each other:

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[41]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Even though we are creating two boxplots we only need one major graph</span>
par<span class="p">(</span>mfrow<span class="o">=</span><span class="kt">c</span><span class="p">(</span><span class="m">1</span><span class="p">,</span><span class="m">1</span><span class="p">))</span>
boxplot<span class="p">(</span>golub<span class="p">[</span><span class="m">1042</span><span class="p">,]</span> <span class="o">~</span> gol.fac<span class="p">,</span> col <span class="o">=</span> <span class="kt">c</span><span class="p">(</span><span class="s">&#39;lightblue2&#39;</span><span class="p">,</span> <span class="s">&#39;mediumpurple&#39;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_62_0.png"
>
</div>

</div>

</div>
</div>

</div>
It can be observed that the gene expression values for ALL are larger than those for AML. Furthermore, since the two sub-boxes around the median are more or less equally wide, the data are quite symmetrically distributed around the median.

We can create a histogram of the expression values of gene CCND3 Cyclin D3 of the acute lymphoblastic leukemia patients e.g.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[110]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>hist<span class="p">(</span>golub<span class="p">[</span><span class="m">1042</span><span class="p">,],</span> col<span class="o">=</span> <span class="s">&#39;lightblue&#39;</span><span class="p">,</span> border<span class="o">=</span> <span class="s">&#39;black&#39;</span><span class="p">,</span> breaks<span class="o">=</span> <span class="m">6</span><span class="p">,</span> freq<span class="o">=</span> <span class="bp">F</span><span class="p">,</span>
     main <span class="o">=</span> <span class="s">&#39;Expression values of gene CCND3 Cyclin D3&#39;</span><span class="p">)</span>
lines<span class="p">(</span>density<span class="p">(</span>golub<span class="p">[</span><span class="m">1042</span><span class="p">,]),</span> col<span class="o">=</span> <span class="s">&#39;slateblue&#39;</span><span class="p">,</span> lwd <span class="o">=</span> <span class="m">3</span><span class="p">)</span>
box<span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_64_0.png"
>
</div>

</div>

</div>
</div>

</div>
Now we can observe the distribution of all gene expressions values in all 38 patients

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[113]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>boxplot<span class="p">(</span>golub<span class="p">,</span> col<span class="o">=</span> <span class="s">&#39;lightblue2&#39;</span><span class="p">,</span> lwd <span class="o">=</span> <span class="m">1</span><span class="p">,</span> border<span class="o">=</span><span class="s">&quot;black&quot;</span><span class="p">,</span> pch<span class="o">=</span><span class="m">18</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_66_0.png"
>
</div>

</div>

</div>
</div>

</div>
To compute the exact values for the quartiles we need a sequence running from 0 to 1 with increments in steps of 0.25

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[114]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>pvec <span class="o">&lt;-</span> <span class="kp">seq</span><span class="p">(</span><span class="m">0</span><span class="p">,</span> <span class="m">1</span><span class="p">,</span> <span class="m">0.25</span><span class="p">)</span>
quantile<span class="p">(</span>golub<span class="p">[</span><span class="m">1042</span><span class="p">,</span> gol.fac<span class="o">==</span><span class="s">&#39;ALL&#39;</span><span class="p">],</span> pvec<span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<p>0%
:   0.4582725%
:   1.79606550%
:   1.9277675%
:   2.178705100%
:   2.7661</p>


</div>

</div>
</div>

</div>
Outliers are data points lying far apart from the pattern set by the majority of the data values. The implementation in R of the boxplot draws such outliers as smalle circles. 

A data point `x` is defined (graphically, not statistically) as an outlier point if $$x < 0.25 x -1.5\left(0.75 x -0.25 x\right) [x>0.25x >1.5(0.75x-0.25x)]$$


### 2.4 Q-Q plots (Quantile-quantile plots)

A method to visualize the distribution of gene expression values is y the so-called quantile-quantile (Q-Q) plots. In such a plot the quantiles of the gene expression values are displayed against the corresponding quantiles of the normal distribution (bell-shaped).

A straight line is added to represent the points which
correspond exactly to the quantiles of the normal distribution. By observing
the extent in which the points appear on the line, it can be evaluated to
what degree the data are normally distributed. That is, the closer the gene
expression values appear to the line, the more likely it is that the data are
normally distributed.

To produce a Q-Q plot of the ALL gene expression values of CCND3 Cyclin D3 one may use the following.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[116]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>qqnorm<span class="p">(</span>golub<span class="p">[</span><span class="m">1042</span><span class="p">,</span> gol.fac <span class="o">==</span> <span class="s">&#39;ALL&#39;</span><span class="p">])</span>
qqline<span class="p">(</span>golub<span class="p">[</span><span class="m">1042</span><span class="p">,</span> gol.fac <span class="o">==</span> <span class="s">&#39;ALL&#39;</span><span class="p">],</span> col <span class="o">=</span> <span class="s">&#39;slateblue&#39;</span><span class="p">,</span> lwd <span class="o">=</span> <span class="m">2</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_72_0.png"
>
</div>

</div>

</div>
</div>

</div>
It can be seen that most of the data points are on or near the straight line, while a few others are further away. The above example illustrates a case where the degree of non-normality is moderate so that a clear conclusion cannot be drawn.


## 3. Loading tab-delimited data

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[117]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>mydata<span class="o">&lt;-</span>read.delim<span class="p">(</span><span class="s">&quot;./NeuralStemCellData.tab.txt&quot;</span><span class="p">,</span> row.names<span class="o">=</span><span class="m">1</span><span class="p">,</span> header<span class="o">=</span><span class="bp">T</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[118]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="kp">class</span><span class="p">(</span>mydata<span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<p>'data.frame'</p>


</div>

</div>
</div>

</div>
### Now try and do some exploratory analysis of your own on this data!


GvHD flow cytometry data

Only exract the CD3 positive cells


<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt"><font color ='#00bcd4'>In&nbsp;[119]: </font></div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span>cor<span class="p">(</span>mydata<span class="p">[,</span><span class="m">1</span><span class="p">],</span>mydata<span class="p">[,</span><span class="m">2</span><span class="p">])</span>
plot<span class="p">(</span>mydata<span class="p">[,</span><span class="m">1</span><span class="p">],</span>mydata<span class="p">[,</span><span class="m">3</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<p>0.956021382271511</p>


</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="{{site.url}}{{site.baseurl}}/images/notebook_images/Tutorial/Tutorial_79_1.png"
>
</div>

</div>

</div>
</div>

</div>
 

