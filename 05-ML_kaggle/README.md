### Before

Read [A few useful things to know about machine learning](http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf). We're reading this paper now, and then again toward the end of the class; this is your first read through it.

Optional:

 * Go through Fortmann-Roe's [Understanding the Bias-Variance Tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html). This is perhaps a more readable introduction and covers KNN, which we're doing in class.


### Questions

 * What is the relationship between the terms "bias" and "variance" in the machine learning sense, and "accuracy" and "precision" in the measurement sense?
 * What is the relationship between correlation and causation?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Question review.

Application presentation.

[Take a look](knn_iris_demo.Rmd) at applying KNN and the idea of training error.

We're interested in test set performance. Kaggle nicely provides training and test sets and is worth trying, so we'll go there.

In pairs, enter the [kaggle](http://www.kaggle.com/) [Titanic](http://www.kaggle.com/c/titanic-gettingStarted) competition. You have KNN handy, so try it. A very good starting point would be to use gender and passenger class. You may need to ensure that gender is numeric to get Euclidean distance from it. The main point here is to get a taste of kaggle and using a training and test set.

[Slides](slides.pdf) on evaluation procedures and metrics.


### Questions

 * You want to use KNN with a training set to eventually make predictions on new data. How will you choose K? (Describe a process that results in a choice for K.)
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### After

Optional:

 * Follow along with Wehrley's [soup to nuts kaggle Titanic solution](https://github.com/wehrley/wehrley.github.io/blob/master/SOUPTONUTS.md) which includes a lot of interesting commentary and plots as well. There's plenty on feature generation and dealing with missing data.
