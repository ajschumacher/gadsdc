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


my.mean <- function(x) {
  return(sum(x)
         /
         length(x))
}

my.cov <- function(x, y) {
  return(sum((x - my.mean(x)) * (y - my.mean(y)))
         /
         (length(x)-1))
}

my.var <- function(x) {
  return(my.cov(x, x))
}

my.cor <- function(x, y) {
  return(my.cov(x, y)
         /
         (sqrt(my.var(x)) * sqrt(my.var(y))))
}


# Do not edit below this line

x <- rnorm(100)
y <- rnorm(100)

equal <- function(a, b) {
  return(isTRUE(all.equal(a, b)))
}

stopifnot(equal(my.mean(x), mean(x)))
stopifnot(equal(my.var(x), var(x)))
stopifnot(equal(my.cov(x, y), cov(x, y)))
stopifnot(equal(my.cor(x, y), cor(x, y)))
