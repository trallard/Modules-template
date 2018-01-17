---
layout: notebook
title: "Classify_demo"
tags:
update_date: 17-01-2018
code_version: 793828d
author: Tania Allard
validation_pass: 'yes'
badge: "https://img.shields.io/badge/notebook-validated-brightgreen.svg"
---
<br/>
# Classification algorithms

***

## Random Forest implementation using sklearn

source: [Random Forests in Python](http://blog.yhat.com/posts/random-forests-in-
python.html)

__Note about the data__: we will be using the famous iris data set which
contains 4 variables measuring various parts of iris flowers (of 3 species) aas
well as the species name.


### Preliminar: load packages
<font color="#808080">
 In&nbsp;[1]:
</font>
```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
```

### Loading the data
<font color="#808080">
 In&nbsp;[2]:
</font>
```python
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)


df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
```
<font color="#808080">
 In&nbsp;[3]:
</font>
```python
df.head()
```
<div>
 <style scoped="">
  .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
 </style>
 <table border="1" class="table-responsive table-striped">
  <thead>
   <tr style="text-align: right;">
    <th>
    </th>
    <th>
     sepal length (cm)
    </th>
    <th>
     sepal width (cm)
    </th>
    <th>
     petal length (cm)
    </th>
    <th>
     petal width (cm)
    </th>
    <th>
     species
    </th>
   </tr>
  </thead>
  <tbody>
   <tr>
    <th>
     0
    </th>
    <td>
     5.1
    </td>
    <td>
     3.5
    </td>
    <td>
     1.4
    </td>
    <td>
     0.2
    </td>
    <td>
     setosa
    </td>
   </tr>
   <tr>
    <th>
     1
    </th>
    <td>
     4.9
    </td>
    <td>
     3.0
    </td>
    <td>
     1.4
    </td>
    <td>
     0.2
    </td>
    <td>
     setosa
    </td>
   </tr>
   <tr>
    <th>
     2
    </th>
    <td>
     4.7
    </td>
    <td>
     3.2
    </td>
    <td>
     1.3
    </td>
    <td>
     0.2
    </td>
    <td>
     setosa
    </td>
   </tr>
   <tr>
    <th>
     3
    </th>
    <td>
     4.6
    </td>
    <td>
     3.1
    </td>
    <td>
     1.5
    </td>
    <td>
     0.2
    </td>
    <td>
     setosa
    </td>
   </tr>
   <tr>
    <th>
     4
    </th>
    <td>
     5.0
    </td>
    <td>
     3.6
    </td>
    <td>
     1.4
    </td>
    <td>
     0.2
    </td>
    <td>
     setosa
    </td>
   </tr>
  </tbody>
 </table>
</div>
### Creating the training and testing data
<font color="#808080">
 In&nbsp;[4]:
</font>
```python
df['is_train'] = np.random.uniform(0, 1, len(df)) &lt;= .75
df.head()
```
<div>
 <style scoped="">
  .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
 </style>
 <table border="1" class="table-responsive table-striped">
  <thead>
   <tr style="text-align: right;">
    <th>
    </th>
    <th>
     sepal length (cm)
    </th>
    <th>
     sepal width (cm)
    </th>
    <th>
     petal length (cm)
    </th>
    <th>
     petal width (cm)
    </th>
    <th>
     species
    </th>
    <th>
     is_train
    </th>
   </tr>
  </thead>
  <tbody>
   <tr>
    <th>
     0
    </th>
    <td>
     5.1
    </td>
    <td>
     3.5
    </td>
    <td>
     1.4
    </td>
    <td>
     0.2
    </td>
    <td>
     setosa
    </td>
    <td>
     True
    </td>
   </tr>
   <tr>
    <th>
     1
    </th>
    <td>
     4.9
    </td>
    <td>
     3.0
    </td>
    <td>
     1.4
    </td>
    <td>
     0.2
    </td>
    <td>
     setosa
    </td>
    <td>
     True
    </td>
   </tr>
   <tr>
    <th>
     2
    </th>
    <td>
     4.7
    </td>
    <td>
     3.2
    </td>
    <td>
     1.3
    </td>
    <td>
     0.2
    </td>
    <td>
     setosa
    </td>
    <td>
     True
    </td>
   </tr>
   <tr>
    <th>
     3
    </th>
    <td>
     4.6
    </td>
    <td>
     3.1
    </td>
    <td>
     1.5
    </td>
    <td>
     0.2
    </td>
    <td>
     setosa
    </td>
    <td>
     True
    </td>
   </tr>
   <tr>
    <th>
     4
    </th>
    <td>
     5.0
    </td>
    <td>
     3.6
    </td>
    <td>
     1.4
    </td>
    <td>
     0.2
    </td>
    <td>
     setosa
    </td>
    <td>
     False
    </td>
   </tr>
  </tbody>
 </table>
</div>
<font color="#808080">
 In&nbsp;[5]:
</font>
```python
train, test = df[df['is_train']==True], df[df['is_train']==False]
```

### Preprocessing the data
<font color="#808080">
 In&nbsp;[6]:
</font>
```python
# Create a list of the feature column's names
features = df.columns[:4]
features
```




    Index(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
           'petal width (cm)'],
          dtype='object')
<font color="#808080">
 In&nbsp;[7]:
