### Before

 * Watch the [10-minute tour of pandas](http://vimeo.com/59324550).
 * Read through the [scikit-learn quick-start](http://scikit-learn.org/dev/tutorial/basic/tutorial.html).

Optional:

 * Go through a brief [Learn pandas](http://nbviewer.ipython.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb) IPython notebook.
 * Take a peak at the [Machine Learning Cheat Sheet (for scikit-learn)](http://peekaboo-vision.blogspot.com/2013/01/machine-learning-cheat-sheet-for-scikit.html).


### Questions

 * Try to describe "the machine learning process" without reference to any particular algorithm(s). What are the generic "objects" and "actions" of the process?
 * When coding, do you tend to prefer more fine-grained control over details or more high-level abstractions? When is one more useful than the other?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

Warm-up: Write a function that takes a CSV file's name (string) argument and returns the list of lists representation of the file.

Building up from base Python:
 * `import numpy as np`
 * `import pandas as pd`
 * `sklearn` and friends

The `sklearn` pattern:
 1. Import a class (make it available)
 2. Instantiate (make one)
 3. Fit (give it data)
 4. Transform/Predict (get results)

For example:

```Python
# Example data
data = pd.DataFrame({'score': [10, 4, 29],
                     'comment': ['it was okay',
                                 'it was so bad',
                                 'it was so good']})

# sklearn pattern example one
from sklearn.feature_extraction.text import CountVectorizer  # 1
vect = CountVectorizer()                                     # 2
vect.fit(data.comment)                                       # 3
train_matrix = vect.transform(data.comment)                  # 4
test_matrix = vect.transform(["kind of good"])               # 4
# check vect.get_feature_names() and .toarray() for sparse matrices

# sklearn pattern example two
from sklearn.linear_model import LinearRegression            # 1
model = LinearRegression()                                   # 2
model.fit(train_matrix, data.score)                          # 3
model.predict(test_matrix)                                   # 4
```

Go through the following:

 * [KNN](knn.md)
 * [Linear Regression](linear.md)
 * [Naive Bayes and Logistic Regression](bayes_logistic.md)

These also introduce [`statsmodels`](http://statsmodels.sourceforge.net/)/[`patsy`](http://patsy.readthedocs.org/), scoring/cross-validation with `sklearn`, and some other syntax.

See also: [sklearn documentation](http://scikit-learn.org/dev/documentation.html)


### After

Do the [logistic regression assignment](../logistic_assignment), due Monday April 28.

Optional:

 * Check out "[Datalicious Notebookmania – My favorite 7 IPython Notebooks](http://beautifuldata.net/2014/03/datalicious-notebookmania-my-favorite-7-ipython-notebooks/)".
 * Look through a notebook on [logistic regression with statsmodels for well switching in Bangledesh](http://nbviewer.ipython.org/github/carljv/Will_it_Python/blob/master/ARM/ch5/arsenic_wells_switching.ipynb).
