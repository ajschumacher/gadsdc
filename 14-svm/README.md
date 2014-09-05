### Before

 * Read the very friendly Chapter 18 (What's Your Vector, Victor?) on support vector machines from [Introduction to Data Science](http://jsresearch.net/). (It gives its example in `R`.)

Optional:

* Read this more exacting article, [A User's Guide to Support Vector Machines](http://pyml.sourceforge.net/doc/howto.pdf). (The class slides draw from this material.)
* Go through scikit's [documentation on SVMs](http://scikit-learn.org/dev/modules/svm.html).


### Questions

 * Imagine an example dataset with two continuous features corresponding to axes in the plane, and binary label. The label is 1 for examples within some distance of the origin, and 0 otherwise. How well would each of the classification algorithms we've seen so far perform with this data?
 * Say you have a red pile of rocks and a blue pile of rocks on the floor in a room. All the red rocks are to the left of all the blue rocks. How many rocks determine the minimum distance between the two piles? (Is it always the same number?)
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

[Slides](slides.pdf) on support vector machines.

Demonstrate a simple numerical example for the discriminant function. Use the training set ((1, 3), +1), ((2, 2), +1), ((1, 2), -1), ((2, 1), -1). Draw a separating hyperplane, get orthogonal vector (_w_), multiply matrices, find a _b_, interpret a little.

Reiterate two 'parts' of SVM:
 * maximum margin hyperplane
 * kernel function / kernel trick

Note that radial basis function (RBF) and Guassian kernel refer to the same thing.

Activity: Achieve better than 98% training accuracy with a support vector machine (`sklearn`'s `SVC` will do nicely) on the data in [data.csv](data.csv). Recommendation: First load the data and get something working. You'll probably use some combination of `pandas` `DataFrame`s and `numpy` `ndarray`s. Things that might be helpful: `values` and `shape`. Consider the parameters to `SVC`. You might also visualize things with matplotlib's `scatter`, for instance. Think about scaling as well. Remember you have access to functions like `mean` (etc.) on `DataFrame`s. Optionally, compare to other `sklearn` algorithms such as logistic regression.


### After

Optional:

 * Read [Support Vector Machines: Hype or Hallelujah?](http://www.bioconductor.org/help/course-materials/2008/BioC2008/labs/ml/ML1.pdf).
 * Read [Support Vector Machines in R](http://www.jstatsoft.org/v15/i09/paper), which provides a some theory in addition to an overview of implementations in `R`.
 * Read [A Tutorial on Support Vector Machines for Pattern
Recognition](https://web.archive.org/web/20120105072605/http://www.umiacs.umd.edu/~joseph/support-vector-machines4.pdf), which includes discussion of VC Dimension.
 * Go through this [tutorial](http://www.louisaslett.com/Courses/Data_Mining/ST4003-Lab7-Introduction_to_Support_Vector_Machines.pdf) on SVMs in `R` using `e1071`.
 * Watch the [Chapter 9 lecture videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) from *An Introduction to Statistical Learning* for more on SVMs and a comparison with logistic regression.
