#!/usr/bin/env python

# A light statistical warm-up in Python

# Task: Implement these functions
# (without using the numpy built-ins)
#  * my_mean
#  * my_var
#  * my_cov
#  * my_cor
# So that this file can be run without error

import numpy as np

x, y = (np.random.randn(100) for _ in range(2))

assert(my_mean(x) == np.mean(x))
assert(my_var(x) == np.var(x))
assert(my_cov(x, y) == np.cov(x, y))
assert(my_cor(x, y) == np.cor(x, y))
