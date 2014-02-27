# TODO: clean/clarify and probably split across multipe files/days

# Python Basics
# Introduction to Python

##Python Shell
Like R, Python at it's core is a fancy calculator.  Typing `python` into the command line will give you a prompt
```sh
python
```

##Defining functions
In Python we define functions by using the `def` keyword.

```Python
def addition(x, y):
  return x + y
```
`x` and `y` are the inputs to the function and the `return` keyword tells us what the function responds.  The most important thing to note here is that Python respect whitespace, the second like **must** be indented for this to run.

##Data Structures

Python has a variety of data structures available.  The most basic of them are the basic integer, float and strings.

###Lists

Lists are one of the most common data structures in Python.

```Python 
l = [1,2,3,4] #Setting up a list
l.append(5) #Adding to it using the append function
l += [6] #Adding to it using the addition operation
```

###Dictionaries

Dictionaries in Python are equivalent to Hash Tables in any other language.

```Python
x = {} # Empty Dictionary
y = {'key' : value}
y[key] = "new-value"
```

##Loop Constructs

Like any other programming language, Python has loop constructs, the ability to iterate over different elements.

```Python

l = [1,2,3,4]
for i in l:
  print i
```

However, when possible, Python will perform better using list comprehensions.

```Python
x = [1,2,3,4]

#The following are equivalent
y = []
for i in x:
  y.append(i**2)

#OR

y = [i**2 for i in x]
```

##Scikits.learn

`scikits.learn` has become one of the most popular machine learning packages in Python.  It has a most of the standard machine learning algorithms built-in and often calls faster external C-code that can make execuation fairly quick.

```Python
from sklearn.datasets import load_iris
iris = load_iris()

from sklearn import neighbors
X, y = iris.data, iris.target
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
# What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
print iris.target_names[knn.predict([[3, 5, 4, 2]])]
```

```Python
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(...)
clf = ...
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)

from sklearn import metrics
print metrics.classification_report(y_test, predicted)
print metrics.confusion_matrix(y_test, predicted)
print metrics.f1_score(y_test, predicted)
```

```Python
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
X_train, X_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

scores = cross_val_score(knn, iris.data, iris.target, cv=5)
```

###Naive Bayes in Sklearn
Download the 20 News Group Dataset

```sh
wget http://people.csail.mit.edu/jrennie/20Newsgroups/20news-bydate.tar.gz
tar -xf 20news-bydate.tar.gz
```

```Python
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the text data
categories = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]
twenty_train_subset = load_files('20news-bydate-train/', categories=categories, charset='latin-1')
twenty_test_subset = load_files('20news-bydate-test/', categories=categories, charset='latin-1')

# Turn the text documents into vectors of word frequencies
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(twenty_train_subset.data)
y_train = twenty_train_subset.target

# Fit a classifier on the training set
classifier = MultinomialNB().fit(X_train, y_train)
print("Training score: {0:.1f}%".format(classifier.score(X_train, y_train) * 100))

# Evaluate the classifier on the testing set
X_test = vectorizer.transform(twenty_test_subset.data)
y_test = twenty_test_subset.target
print("Testing score: {0:.1f}%".format(classifier.score(X_test, y_test) * 100))

from sklearn import metrics
metrics.confusion_matrix(y_test, classifier.predict(X_test))
```

##Pandas

Pandas is a Python library for data analysis that resembles the tools available in R.  It is also optimized for fast I/O and data manipulation.

```Python
import pandas as pd

data = pd.read_csv('Dropbox/src/538model/data/2012_poll_data_states.csv', sep='\t')
print data['Poll']
data.describe()

data['Poll'].value_counts()

data.groupby('Poll')['Obama (D)'].mean()
```
