## Naive Bayes and Logistic Regression in `sklearn`

This uses a [data set](https://github.com/ajschumacher/gadsdata/tree/master/insults) of comments that are identified as insults or not. Some of the comments are very insulting - don't read the comments if you would rather not.

```Python
import pandas as pd
train = pd.read_csv('../../gadsdata/insults/train.csv')
test = pd.read_csv('../../gadsdata/insults/test.csv')
```

We'll process the text into numeric features with a CountVectorizer.

```Python
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train.Comment)
X_test = vectorizer.transform(test.Comment)
```

To get our models going, we bring in the relevant things from sklearn.

```Python
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
```

We want to check performance by scoring with AUC.

```Python
from sklearn.cross_validation import cross_val_score
cross_val_score(MultinomialNB(), X_train, train.Insult, scoring="roc_auc")
cross_val_score(LogisticRegression(), X_train, train.Insult, scoring="roc_auc")
```

Having evaluated performance, we can make and use a model.

```Python
model = MultinomialNB().fit(X_train, list(train.Insult))
predictions = model.predict_proba(X_test)[:,1]
```

You could write out predictions using `pandas` if needed:

```Python
submission = pd.DataFrame({'id': test.id, 'insult': predictions})
submission.to_csv('submission.csv', index=False)
```

See also this blog post: [Recap of my first Kaggle Competition: Detecting Insults in Social Commentary](http://peekaboo-vision.blogspot.com/2012/09/recap-of-my-first-kaggle-competition.html)
