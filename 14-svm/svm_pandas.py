### Example solution to SVM exercise

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, metrics, preprocessing
from sklearn.grid_search import GridSearchCV

# reading data into pandas and examining it
data_pd = pd.read_csv('data.csv')
data_pd
type(data_pd)
data_pd.describe()

# review of pandas series
data_pd.feature_1
data_pd['feature_1']
data_pd['feature_1'][0:5]
type(data_pd.feature_1)
data_pd.feature_1.shape
data_pd.feature_1.values
type(data_pd.feature_1.values)

# review of pandas dataframes
cols = ['feature_1', 'feature_2']
type(cols)
data_pd[cols]
data_pd[['feature_1', 'feature_2']]
type(data_pd[['feature_1', 'feature_2']])
data_pd[['feature_1', 'feature_2']].values

# series vs one-column dataframe
type(data_pd['feature_1'])
data_pd['feature_1'].shape
type(data_pd[['feature_1']])
data_pd[['feature_1']].shape

# creating X (2d array) and y (1d array) for sklearn
X = data_pd[cols].values
X = data_pd[data_pd.columns[0:2]].values
X.shape
y = data_pd.label.values
y.shape

# plotting
colors = np.where(data_pd.label==True, 'r', 'b')
plt.scatter(data_pd.feature_1, data_pd.feature_2, c=colors)
plt.scatter(X[:, 0], X[:, 1], c=y[:])

# train and predict on training set
clf = svm.SVC()
clf.fit(X, y)
predicted = clf.predict(X)
print metrics.accuracy_score(y, predicted)

# center and scale before training and predicting
X_scaled = preprocessing.scale(X)
clf.fit(X_scaled, y)
predicted = clf.predict(X_scaled)
print metrics.accuracy_score(y, predicted)

# grid search for optimal parameters
C_range = 10.0 ** np.arange(-2, 5)
gamma_range = 10.0 ** np.arange(-4, 5)
param_grid = dict(C=C_range, gamma=gamma_range)
grid = GridSearchCV(clf, param_grid, scoring='accuracy')
grid.fit(X_scaled, y)
grid.grid_scores_
grid.best_score_
grid.best_estimator_
grid.best_params_
