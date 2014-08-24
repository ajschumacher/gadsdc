### Before

Read [Generalized Linear Models (GLM)](http://www.wright.edu/~thaddeus.tarpey/ES714glm.pdf), focusing on section one, _Logistic Regression_.

Optional:

 * Check out this [deck](http://www.mc.vanderbilt.edu/gcrc/workshop_files/2004-11-12.pdf) introducing logistic regression.


### Questions

 * Say you run an L1-regularized regression and it selects five features (all the other coefficients are zero). You could fit an OLS regression with these five features. How would the the two techniques compare, in terms of computation and results?
 * Consider thinking of boolean multinomial Naive Bayes likelihood probabilities as coefficients on word dummy features. How are they similar or different as compared with linear regression coefficients? Could we use a linear model for probability labels?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

Warm up to slides with duck example:

 * Say the _probability_ that an animal is a duck is 25%, or 0.25.
 * Then the _odds_ that the animal is a duck is 0.25/(1-0.25) = 1/3, or "one to three against". (So if you bet a dollar to win three more if it's a duck, you break even long term.)
 * Then the _log odds_ that the animal is a duck is the (natural) log of the odds, ln(1/3) or just log(1/3), about -1.1.
 * If animals either quack or don't quack, we can make a dummy variable called quack and compare duck-ness of quackers vs. non-quackers. Quackers are ducks 90% of the time, and non-quackers are ducks 20% of the time, say. Then the _odds ratio_ is (0.9/(1-0.9))/(0.2/(1-0.2)) and the _log odds ratio_ is the (natural) log of that.

Logistic regression [slides](slides.pdf).

Follow up from the slides with duck example:

 * Using the quack vs. no-quack example, write out the logistic function. Fill in the values for the coefficients and confirm calculated probabilities are correct.

Logistic regression [example](logistic.Rmd).

Note that everything we've talked about with regard to test sets and cross-validation, and even everything we've done with regularization, can be applied to logistic regression! (The `glmnet` package has a `family` argument just like `glm` has.)

To get started with a beefier example, predict whether a car is a bad buy using the prepared [lemons](https://github.com/ajschumacher/gadsdata/tree/master/lemons) data.

Both Naive Bayes and Logistic Regression with `sklearn`:

 * [Naive Bayes and Logistic Regression](bayes_logistic.md)


### After

There is [logistic regression assignment](../logistic_assignment). It recommends some data and makes some specifics suggestions in the description, but you can use your own (project) data and you can use `R` or `Python`. There is a `logistic_assignment` directory of the class repo to hold your submitted work. We also have a highly specified linear regression assignment. To maintain focus on projects and not overload, we'll expect a write-up from you for either the linear or logistic assignment, but not necessarily both. Hopefully you can do what makes the most sense for you.


Optional:

 * Read [Generative and Discriminative Classifiers: Naive Bayes and Logistic Regression](http://www.cs.cmu.edu/~tom/mlbook/NBayesLogReg.pdf). This will likely help you to better understand both Naive Bayes and logistic regression, and how they can be thought of as related.
 * The UCLA Institute for Digital Research and Education has a lot of resources on using statistical software, such as: [R Data Analysis Examples: Logit Regression](http://www.ats.ucla.edu/stat/r/dae/logit.htm).
 * For a few general multiclass reduction approaches, read these papers on [Weighted One-Against All](http://hunch.net/~jl/projects/reductions/woa/woa.pdf) and [Error-Correcting Tournaments](http://hunch.net/~beygel/tournament.pdf).
 * Read much more on GLMs with a [chapter](http://www.sagepub.com/upm-data/21121_Chapter_15.pdf) on the topic.
 * Look through a notebook on [logistic regression with statsmodels for well switching in Bangledesh](http://nbviewer.ipython.org/github/carljv/Will_it_Python/blob/master/ARM/ch5/arsenic_wells_switching.ipynb).
