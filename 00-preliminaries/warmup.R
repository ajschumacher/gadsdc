#!/usr/bin/env Rscript

# A light statistical warm-up in R

# Task: Implement these functions
# (without using the R built-ins)
#  * my.mean
#  * my.var
#  * my.cov
#  * my.cor
# So that this file can be run without error.

### YOUR CODE HERE

# Do not edit below this line

x <- rnorm(100)
y <- rnorm(100)

'%==%' <- function(x, y)
{ result = isTRUE(all.equal(x, y)) }

stopifnot(my.mean(x) == mean(x))
stopifnot(my.var(x) == var(x))
stopifnot(my.cov(x, y) == cov(x, y))
stopifnot(my.cor(x, y) == cor(x, y))
