### Before

 * Watch the [10-minute tour of pandas](http://vimeo.com/59324550).
 * Read through the [scikit-learn quick-start](http://scikit-learn.org/dev/tutorial/basic/tutorial.html).

Optional:

 * Go through a brief [Learn pandas](http://nbviewer.ipython.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb) IPython notebook.
 * Take a peak at the [Machine Learning Cheat Sheet (for scikit-learn)](http://peekaboo-vision.blogspot.com/2013/01/machine-learning-cheat-sheet-for-scikit.html).


### Questions



### During

Application presentation.

Question review.

Warm-up: Write a function that takes a CSV file's name (string) argument and returns the list-of-lists representation of the file.

Building up from base Python:
 * `import numpy as np` ([tutorial one](http://scipy-lectures.github.io/intro/numpy/array_object.html), [tutorial two](http://wiki.scipy.org/Tentative_NumPy_Tutorial))
 * `import pandas as pd` ([tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html))
 * `sklearn` ([documentation](http://scikit-learn.org/dev/documentation.html)) and friends

The `sklearn` pattern:
 1. Import a class (make it available)
 2. Instantiate (make one)
 3. Fit (give it data)
 4. Transform/Predict (get results)

Go through the [walk-through](walkthrough.py) together.

Go through the following:

 * [KNN](knn.md)
 * [Linear Regression](linear.md)
 * [Naive Bayes and Logistic Regression](bayes_logistic.md)

These also introduce [`statsmodels`](http://statsmodels.sourceforge.net/)/[`patsy`](http://patsy.readthedocs.org/), scoring/cross-validation with `sklearn`, and some other syntax.


### After

Do the [logistic regression assignment](../logistic_assignment), due Monday April 28.

Optional:

 * Check out "[Datalicious Notebookmania – My favorite 7 IPython Notebooks](http://beautifuldata.net/2014/03/datalicious-notebookmania-my-favorite-7-ipython-notebooks/)".
 * Look through a notebook on [logistic regression with statsmodels for well switching in Bangledesh](http://nbviewer.ipython.org/github/carljv/Will_it_Python/blob/master/ARM/ch5/arsenic_wells_switching.ipynb).
 * There are other kinds of analyis such as survival analysis which can also be done in Python with, e.g., [lifelines](http://lifelines.readthedocs.org/).
