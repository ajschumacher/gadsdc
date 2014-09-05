### Before

Read _Chapter 3: Linear Regression_ from [An Introduction to Statistical Learning with Applications in R](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20First%20Printing.pdf) (internal pages 59 to 126, PDF pages 74 to 141).

Optional:

 * Watch the [Chapter 3 lecture videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) to supplement the reading.
 

### Questions

 * What is your background with linear regression? What have you used it for, and how have you used it?
 * What questions or uncertainties do you have about your final project? What kinds of support would be helpful?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

[Slides](slides.pdf) on linear regression.

A pragmatic approach to model assumptions from Gelman: "[What are the key assumptions of linear regression?](http://andrewgelman.com/2013/08/04/19470/)".

Linear regression [exploration in R](lm.Rmd).

Exercise: Extended exploration with secret data: [train](train.csv) and [test](test.csv). Both sets include the `response` variable, so you can evaluate your performance yourself. Use test set RMSE (root mean squared error) to describe how well you're doing.

 * Download and load the data into `R`.
 * Look at the data.
 * Make exploratory graphs.
 * Make exploratory models.
 * Are there relationships between the variables? Make some notes (comments in code could be enough) as you notice things about the variables.
 * Consider tranforming values. Could it be helpful?
 * What RMSE can you get on the training data? On the test data?
     * Usually training error will be lower than test error, but this may not be the case for you with this data. Why not?
 * See how good a model you can build. How low can you get RMSE?

Hints:

 * Interactions are worth investigating!
 * While it may not be obvious, the data was made with a physical system in mind. Think like a physicist!
 * Do all the numeric values behave like numeric values?
 * Unlike a real-world problem, we know exactly how this data was created, so we also (as a result) know how what the *best* achievable performance is. Also unlike a real-world problem, the best achievable performance is zero test-set RMSE.


### After

Optional:

 * Write up your exploratory modeling. You can submit a file to the `09-linear_R` directory of the class repo.
 * Read the yhat [Fitting & Interpreting Linear Models in R](http://blog.yhathq.com/posts/r-lm-summary.html) to solidify your comfort with `lm`.
 * Read the Win-Vector post on [Correlation and R-Squared](http://www.win-vector.com/blog/2011/11/correlation-and-r-squared/).
 * Read about [robust regression](http://www.ats.ucla.edu/stat/r/dae/rreg.htm) at the UCLA Institute for Digital Research and Education sight.
