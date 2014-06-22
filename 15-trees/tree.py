#!/usr/bin/env python

# Based on: http://scikit-learn.org/dev/modules/tree.html

# The headache here is in order to get the tree viz working
# First, get a few things installed:
# A version of pyparsing that will install with pip and work:
#     pip install -Iv https://pypi.python.org/packages/source/p/pyparsing/pyparsing-1.5.7.tar.gz#md5=9be0fcdcc595199c646ab317c1d9a709
# (from http://stackoverflow.com/questions/15951748/pydot-and-graphviz-error-couldnt-import-dot-parser-loading-of-dot-files-will)
#     pip install pydot
# May also need to (brew) install graphviz

from sklearn.datasets import load_iris
from sklearn import tree
import StringIO
import pydot
from collections import Counter

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf.fit(iris.data, iris.target)

dot_data = StringIO.StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf('iris_dectree.pdf')

clf.predict(iris.data)

Counter(clf.predict(iris.data))
