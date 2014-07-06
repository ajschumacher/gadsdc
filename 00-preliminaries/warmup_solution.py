#!/usr/bin/env python

# A light statistical warm-up in Python

# Task: Implement these functions
# (without using the numpy built-ins)
#  * my_mean
#  * my_var
#  * my_cov
#  * my_cor
# So that this file can be run without error

### YOUR CODE HERE


def my_mean(x):
  return (sum(x)
          /
          len(x))

def my_var(x):
  return (sum([(_ - my_mean(x))**2 for _ in x])
          /
          len(x))

def _sample_cov(x, y):
  return (sum([(xx - my_mean(x)) * (yy - my_mean(y))
               for xx, yy in zip(x, y)])
         /
         (len(x) - 1))

def my_cov(x, y):
  return [[_sample_cov(x, x), _sample_cov(x, y)],
          [_sample_cov(y, x), _sample_cov(y, y)]]

def my_cor(x, y):
  cor = (_sample_cov(x, y)
         /
         (_sample_cov(x, x)**0.5 * _sample_cov(y, y)**0.5))
  return [[1, cor],
          [cor, 1]]


# Do not edit below this line

import numpy as np

x, y = (np.random.randn(100) for _ in range(2))

def equal(a, b):
  np.testing.assert_allclose(a, b)

equal(my_mean(x), np.mean(x))
equal(my_var(x), np.var(x))
equal(my_cov(x, y), np.cov(x, y))
equal(my_cor(x, y), np.corrcoef(x, y))