</font>
```python
# train['species'] contains the actual species names. Before we can use it,
# we need to convert each species name into a digit. So, in this case there
# are three species, which have been coded as 0, 1, or 2.
y, _ = pd.factorize(train['species'])
```
<font color="#808080">
 In&nbsp;[8]:
</font>
```python
print(y)
```

### Training the random forest classifier
<font color="#808080">
 In&nbsp;[9]:
</font>
```python
clf = RandomForestClassifier(n_jobs = 2 )

# Training the classifier
clf.fit(train[features], y)
```




    RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                max_depth=None, max_features='auto', max_leaf_nodes=None,
                min_impurity_decrease=0.0, min_impurity_split=None,
                min_samples_leaf=1, min_samples_split=2,
                min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=2,
                oob_score=False, random_state=None, verbose=0,
                warm_start=False)



### Applying to the data
<font color="#808080">
 In&nbsp;[10]:
</font>
```python
preds = iris.target_names[clf.predict(test[features])]
```
<font color="#808080">
 In&nbsp;[11]:
</font>
```python
pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['predicted'])
```
<div>
 <style scoped="">
  .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
 </style>
 <table border="1" class="table-responsive table-striped">
  <thead>
   <tr style="text-align: right;">
    <th>
     predicted
    </th>
    <th>
     setosa
    </th>
    <th>
     versicolor
    </th>
    <th>
     virginica
    </th>
   </tr>
   <tr>
    <th>
     actual
    </th>
    <th>
    </th>
    <th>
    </th>
    <th>
    </th>
   </tr>
  </thead>
  <tbody>
   <tr>
    <th>
     setosa
    </th>
    <td>
     5
    </td>
    <td>
     0
    </td>
    <td>
     0
    </td>
   </tr>
   <tr>
    <th>
     versicolor
    </th>
    <td>
     0
    </td>
    <td>
     11
    </td>
    <td>
     0
    </td>
   </tr>
   <tr>
    <th>
     virginica
    </th>
    <td>
     0
    </td>
    <td>
     2
    </td>
    <td>
     12
    </td>
   </tr>
  </tbody>
 </table>
</div>
### View feature importance
<font color="#808080">
 In&nbsp;[12]:
</font>
```python
list(zip(train[features], clf.feature_importances_))
```




    [('sepal length (cm)', 0.16992592921521485),
     ('sepal width (cm)', 0.019510194239802908),
     ('petal length (cm)', 0.18115102228639413),
     ('petal width (cm)', 0.62941285425858806)]



***

## K- Means

### Preliminar : load packages
<font color="#808080">
 In&nbsp;[13]:
</font>
```python
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
```

### Loading the data
<font color="#808080">
 In&nbsp;[14]:
</font>
```python
iris = load_iris()


# converting to a pandas DF for ease of use
x = pd.DataFrame(iris.data, columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
y = pd.DataFrame(iris.target, columns=['Target'])
```

### Exploratory visualization of the data
<font color="#808080">
 In&nbsp;[15]:
</font>
```python
# creating a plot of the data first
plt.style.use('ggplot')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (8, 4), sharey =False)
colors = np.array(['darkviolet', 'c', 'black'])

#Draw a Scatter plot for Sepal Length vs Sepal Width
#nrows=1, ncols=2, plot_number=1
ax1.scatter(x['Sepal Length'], x['Sepal Width'], c=colors[y['Target']], s = 20)
ax1.set_title('Sepal Length vs Sepal Width')

ax2.scatter(x['Petal Length'], x['Petal Width'], c= colors[y['Target']], s = 20)
ax2.set_title('Petal Length vs Petal Width');
```
<img alt="png" src="{{site.url}}{{site.baseurl}}/images/notebook_images/Classify_demo/Classify_demo_31_0.png"/>
### Create a model object consiting of 3 clusters
<font color="#808080">
 In&nbsp;[16]:
</font>
```python
model = KMeans(n_clusters = 3)
```

### Apllying the model on the data
<font color="#808080">
 In&nbsp;[17]:
</font>
```python
model.fit(x)
```




    KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
        n_clusters=3, n_init=10, n_jobs=1, precompute_distances='auto',
        random_state=None, tol=0.0001, verbose=0)
<font color="#808080">
 In&nbsp;[18]:
</font>
```python
# model.labels_ contains the array of cluster ids
print (model.labels_)
```

Visualise the output of the model
<font color="#808080">
 In&nbsp;[19]:
</font>
```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (8, 4), sharey =False)

predictedY = np.choose(model.labels_, [1, 0, 2]).astype(np.int64)


# Plot the classifications that we saw earlier between Petal Length and Petal Width

ax1.scatter(x['Petal Length'], x['Petal Width'], c=colors[y['Target']], s=20)
ax1.set_title('Real classification')

# Plot the classifications according to the model
ax2.scatter(x['Petal Length'], x['Petal Width'], c=colors[predictedY], s=20)
ax2.set_title("Model's classification");
```
<img alt="png" src="{{site.url}}{{site.baseurl}}/images/notebook_images/Classify_demo/Classify_demo_38_0.png"/>
<font color="#808080">
 In&nbsp;[20]:
</font>
```python
import time
print('This notebook was last run on: ' + time.strftime('%d/%m/%y') + ' at: ' + time.strftime('%H:%M:%S'))
```
