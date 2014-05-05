#!/usr/bin/env python

from __future__ import division
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier

X = pd.read_csv('pure_spectra_matrix.csv', sep=';', header=None)

# A bit sparse
print 'fraction non-zero:', (X!=0).sum().sum() / np.prod(X.shape)

Y = pd.read_csv('pure_spectra_metadata.csv', sep=';')

Y['gram'] = map(lambda x: x.split('.')[0] in
                          ['QWP', 'VVJ', 'QBG', 'RTO'],
                Y.Species)

# About 31% gram positive
print 'fraction gram positive:', np.mean(Y.gram)

tree = DecisionTreeClassifier(max_depth=1)
tree.fit(X, Y.gram)
print 'stump accuracy on all data:', tree.score(X, Y.gram)

pca = PCA(n_components=1)
X1 = pca.fit_transform(X)
tree.fit(X1, Y.gram)
print 'stump accuracy on one principal component', tree.score(X1, Y.gram)
