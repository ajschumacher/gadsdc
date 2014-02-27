# TODO: Just logistic! Clean up!

# Logistic Regression and Naive Bayes Assignment

##The Problem

In this assignment we will tackle classification of comments on social media.  This is another Kaggle competition hosted by Impermium.  To quote from the Kaggle page: "The challenge is to detect when a comment from a conversation would be considered insulting to another participant in the conversation"

## The Data

There are only two major files in this assignment - again a training file which you will use, and a test set to submit predictions on.

1. [train.csv](https://www.dropbox.com/s/f6w2rukksx86rcf/train.csv)
2. [test.csv](https://www.dropbox.com/s/x5p07bfek3ll8xw/test.csv)

The training file will have both the text of the comment along with a column 'Insult'. which is 1 if it is an insult and 0 otherwise.

The original train and test files present many characters as their escape sequences. You may enjoy learning to deal with this yourself. You can also check out the `decode.py` script and `[train|test]-utf8.csv` files [here](https://github.com/arahuja/GADS4/tree/master/data/insults).

At the end you will submit **the probability of it being an insult** for the test file, in the format
```
Id, Insult
1234, 0.898
2345, 0.564
```

In R, you can get this by using predict(...., type='response') and in Python you can use model.predict_proba().

##Assignment
At any point in the following steps you can use your model to predict salaries on the final test set and submit. 
Some bullets have stars and rank from Basic (no star) to Challenging (3 stars)
* * - 1 star - Try these out but they will be harder
* ** - 2 stars - For those looking for a challenge or really explore the topic
* *** - 3 stars - Test out some of the ideas using different tools a

**NOTE: The following can be done with R or Python.  If you use R, you'll want to use TM to convert text into features.  In Python, you'll want to use CountVectorizer, or other feature converters available in sklearn.feature_extraction.**

1) Split the data into train and test. You will use one as your training set and the other for validation. Feel free to make multiple splits or use cross validation to make multiple splits

2) Build a logistic regression model to predict whether the comment is an insult.  Explore regularization again and how it effects your model.

You can use R - ( glm(...., family='binomial'), glmnet(..., family='binomial') ) or Python (sklearn.linear_model.LogisticRegression)

Use AUC to evaluate your model.

3) Build a Naive Bayes model on the same task.  Compare the performance with the logistic regression model

Use sklearn.naive_bayes.MultinomialNB

Try out different prior values and see how this effects performance.

Use AUC to evaluate your model.

*** 4) Try out Vowpal Wabbit to build a logistic regression model.

```sh
git clone git://github.com/JohnLangford/vowpal_wabbit.git
cd vowpal_wabbit
make install
```
Create a training file for vowpal wabbit using Python:
```sh
<Insult> | This is comment 1, no feature building needed
0 |c i really don't understand your point.\xa0 It seems that you are mixing apples and oranges.
0 |c Yeah and where are you now?
1 |c your such a dickhead...
```

This would work without editing the text at all, but you may want to remove stopwords, lowercase things and remove punctuation to clean it up.

Try the following:
```sh
vw -c -k train.vw --loss logistic -f model
vw -c -k train.vw --loss logistic -f model -l1 0.0001 ##for l1 loss
vw -c -k train.vw --loss logistic -f model -l2 0.0001 ## for l2 loss

vw -c -k -t test.vw -i model -p test.predictions
```

*** 5) Try out quadratic or cubic features in Vowpal Wabbit. 

```sh
vw -c -k train.vw --loss logistic -f model -q cc #makes quadaratic (all pairs of words) features for the 'c' feature namespace
vw -c -k train.vw --loss logistic -f model --cubic ccc #makes cubic (all triplets of words) features for the 'c' feature namespace

vw -c -k -t test.vw -i model -p test.predictions
```
