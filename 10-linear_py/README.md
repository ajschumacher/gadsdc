### Before

 * Read through the [scikit-learn quick-start](http://scikit-learn.org/dev/tutorial/basic/tutorial.html).
 * Take a peak at the [Machine Learning Cheat Sheet (for scikit-learn)](http://peekaboo-vision.blogspot.com/2013/01/machine-learning-cheat-sheet-for-scikit.html).

Optional:

 * Read _Chapter 3: Linear Methods for Regression_ from [The Elements of Statistical Learning](http://statweb.stanford.edu/~tibs/ElemStatLearn/printings/ESLII_print10.pdf) (internal pages 43 to 99, PDF pages 62 to 118).
 * Check out [Linear algebra explained in four pages](http://cnd.mcgill.ca/~ivan/miniref/linear_algebra_in_4_pages.pdf)


### Questions

 * Try to describe "the machine learning process" without reference to
   any particular algorithm(s). What are the generic "objects" and
   "actions" of the process?
 * When coding, do you tend to prefer more fine-grained control over
   details or more high-level abstractions? When is one more useful
   than the other?
 * What other thoughts, comments, concerns, and questions do you have?
   What's on your mind?


### During

Application presentation.

Question review.

[Slides](slides.pdf) on regularization for linear regression.

`glmnet` [demo](glmnet.Rmd).

Building up from base Python:
 * `numpy`
 * `pandas` (Don't forget about [`pandas`' visualization](http://pandas.pydata.org/pandas-docs/stable/visualization.html)!)
 * [`patsy`](http://patsy.readthedocs.org/) (see also: [patsy quick start](https://patsy.readthedocs.org/en/latest/quickstart.html) (see also: [Why's it called "patsy"?](http://seveninchesofyourtime.com/wp-content/uploads/2014/08/montypython7.gif))
 * [`statsmodels`](http://statsmodels.sourceforge.net/devel/)
 * `sklearn` ([documentation](http://scikit-learn.org/dev/documentation.html))

Build up to [linear regression in Python](linear.ipynb).

The `sklearn` pattern:
 1. Import a class (make it available)
 2. Instantiate (make one)
 3. Fit (give it data)
 4. Transform/Predict (get results)

Question to consider: How do we change text into features?

Explore the [sklearn pattern](sklearn_pattern.ipynb) together.

Go through [KNN](knn.md) to learn more about `sklearn`.

Exercise: Do in `Python` the equivalent of what we did with `R` for the exercise data from last class.


### After

There is [linear regression assignment](../linear_assignment). It specifies particular data and some specifics suggestions in the description are for `R`, but you can use your own (project) data and you can use `R` or `Python`. There is a `linear_assignment` directory of the class repo to hold your submitted work. We also have a highly specified logistic regression assignment. To maintain focus on projects and not overload, we'll expect a write-up from you for either the linear or logistic assignment, but not necessarily both. Hopefully you can do what makes the most sense for you.

Optional:
 * Read this [glmnet vignette](http://www.stanford.edu/~hastie/glmnet/glmnet_alpha.html) for even more about using `R`'s `glmnet` package.
 * The `DAAG` `R` package includes `cv.lm` function which you might investigate. It may or may not be better than using your own.
 * Check out the [intro to scikit-learn][] video series from SciPy2013.
 * Learn more about `sklearn` by reading [API design for machine learning software: experiences from the scikit-learn project](http://arxiv.org/abs/1309.0238).
 * Check out "[Datalicious Notebookmania – My favorite 7 IPython Notebooks](http://beautifuldata.net/2014/03/datalicious-notebookmania-my-favorite-7-ipython-notebooks/)".
 * There are other kinds of analyis such as survival analysis which can also be done in Python with, e.g., [lifelines](http://lifelines.readthedocs.org/).

[intro to scikit-learn]: https://www.youtube.com/watch?v=r4bRUvvlaBw
