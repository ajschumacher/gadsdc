# TODO: use to show the python way of doing many things

# A simple solution to the Logistic Regression and Naive Bayes assignment

Here is a simple solution to [the logistic regression and naive Bayes assignment](https://github.com/arahuja/GADS4/wiki/Logistic-Regression-and-Naive-Bayes-Assignment). It uses almost entirely code simply copied and pasted from class materials.

Get the cleaned-up data files from [the class repo](https://github.com/arahuja/GADS4/tree/master/data/insults):

```bash
wget https://github.com/arahuja/GADS4/raw/master/data/insults/train-utf8.csv
wget https://github.com/arahuja/GADS4/raw/master/data/insults/test-utf8.csv
```

We need to load the files into Python. Use the pandas code from [the Python handout](https://github.com/arahuja/GADS4/wiki/Python-Basics):

```python
import pandas as pd
train = pd.read_csv('train-utf8.csv')
test = pd.read_csv('test-utf8.csv')
```

We'll process the text into numeric features with a CountVectorizer. The code comes again from [the Python handout](https://github.com/arahuja/GADS4/wiki/Python-Basics):

```python
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train.Comment)
X_test = vectorizer.transform(test.Comment)
```

To get our models going, we bring in the relevant things from sklearn. Code comes from [the Python handout](https://github.com/arahuja/GADS4/wiki/Python-Basics) and [a class log](https://raw.github.com/arahuja/GADS4/master/RSessions/lesson7.log):

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
```

We want to check performance by scoring with AUC. Code is from [the Python handout](https://github.com/arahuja/GADS4/wiki/Python-Basics) and the first google result for 'sklearn auc score':

```python
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import auc_score
cross_val_score(MultinomialNB(), X_train, train.Insult, score_func=auc_score)
cross_val_score(LogisticRegression(), X_train, train.Insult, score_func=auc_score)
```

Having evaluated performance, we can make and use a model. Code comes again from [the Python handout](https://github.com/arahuja/GADS4/wiki/Python-Basics):

```python
model = MultinomialNB().fit(X_train, list(train.Insult))
predictions = model.predict_proba(X_test)[:,1]
```

And then we can write this out using pandas:

```python
submission = pd.DataFrame({'id': test.id, 'insult': predictions})
submission.to_csv('submission.csv', index=False)
```

This simple naive Bayes submission scores AUC of 0.7359 on the test set.
