## `sklearn` and K Nearest Neighbors

```Python
from sklearn.datasets import load_iris
iris = load_iris()
```

This loads in one of most well-known toy datasets for machine learning. It's useful since it's very easy to get good performance on. Each row contains one flower instance with information on it's petal and sepal measurements. Its flower is classified into 1 of 3 species.

```Python
from sklearn import neighbors
X, y = iris.data, iris.target
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)

# What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
print iris.target_names[knn.predict([[3, 5, 4, 2]])]
```

`sklearn` has a very common interface for all it's models making it easy to use and switch between models.  The two major stages are 1) `fit` where we fit a model, or learn from the data and 2) `predict` where we extrapolate from what we learned.

### Cross Validation

```Python
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
predicted = knn.predict(X_test)
```

```Python
from sklearn import metrics
print metrics.classification_report(y_test, predicted)
print metrics.confusion_matrix(y_test, predicted)
print metrics.f1_score(y_test, predicted)
```

```Python
from sklearn.cross_validation import cross_val_score
scores = cross_val_score(knn, iris.data, iris.target, cv=5)
```
