"""Testing for K-means"""
import sys

import numpy as np
from scipy import sparse as sp

from sklearn.utils.testing import assert_equal
from sklearn.utils.testing import assert_array_equal, assert_array_almost_equal
from sklearn.utils.testing import assert_raises
from sklearn.utils.testing import assert_true
from sklearn.utils.testing import assert_greater

from sklearn.metrics.cluster import v_measure_score
from kmeans_exercise import KMeans, k_means, distance_function
from kmeans_exercise import _compute_labels_and_score
from sklearn.datasets.samples_generator import make_blobs
from sklearn.externals.six.moves import cStringIO as StringIO


# non centered, sparse centers to check the
centers = np.array([
    [0.0, 5.0, 0.0, 0.0, 0.0],
    [1.0, 1.0, 4.0, 0.0, 0.0],
    [1.0, 0.0, 0.0, 5.0, 1.0],
])
n_samples = 100
n_clusters, n_features = centers.shape
X, true_labels = make_blobs(n_samples=n_samples, centers=centers,
                            cluster_std=1., random_state=42)


def test_distance():
    x1 = np.array([1, 0])
    x2 = np.array([0,1])
    x1_x2_distance = distance_function(x1, x2)
    assert_equal(x1_x2_distance, np.sqrt(2))


    x1 = np.array([1, 0])
    x2 = np.array([0,0])
    x1_x2_distance = distance_function(x1, x2)
    assert_equal(x1_x2_distance, 1)


    x1 = np.array([4,5,2])
    x2 = np.array([7,2,9])
    x1_x2_distance = distance_function(x1, x2)
    assert_equal(x1_x2_distance, np.sqrt(67))


def test_labels_assignment_and_score():
    # pure numpy implementation as easily auditable reference gold
    # implementation
    rng = np.random.RandomState(42)
    noisy_centers = centers + rng.normal(size=centers.shape)
    labels_gold = - np.ones(n_samples, dtype=np.int)
    mindist = np.empty(n_samples)
    mindist.fill(np.infty)
    for center_id in range(n_clusters):
        dist = np.sqrt(np.sum((X - noisy_centers[center_id]) ** 2, axis=1))
        labels_gold[dist < mindist] = center_id
        mindist = np.minimum(dist, mindist)

    score_gold = mindist.sum()
    assert_true((mindist >= 0.0).all())
    assert_true((labels_gold != -1).all())

    # perform label assignment using the dense array input
    labels_array, score_array = _compute_labels_and_score(X, noisy_centers)
    assert_array_almost_equal(score_array, score_gold)
    assert_array_equal(labels_array, labels_gold)



def _check_fitted_model(km):
    # check that the number of cluster centers and distinct labels match
    # the expectation
    centers = km.cluster_centers_
    assert_equal(centers.shape, (n_clusters, n_features))

    labels = km.labels_
    assert_equal(np.unique(labels).shape[0], n_clusters)

    # check that the labels assignment are perfect (up to a permutation)
    assert_equal(v_measure_score(true_labels, labels), 1.0)
    assert_greater(km.score_, 0.0)


def test_k_means_check_fitted():
    km = KMeans(n_clusters=n_clusters, random_state=42)
    assert_raises(AttributeError, km._check_fitted)


def test_k_means_random_init():
    km = KMeans(n_clusters=n_clusters, random_state=42)
    km.fit(X)
    _check_fitted_model(km)


def test_predict():
    km = KMeans(n_clusters=n_clusters, random_state=42)

    km.fit(X)

    # sanity check: predict centroid labels
    pred = km.predict(km.cluster_centers_)
    assert_array_equal(pred, np.arange(n_clusters))

    # sanity check: re-predict labeling for training set samples
    pred = km.predict(X)
    assert_array_equal(pred, km.labels_)

    # re-predict labels for training set using fit_predict
    pred = km.fit_predict(X)
    assert_array_equal(pred, km.labels_)


def test_score():
    km1 = KMeans(n_clusters=n_clusters, n_init=1, max_iter=1, random_state=42)
    s1 = km1.fit(X).score(X)
    km2 = KMeans(n_clusters=n_clusters, max_iter=10, random_state=42)
    s2 = km2.fit(X).score(X)
    assert_greater(s2, s1)


def test_transform():
    km = KMeans(n_clusters=n_clusters)
    km.fit(X)
    X_new = km.transform(km.cluster_centers_)

    for c in range(n_clusters):
        assert_equal(X_new[c, c], 0)
        for c2 in range(n_clusters):
            if c != c2:
                assert_greater(X_new[c, c2], 0)


def test_n_init():
    """Check that increasing the number of init increases the quality"""
    n_runs = 5
    n_init_range = [1, 5, 10]
    score = np.zeros((len(n_init_range), n_runs))
    for i, n_init in enumerate(n_init_range):
        for j in range(n_runs):
            km = KMeans(n_clusters=n_clusters, n_init=n_init, random_state=j).fit(X)
            score[i, j] = km.score_

    score = score.mean(axis=1)
    failure_msg = ("Score %r should be decreasing"
                   " when n_init is increasing.") % list(score)
    for i in range(len(n_init_range) - 1):
        assert_true(score[i] >= score[i + 1], failure_msg)


def test_k_means_function():
    # test calling the k_means function directly
    # catch output
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        cluster_centers, labels, score = k_means(X, n_clusters=n_clusters,
                                                   verbose=True)
    finally:
        sys.stdout = old_stdout
    centers = cluster_centers
    assert_equal(centers.shape, (n_clusters, n_features))

    assert_equal(np.unique(labels).shape[0], n_clusters)

    # check that the labels assignment are perfect (up to a permutation)
    assert_equal(v_measure_score(true_labels, labels), 1.0)
    assert_greater(score, 0.0)
