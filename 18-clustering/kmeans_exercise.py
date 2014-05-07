"""
K-means clustering implementation exercise
KMeans code based on sklearn/clustering/k_means_.py
"""

import numpy as np
from sklearn.utils import check_random_state
from sklearn.utils.fixes import bincount
from sklearn.metrics.pairwise import euclidean_distances


""" Takes two vectors v1, v2 and tells us the distance between them
    Basic impl: Euclidean Distance =
          sum of squared distances =
          SUM_over_i ( (v2[i] - v2[i]) ^ 2 )
"""
def distance_function(v1, v2):
  #TODO: IMPLEMENT
  # Write a function to compute the euclidean
  # distance between two vectors, v1 and v2
  return 0


def _compute_labels_and_score(X, centers):
    """
    Compute the labels and the current score of the given samples and centers

    Parameters
    ----------
    X: float64 array-like or CSR sparse matrix, shape (n_samples, n_features)
        The input samples to assign to the labels.

    centers: float64 array, shape (k, n_features)
        The cluster centers.

    Returns
    -------
    labels: int array of shape(n)
        The resulting assignment

    score: float
        The value of the score criterion with the assignment
        The score (sum of squared distances to the centers).
    """
    n_clusters = centers.shape[0]
    n_samples = X.shape[0]
    score = 0.0

    # set the default value of labels to -1 to be able to detect errors
    labels = np.ones(n_samples, np.int32)
    #TODO: IMPLEMENT
        # Iterate over the samples and the clusters
        # Compute the distance between samples and cluster center
        # Check if the cluster center is closer than any other cluster center
        # Save the closest cluster center
        # SCORE is the  SUM of distances from point to closest center
        # So once we've found the closest center, add the distance to score

    return labels, score


def _recompute_centers( X, labels, n_clusters):
    """
    Computation of cluster centers / means.

    Parameters
    ----------
    X: array-like, shape (n_samples, n_features)

    labels: array of integers, shape (n_samples)
        Current label assignment

    n_clusters: int
        Number of desired clusters

    Returns
    -------
    centers: array, shape (n_clusters, n_features)
        The resulting centers
    """

    n_samples = X.shape[0]
    n_features = X.shape[1]
   
    # Initialize centers to all zero
    centers = np.zeros((n_clusters, n_features))
    n_samples_in_cluster = bincount(labels, minlength=n_clusters)

    # Compute a center for each label
    # For each label, average over samples and features
    # TODO: IMPLEMENT
        # Take all of the samples in a cluster and average their features

    return centers


def k_means(X, n_clusters,
            n_init=10, max_iter=10, verbose=False,
            tol=1e-4, random_state=None):
    """
    K-means clustering algorithm.

    Parameters
    ----------
    X : array-like or sparse matrix, shape (n_samples, n_features)
        The observations to cluster.

    n_clusters : int
        The number of clusters to form as well as the number of
        centroids to generate.

    max_iter : int, optional, default 300
        Maximum number of iterations of the k-means algorithm to run.

    n_init : int, optional, default: 10
        Number of time the k-means algorithm will be run with different
        centroid seeds. The final results will be the best output of
        n_init consecutive runs in terms of score.

    tol : float, optional
        The relative increment in the results before declaring convergence.

    verbose : boolean, optional
        Verbosity mode.

    random_state : integer or numpy.RandomState, optional
        The generator used to initialize the centers. If an integer is
        given, it fixes the seed. Defaults to the global numpy random
        number generator.

    Returns
    -------
    centroid : float ndarray with shape (k, n_features)
        Centroids found at the last iteration of k-means.

    label : integer ndarray with shape (n_samples,)
        label[i] is the code or index of the centroid the
        i'th observation is closest to.

    score : float
        The final value of the score criterion (sum of squared distances to
        the closest centroid for all observations in the training set).

    """
    random_state = check_random_state(random_state)
    best_labels, best_score, best_centers = None, None, None

    # We are going to do `n_init` random starts and return the best one
    for it in range(n_init):
        # run k-means once
        labels, score, centers = _kmeans_single(X, n_clusters, max_iter=max_iter, 
          verbose=verbose, random_state=random_state)
        # determine if these results are the best so far
        # If so, update best_centers, best_labels, best_score
        # TODO: IMPLEMENT

    return best_centers, best_labels, best_score


