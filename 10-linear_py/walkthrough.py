# Machine learning with sklearn

import pandas as pd

# Example data
data = pd.DataFrame({'score': [10, 4, 29],
                     'comment': ['it was okay',
                                 'it was so bad',
                                 'it was so good']})

# sklearn pattern example one
from sklearn.feature_extraction.text import CountVectorizer  # 1
vect = CountVectorizer()                                     # 2
vect.fit(data.comment)                                       # 3
train_matrix = vect.transform(data.comment)                  # 4
test_matrix = vect.transform(["kind of good"])               # 4
# check vect.get_feature_names() and .toarray() for sparse matrices

# sklearn pattern example two
from sklearn.linear_model import LinearRegression            # 1
model = LinearRegression()                                   # 2
model.fit(train_matrix, data.score)                          # 3
model.predict(test_matrix)                                   # 4
