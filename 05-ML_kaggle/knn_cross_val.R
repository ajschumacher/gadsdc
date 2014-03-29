library(class)

accuracy_for_k <- function(data, labels, k) {
  n <- 10
  chunks <- sample(n, nrow(data), replace=TRUE)
  accs <- sapply(1:n, function(chunk) {
    test <- data[chunk == chunks, ]
    test.labels <- labels[chunk == chunks]
    train <- data[chunk != chunks, ]
    train.labels <- labels[chunk != chunks]
    preds <- knn(train, test, train.labels, k)
    return(mean(preds == test.labels))
  })
  return(mean(accs))
}

accs <- sapply(1:30, function(i) accuracy_for_k(iris[, 1:4], iris[, 5], i))

library(ggplot2)
qplot(1:30, accs) + geom_smooth()
