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

# Do not edit below this line

import numpy as np

x, y = (np.random.randn(100) for _ in range(2))

def equal(a, b):
  np.testing.assert_allclose(a, b)

equal(my_mean(x), np.mean(x))
equal(my_var(x), np.var(x))
equal(my_cov(x, y), np.cov(x, y))
equal(my_cor(x, y), np.corrcoef(x, y))
