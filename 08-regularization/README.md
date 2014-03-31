### Before

Read _Chapter 3: Linear Methods for Regression_ from [The Elements of Statistical Learning](http://statweb.stanford.edu/~tibs/ElemStatLearn/printings/ESLII_print10.pdf) (internal pages 43 to 99, PDF pages 62 to 118).

Optional:

 * Check out [Linear algebra explained in four pages](http://cnd.mcgill.ca/~ivan/miniref/linear_algebra_in_4_pages.pdf)


### Questions

 * How do K Nearest Neighbors, Naive Bayes, and linear models compare in terms of model interpretability? How/when could this inform model choices?
 * What determines the complexity of a linear model, as it relates to model bias and variance? How can you control this complexity?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Project elevator pitches.

Question review.

[Slides](slides.pdf) on regularization for linear regression.

`glmnet` [demo](glmnet.Rmd).

Introduce the [linear regression assignment](../linear_assignment).

 * Write out a mean squared error function.
 * Experiment with some null models for `SalaryNormalized` - try zeros, and the intercept-only model.
 * Mention the idea of checking some distributions.
 * Use `grep` to hand-dummy some columns based on the text descriptions.
 * Note that the answers are available in `solution.csv` but performance should only be checked there as a _final_ step.


### After

Complete your [linear regression assignment](../linear_assignment). When you're done you'll have a `name.Rmd` (or similar) file in the `linear_assignment` directory of the class repo.

Optional:
 * Read this [glmnet vignette](http://www.stanford.edu/~hastie/glmnet/glmnet_alpha.html) for even more about using `R`'s `glmnet` package.
 * The `DAAG` `R` package includes `cv.lm` function which you might investigate. It may or may not be better than using your own.
