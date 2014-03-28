## TODO: update, move data, get complete test set (it's in the repo!), etc.


[Choosing a ML Classifier](http://blog.echen.me/2011/04/27/choosing-a-machine-learning-classifier/)

[Machine Learning Cheat Sheet (for scikit-learn)](http://peekaboo-vision.blogspot.com/2013/01/machine-learning-cheat-sheet-for-scikit.html)


##Predicting Bad Car Buys

###Problem:

This problem is based on http://www.kaggle.com/c/DontGetKicked.  Our goal is predict when a used car purchase is a poor purchase, or put more crudely, when we've bought a lemon.

Please work in groups of 1-3

Evaluate different models and configurations as well as different feature sets.

The goal is to get the highest AUC (on the test set)

### Data

- [training](https://github.com/arahuja/GADS7/blob/master/src/lesson10/inclass_training.csv)
- [test](https://github.com/arahuja/GADS7/blob/master/src/lesson10/inclass_test.csv)

- [data dictionary](https://github.com/arahuja/GADS7/blob/master/src/lesson10/data_dictionary.csv)
- [sample submission](https://github.com/arahuja/GADS7/blob/master/src/lesson10/submission.csv)

### Submission

Of the form:
```
RefId, IsBadBuy
1, 0.92
2, 0.4
4, .45
```

You can submit and score yourself here:
https://inclass.kaggle.com/c/ga-data-science-ny-7-review
