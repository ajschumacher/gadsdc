#!/usr/bin/env python

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

data = pd.read_csv('../14-svm/data.csv')

pipeline = Pipeline([('scale', StandardScaler()),
                     ('svm',   SVC()           )])

pipeline.fit(data[[0, 1]], data.label)

# Accuracy on training data
print pipeline.score(data[[0, 1]], data.label)
