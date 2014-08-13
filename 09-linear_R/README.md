### Before

Read _Chapter 3: Linear Regression_ from [An Introduction to Statistical Learning with Applications in R](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20First%20Printing.pdf) (internal pages 59 to 126, PDF pages 74 to 141).

Optional:

Watch the related videos from the [Statistical Learning course](https://class.stanford.edu/courses/HumanitiesScience/StatLearning/Winter2014/about) taught by the authors of the book:

 * [Simple Linear Regression](https://www.youtube.com/watch?v=PsE9UqoWtS4) (13:01)
 * [Hypothesis Testing and Confidence Intervals](https://www.youtube.com/watch?v=J6AdoiNUyWI) (8:24)
 * [Multiple Linear Regression](https://www.youtube.com/watch?v=1hbCJyM9ccs) (15:37)
 * [Some Important Questions](https://www.youtube.com/watch?v=3T6RXmIHbJ4) (14:51)
 * [Extensions of the Linear Model](https://www.youtube.com/watch?v=IFzVxLv0TKQ) (14:16)
 * [Linear Regression in R](https://www.youtube.com/watch?v=5ONFqIk3RFg) (22:10)


### Questions

 * Suppose you have features that correspond to length, width, and height, and you're predicting a label which is volume. Could you use KNN? Explain how it could work (with some relevant implementation details), or why it wouldn't work.
 * Suppose you have features that correspond to length, width, and height, and you're predicting a label which is volume. Could you use a Bayesian approach? Explain how it could work (with some relevant implementation details), or why it wouldn't work.
 * Suppose you have features that correspond to length, width, and height, and you're predicting a label which is volume. Could you use linear regression? Explain how it could work (with some relevant implementation details), or why it wouldn't work.
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

[Slides](slides.pdf) on linear regression.

Linear regression [exploration in R](lm.Rmd).

Extended exploration with [baseball data](https://github.com/ajschumacher/gadsdata/tree/master/baseball):

 * Download and load the data into `R`.
 * Combine some/all of the data (using `merge`) to create a dataset from which to model `salary`.
 * Make a couple exploratory graphs and models.
 * Consider tranforming values. Could it be helpful?
 * Build out a cross-validation framework for testing `lm` models. (What evaluation metric are you using?)
 * See how good a model you can build.


### After

Optional:

 * Write up your baseball salary modeling. You can submit a file to the `07-linear` directory of the class repo.
 * Read the yhat [Fitting & Interpreting Linear Models in R](http://blog.yhathq.com/posts/r-lm-summary.html) to solidify your comfort with `lm`.
 * Read the Win-Vector post on [Correlation and R-Squared](http://www.win-vector.com/blog/2011/11/correlation-and-r-squared/).
 * Read about [robust regression](http://www.ats.ucla.edu/stat/r/dae/rreg.htm) at the UCLA Institute for Digital Research and Education sight.
