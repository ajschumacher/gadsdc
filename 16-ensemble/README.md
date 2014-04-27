### Before

 * Read [Choosing a Machine Learning Classifier](http://blog.echen.me/2011/04/27/choosing-a-machine-learning-classifier/).
 * Read this [post](http://blog.yhathq.com/posts/random-forests-in-python.html) on random forests in Python.

Optional:

 * Read [Ensemble Methods in Machine Learning](http://www.cs.iastate.edu/~jtian/cs573/Papers/Dietterich-ensemble-00.pdf).
 * Read [A few useful things to know about machine learning](http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) for the second time. It should be pretty familiar material by now!


### Questions

 * How do the models we've seen deal with variously scaled features? Which are scale invariant?
 * If you want to know the opinion of the country, why is it better to ask more than just a handful of people? What is the problem with a small sample size? What is the advantage of a larger sample size, and does it always hold?
 * How does the idea of sample size correspond / not correspond to modeling? If it's good to "ask more people", is it also good to "ask more models"?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Warm-up coding: Make a `Pipeline` incorporating a `StandardScaler` and an `SVC` to solve the circular data problem from `15-svm`. What training accuracy do the default settings achieve?

Question review.

Ensemble [slides](slides.pdf).

Work through the provided [code and words](tf-idf_forests.md) on tf-idf and random forests in Python.


### After

Optional:

 * Read through the `sklearn` [documentation on ensemble methods](http://scikit-learn.org/dev/modules/ensemble.html).
 * Check out Jay Hyer's excellent slides on [Ensemble Methods](http://adataheadsdiary.files.wordpress.com/2013/12/dsdc-ensemble-learing.pdf).
 * Check out kaggle's [Getting Started With Random Forests](http://www.kaggle.com/c/titanic-gettingStarted/details/getting-started-with-random-forests).
 * You might look into this [post](http://citizennet.com/blog/2012/11/10/random-forests-ensembles-and-performance-metrics/) about neural nets and random forests, oh my.
