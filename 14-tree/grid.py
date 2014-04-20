#!/usr/bin/env python

# sklearn's grid search functionality

from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier
from sklearn.grid_search import GridSearchCV

digits = load_digits()
tree = DecisionTreeClassifier()
params = {'criterion': ['gini', 'entropy']}
grid = GridSearchCV(tree, params)
grid.fit(digits.data, digits.target)

grid.grid_scores_
# etc.
