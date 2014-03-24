# A function to implement 1NN

nn <- function(train, labels, test) {
  apply(test, 1, function(x1) {
    labels[which.min(apply(train, 1, function(x2) sqrt(sum((x1-x2)^2))))]
  })
}

# For example
nn(iris[, 1:4], iris[, 5], iris[, 1:4])
