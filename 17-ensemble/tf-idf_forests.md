# Using tf-idf and random forests

## Newsgroups Data

We will take a look at some of the twenty newsgroups dataset, another common dataset for classification. Note that the data is fetched from 

```Python
from sklearn.datasets import fetch_20newsgroups

# We will use four of the twenty newsgroups
categories = ['alt.atheism',
              'talk.religion.misc',
              'comp.graphics',
              'sci.space']

twenty_train_subset = fetch_20newsgroups(subset='train', categories=categories)
twenty_test_subset = fetch_20newsgroups(subset='test', categories=categories)
```

Now we have lists of messages (as strings) in the `.data` members.


## tf-idf features

Here are some ways to generate features from the text:

```Python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Turn the text documents into vectors of word frequencies
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(twenty_train_subset.data)
```

This makes a matrix of word counts, where each row is a document and each column is the word, the cell `matrix[document, word]` contains the count of `word` in `document`.

We can expand on this by setting the `ngram_range`.  This parameter allows us to set each column not only as one word, but possibly sequences of words.

```Python
# Include every 1-gram, 2-gram, and 3-gram
vectorizer = CountVectorizer(ngram_range=(1,3))
X_train = vectorizer.fit_transform(twenty_train_subset.data)
```

Additionally, we could use a tf-idf representation, which stands for Term Frequency - Inverse Document Frequency.

This value is the product of two intermediate values, the Term Frequency and the Inverse Document Frequency.

The Term Frequency is equivalent to the CountVectorizer features, the number of times or count that a word appear in the document.  This is our most basic representation of text.

To establish Inverse Document Frequency, first let's define Document Frequency. This is the percentage of documents that a particular word appears in. For example, the word `the` might appear in 100% of documents, while words like `Syria` would likely have low document frequency. Inverse Document Frequency is simply 1 / Document Frequency (although often the log is also taken).

So tf-idf is Term Frequency * Inverse Document Frequency, or similar to Term Frequency / Document Frequency. The intuition is that words that have high weight are those that appear a lot in this document and/or appear in very few other documents (somehow unique to this document).

```Python
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(twenty_train_subset.data)
```

We can put this together with our other tricks as well.
```Python
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,5))
X_train = vectorizer.fit_transform(twenty_train_subset.data)
```

Question: How many features do these various methods produce?


## Random Forests

Random Forests are very popular ensemble classifiers. They are relatively simple to use (very few parameters to set and easy to avoid overfitting). The only parameter we are really worried about is the number of trees we want to create - `n_estimators` in sklearn.

```
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=10)
model.fit(...) # as usual
```

We can use predict using our 20-newsgroup dataset above

```Python 
from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier

vectorizer = TfidfVectorizer(stop_words='english')
X_train = vectorizer.fit_transform(twenty_train_subset.data)

tree_model = DecisionTreeClassifier()
print cross_val_score(tree_model, X_train.toarray(), twenty_train_subset.target)

rf_model = RandomForestClassifier(n_estimators=20)
print cross_val_score(rf_model, X_train.toarray(), twenty_train_subset.target)
```

### Getting Important Features

Random Forests can quantify the importance of features.  Unlike with logistic regression, we don't have coeffcients that tell us relative impact. But we can keep track of what features give us the best splits.

```Python
rf_model = RandomForestClassifier(n_estimators=10, compute_importances=True)
rf_model.fit(X_train.toarray(), twenty_train_subset.target)

# This prints the top 10 most important features
print sorted(zip(rf_model.feature_importances_, vectorizer.get_feature_names()), reverse=True)[:20]
```

Extensions:

 * Experiment with other options to the various pieces used here.
 * Evaluate performance for various models on the hold-out test set that was initially loaded.
 * Explore AdaBoost and other methods in the `sklearn.ensemble` module.
