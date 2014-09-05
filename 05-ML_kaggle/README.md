### Before

Read [A few useful things to know about machine learning](http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf). We're reading this paper now, and then again toward the end of the class; this is your first read through it.

Optional:

 * Go through Fortmann-Roe's [Understanding the Bias-Variance Tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html). This is perhaps a more readable introduction and covers KNN, which we're doing in class.


### Questions

 * What is the relationship between the terms "bias" and "variance" in the machine learning sense, and "accuracy" and "precision" in the measurement sense?
 * What is the relationship between correlation and causation?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

 * Briefly discuss the [No Free Lunch theorem](http://en.wikipedia.org/wiki/No_free_lunch_theorem) - and being slightly less pessimistic about choosing machine learning algorithms.
 * Briefly discuss the [curse of dimensionality](http://www.statsoft.com/Portals/0/blog/curse-of-dimensionality.jpg) and how it affects KNN, for example.

[Take a look](knn_iris_demo.Rmd) at applying KNN and the idea of training error.

We're interested in test set performance. Kaggle nicely provides training and test sets and is worth trying, so we'll go there.

In pairs, enter the [kaggle](http://www.kaggle.com/) [Titanic](http://www.kaggle.com/c/titanic-gettingStarted) competition. You have KNN handy, so try it. A very good starting point would be to use gender and passenger class. You may need to ensure that gender is numeric to get Euclidean distance from it. The main point here is to get a taste of kaggle and using a training and test set.

[Slides](slides.pdf) on evaluation procedures and metrics.

Note here, perhaps, the importance of optimizing the right thing. This relationship will be clearer with later models.

The `caret` package has a `confusionMatrix` function that calculates a lot of categorical evaluation metrics. The `pROC` package has `roc` and `auc` functions.

Implement 10-fold cross-validation for KNN classification accuracy. This should be a function that takes a training data set of features, the labels, and K. The function should return the accuracy arrived at by cross-validation. You could pretty easily extend this from 10-fold to n-fold. Think about how to generalize further. Test your function with some data! You can put your function in a `name.R` (or similar) file, in the `05-ML_kaggle` directory of the class repo.


### Questions

 * You want to use KNN with a training set to eventually make predictions on new data. How will you choose K? (Describe a process that results in a choice for K.)
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### After

Optional:

 * This [interactive visualization](http://www.navan.name/roc/) may help you to gain a better intuitive understanding of ROC curves and area under the curve (AUC).
 * Read [An introduction to ROC analysis](https://ccrma.stanford.edu/workshops/mir2009/references/ROCintro.pdf) for more on area under the ROC curve.
 * Follow along with Wehrley's [soup to nuts kaggle Titanic solution](https://github.com/wehrley/wehrley.github.io/blob/master/SOUPTONUTS.md) which includes a lot of interesting commentary and plots as well. There's plenty on feature generation and dealing with missing data.
 * Watch the [lecture videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) from *An Introduction to Statistical Learning* for more on the curse of dimensionality (chapter 2), the bias-variance trade-off (chapter 2), and model evaluation (chapter 5).
