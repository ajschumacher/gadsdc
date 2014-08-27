### Example solution: Naive Bayes spam classifier using sklearn


## READING FILES

# files downloaded from http://spamassassin.apache.org/publiccorpus/
# getting a list of filenames
import glob
easy_ham_files = glob.glob("easy_ham/*")
spam_files = glob.glob("spam/*")

# read the easy ham files into a list
easy_ham_text = []
for filename in easy_ham_files:
    with open(filename, 'rU') as f:
        easy_ham_text.append(f.read())

# read the spam files into a list
spam_text = []
for filename in spam_files:
    with open(filename, 'rU') as f:
        spam_text.append(f.read())

# combine the training data into a single list
ham_and_spam_text = easy_ham_text + spam_text


## COUNTVECTORIZER

# convert text into a matrix of token counts
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(decode_error="ignore")
vect.fit(ham_and_spam_text)
train = vect.transform(ham_and_spam_text)

# convert train to an array and examine it
train_arr = train.toarray()
train_arr.shape
sum(train_arr[0])

# store feature names and examine it
train_features = vect.get_feature_names()
len(train_features)
train_features[0]


## SIMPLE SUMMARIES

# summarize the data
import numpy as np
tokens_per_email = np.sum(train_arr, axis=1)    # sum of each row
count_per_token = np.sum(train_arr, axis=0)     # sum of each column

# find the most frequent token
np.max(count_per_token)
np.argmax(count_per_token)
count_per_token[np.argmax(count_per_token)]
train_features[np.argmax(count_per_token)]


## FIND THE HAMMIEST AND SPAMMIEST TOKENS

# create an array of the labels
train_label = [0]*len(easy_ham_text) + [1]*len(spam_text)
train_label_arr = np.array(train_label)

# calculate rate of each token in ham emails
ham_arr = train_arr[train_label_arr==0]
ham_count_per_token = np.sum(ham_arr, axis=0) + 1
ham_token_rate = ham_count_per_token.astype(float)/ham_arr.shape[0]
del(ham_arr)

# calculate rate of each token in spam emails
spam_arr = train_arr[train_label_arr==1]
spam_count_per_token = np.sum(spam_arr, axis=0) + 1
spam_token_rate = spam_count_per_token.astype(float)/spam_arr.shape[0]
del(spam_arr)

# for each token, calculate ratio of ham-to-spam
ham_to_spam_ratio = ham_token_rate/spam_token_rate
np.max(ham_to_spam_ratio)
train_features[np.argmax(ham_to_spam_ratio)]

# for each token, calculate ratio of spam-to-ham
spam_to_ham_ratio = spam_token_rate/ham_token_rate
np.max(spam_to_ham_ratio)
train_features[np.argmax(spam_to_ham_ratio)]


## MODEL BUILDING AND EVALUATION

# use cross-validation to assess Naive Bayes performance
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import cross_val_score
cross_val_score(MultinomialNB(), train, train_label_arr, cv=5,
                scoring="accuracy")
cross_val_score(MultinomialNB(), train, train_label_arr, cv=5,
                scoring="roc_auc")

# split into training and test sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(train, train_label,
                                                    test_size=0.4,
                                                    random_state=0)

# build Naive Bayes model and assess performance on test set
model = MultinomialNB().fit(X_train, y_train)
preds = model.predict(X_test)
from sklearn import metrics
metrics.accuracy_score(y_test, preds)
metrics.confusion_matrix(y_test, preds)
metrics.classification_report(y_test, preds)

# train model on all training data and predict on sample emails
test = vect.transform(["fork my GitHub repo", "buy a car"])
model = MultinomialNB().fit(train, train_label)
model.predict(test)

# train model on all training data and predict on hard ham
hard_ham_files = glob.glob("hard_ham/*")
hard_ham_text = []
for filename in hard_ham_files:
    with open(filename, 'rU') as f:
        hard_ham_text.append(f.read())
test = vect.transform(hard_ham_text)
model = MultinomialNB().fit(train, train_label)
preds = model.predict(test)
metrics.confusion_matrix([0]*len(preds), preds)
