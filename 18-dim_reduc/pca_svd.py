
import numpy as np
%pylab

# 1) Set up some data and look at it a little

x1 = np.random.normal(loc=40, scale=8, size=100)
x2 = x1 - 10 + np.random.normal(scale=3, size=100)
scatter(x1, x2)

X = np.column_stack((x1, x2))
X.shape

X.mean(axis=0)
X_centered = X - X.mean(axis=0)

np.cov(X, rowvar=0)
np.cov(X_centered, rowvar=0)

np.dot(X.T, X)
np.dot(X_centered.T, X_centered)
np.dot(X_centered.T, X_centered)/99 # unimportant scaling


# 2) Do some PCA

eig_vals, Q = np.linalg.eig(np.cov(X_centered, rowvar=0)*99)
np.dot(Q, np.dot(np.diag(eig_vals), np.linalg.inv(Q)))
np.cov(X_centered, rowvar=0)*99

ordered = sorted(zip(eig_vals, Q.T), reverse=True)
eig_vals = np.array([_[0] for _ in ordered])
Q = np.column_stack((_[1] for _ in ordered))

X_transformed = np.dot(Q[:, 0].reshape(2, 1).T, X_centered.T)

X_reconstituted = np.dot(X_transformed.reshape(100, 1),
                         Q[:, 0].reshape(1, 2))

scatter(X_centered[:, 0], X_centered[:, 1])
scatter(X_reconstituted[:, 0], X_reconstituted[:, 1], c='r')


# 3) Do some SVD

U, singular_vals, V_T = np.linalg.svd(X_centered)
Sigma = np.zeros((100, 2))
Sigma[:2, :2] = np.diag(singular_vals)
np.dot(U, np.dot(Sigma, V_T))[:5, :]
X_centered[:5, :]

singular_vals**2
eig_vals

np.dot(U[:,0].reshape(100, 1), Sigma[0, 0])[:5]
X_transformed[:, :5]

np.dot(U[:,0].reshape(100, 1), Sigma[0, 0]).dot(V_T[0, :].reshape(1, 2))[:5, :]
X_reconstituted[:5, :]

# (But also, U and V themselves.)