def _kmeans_single(X, n_clusters, max_iter=10, verbose=False, random_state=None):
    """A single run of k-means, assumes preparation completed prior.

    Parameters
    ----------
    X: array-like of floats, shape (n_samples, n_features)
        The observations to cluster.

    n_clusters: int
        The number of clusters to form as well as the number of
        centroids to generate.

    max_iter: int, optional, default 10
        Maximum number of iterations of the k-means algorithm to run.

    verbose: boolean, optional
        Verbosity mode

    random_state: integer or numpy.RandomState, optional
        The generator used to initialize the centers. If an integer is
        given, it fixes the seed. Defaults to the global numpy random
        number generator.

    Returns
    -------
    centroid: float ndarray with shape (k, n_features)
        Centroids found at the last iteration of k-means.

    label: integer ndarray with shape (n_samples,)
        label[i] is the code or index of the centroid the
        i'th observation is closest to.

    score: float
        The final value of the score criterion (sum of squared distances to
        the closest centroid for all observations in the training set).
    """
    random_state = check_random_state(random_state)

    best_labels, best_score, best_centers = None, None, None
    # init
    centers = _init_random_centroids(X, n_clusters, random_state=random_state)
    if verbose:
        print('Initialization complete')

    for i in range(max_iter):
        # Figure out the labels, given the centers
        labels, score = _compute_labels_and_score(X, centers)

        # Recompute the centers given the labels and data
        centers = _recompute_centers(X, labels, n_clusters)

        # Is this run better than the last run?
        # If so, update best_centers, best_labels, best_score
        # TODO: IMPLEMENT

    return best_labels, best_score, best_centers


def _init_random_centroids(X, k, random_state=None):
    """
    Compute the initial centroids

    Parameters
    ----------

    X: array, shape (n_samples, n_features)

    k: int
        number of centroids

    random_state: integer or numpy.RandomState, optional
        The generator used to initialize the centers. If an integer is
        given, it fixes the seed. Defaults to the global numpy random
        number generator.

    Returns
    -------
    centers: array, shape(k, n_features)
    """
    random_state = check_random_state(random_state)
    n_samples = X.shape[0]

    seeds = random_state.permutation(n_samples)[:k]
    centers = X[seeds]

    return centers


class KMeans():
    """K-Means clustering

    Parameters
    ----------

    n_clusters : int, optional, default: 8
        The number of clusters to form as well as the number of
        centroids to generate.

    max_iter : int
        Maximum number of iterations of the k-means algorithm for a
        single run.

    n_init : int, optional, default: 10
        Number of time the k-means algorithm will be run with different
        centroid seeds. The final results will be the best output of
        n_init consecutive runs in terms of score.

    random_state : integer or numpy.RandomState, optional
        The generator used to initialize the centers. If an integer is
        given, it fixes the seed. Defaults to the global numpy random
        number generator.

    Attributes
    ----------
    `cluster_centers_` : array, [n_clusters, n_features]
        Coordinates of cluster centers

    `labels_` :
        Labels of each point

    `score_` : float
        The value of the score criterion associated with the chosen
        partition.

   """

    def __init__(self, n_clusters=8, n_init=10, max_iter=10, verbose=0, random_state=None):

        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.n_init = n_init
        self.verbose = verbose
        self.random_state = random_state

    def _check_fit_data(self, X):
        """Verify that the number of samples given is larger than k"""
        if X.shape[0] < self.n_clusters:
            raise ValueError("n_samples=%d should be >= n_clusters=%d" % (
                X.shape[0], self.n_clusters))
        return X

    def _check_test_data(self, X):
        n_samples, n_features = X.shape
        expected_n_features = self.cluster_centers_.shape[1]
        if not n_features == expected_n_features:
            raise ValueError("Incorrect number of features. "
                             "Got %d features, expected %d" % (
                                 n_features, expected_n_features))

        return X

    def _check_fitted(self):
        if not hasattr(self, "cluster_centers_"):
            pass # No problem!
            # raise AttributeError("Model has not been trained yet.")
            # TODO: Make this work right again.

    def fit(self, X, y=None):
        """Compute k-means clustering.

        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
        """
        random_state = check_random_state(self.random_state)
        X = self._check_fit_data(X)

        self.cluster_centers_, self.labels_, self.score_ = k_means(
            X, n_clusters=self.n_clusters, n_init=self.n_init,
            max_iter=self.max_iter, verbose=self.verbose, random_state=random_state)
        return self

    def fit_predict(self, X):
        """Compute cluster centers and predict cluster index for each sample.

        Convenience method; equivalent to calling fit(X) followed by
        predict(X).
        """
        return self.fit(X).labels_

    def transform(self, X, y=None):
        """Transform X to a cluster-distance space

        In the new space, each dimension is the distance to the cluster
        centers.  Note that even if X is sparse, the array returned by
        `transform` will typically be dense.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            New data to transform.

        Returns
        -------
        X_new : array, shape [n_samples, k]
            X transformed in the new space.
        """
        self._check_fitted()
        X = self._check_test_data(X)
        return euclidean_distances(X, self.cluster_centers_)

    def predict(self, X):
        """Predict the closest cluster each sample in X belongs to.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            New data to predict.

        Returns
        -------
        labels : array, shape [n_samples,]
            Index of the cluster each sample belongs to.
        """
        self._check_fitted()
        X = self._check_test_data(X)
        return _compute_labels_and_score(X, self.cluster_centers_)[0]

    def score(self, X):
        """Opposite of the value of X on the K-means objective.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            New data.

        Returns
        -------
        score : float
            Opposite of the value of X on the K-means objective.
        """
        self._check_fitted()
        X = self._check_test_data(X)
        return -_compute_labels_and_score(X, self.cluster_centers_)[1]
