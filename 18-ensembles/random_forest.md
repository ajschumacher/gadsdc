# TODO: Clean this up!

# Ensemble Methods in Python
## With a focus on Random Forests

##Data
Again we will take a look at the twenty news groups dataset

```Python
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer

# Load the text data
categories = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]
twenty_train_subset = load_files('20news-bydate-train/', categories=categories, charset='latin-1')
twenty_test_subset = load_files('20news-bydate-test/', categories=categories, charset='latin-1')

# Turn the text documents into vectors of word frequencies
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(twenty_train_subset.data)
```

Previously, we had been using `CountVectorizer` to make a matrix of word counts, where each row is a document and each column is the word, the cell `matrix[document][word]` contains the count of `word` in `document`.

We can expand on this by setting the `ngram_range`.  This parameter allows us to set each column not only as a word, but possibly sequences of words

```Python
from sklearn.feature_extraction.text import CountVectorizer

#Creates a column for every possible word, length 2 sequence of words and length 3 sequence of words
vectorizer = CountVectorizer(ngram_range=(1,3))
X_train = vectorizer.fit_transform(twenty_train_subset.data)

```

Additionally, we also use a TF-IDF representation, which stands for Term Frequency - Inverse Document Frequency.

This value is the product of two intermediate values, the Term Frequency and the Inverse Document Frequency.

The Term Frequency is equivalent to the CountVectorizer features, the number of times or count that a word appear in the document.  This is our most basic representation of text.

To establish what Inverse Document Frequency, first let's define Document Frequency.  This is the % of documents that a particular word appears in.  For example, you could assume `the` appears in 100% of documents, while words like `Syria` would have low document frequency.  Inverse Document Frequency is simply 1 / Document Frequency (although frequently the log is also taken). 

Looking at our final term - Term Frequency * Inverse Document Frequency = Term Frequency / Document Frequency.  The intuition is that words that have high weight are though that either appear alot in this document or appear in very few other documents (somehow unique to this document).

```Python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(twenty_train_subset.data)
```

We can put this together with our other tricks as well.
```Python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', lowercase=True, ngram_range=(1,5))
X_train = vectorizer.fit_transform(twenty_train_subset.data)
```

##Random Forests

Random Forests are some of the most widespread classifiers used.  They are relatively simple to use (very few parameters to set and easy to avoid overfitting).  The only parameter we are really worried about is the number of trees we want to create - `n_estimators` in sklearn.

```
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=10)
model = model.fit(...)
```

We can use predict using our 20-newsgroup dataset above
```Python 
from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier

vectorizer = TfidfVectorizer(stop_words='english', lowercase=True, ngram_range=(1,1), min_df=1)
X_train = vectorizer.fit_transform(twenty_train_subset.data)


tree_model = DecisionTreeClassifier()
print cross_val_score(tree_model, X_train.toarray(), twenty_train_subset.target)

rf_model = RandomForestClassifier(n_estimators=10)
print cross_val_score(rf_model, X_train.toarray(), twenty_train_subset.target)
```
###Getting Important Features

As we saw before, getting information on what features we are using in Python can be difficult.  Each vectorizer has `get_feature_names` which we can use to tie back to our dataset.

Random Forests though (and Decision Trees) have a good way extracting what features are important.  Unlike we Logistic Regression, we don't have coeffcients that tell us relative impact.  But we can keep track of what features give us the best splits.

```Python
rf_model = RandomForestClassifier(n_estimators=10, compute_importances=True)

#This prints the top 10 most important features
print sorted(zip(rf_model.feature_importances_, vectorizer.get_feature_names()), reverse=True)[:10]
```
