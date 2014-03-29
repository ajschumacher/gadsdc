# TODO: clean up, consider merging with other file(s)

# More basics for regression homework

```R

# This is the directory all this stuff is in - on my machine.
# Won't be the same for others.
setwd("~/regress/")


# define Mean Absolute Error
mae <- function(one, other) {
  return(mean(abs(one - other)))
} # Make a note about R scoping!

# Check a simple case:
mae(5, 2)
# This is a simple form of testing:
stopifnot(mae(5, 2)==3)


# Note that our train/test split is not the global train/test split
alltrain <- read.csv("train.csv")

# Randomly select fold assignments for n-fold cross-validation
set.seed(42)
alltrain$fold <- sample(1:10, nrow(alltrain), replace=TRUE)

# We can do this here for convenience, or not
train <- subset(alltrain, fold != 3)
test  <- subset(alltrain, fold == 3)

# What is the dumbest model we could do?
# Let's predict every salary is 0. (Note, there is no training step here.)
mae(0, train$SalaryNormalized)
mae(0,  test$SalaryNormalized)
# Why are they different? What do they mean? Will they change for different folds?
# Look at the distribution of the data.

# What's the second-dumbest model we could do?
model <- lm(SalaryNormalized ~ 1, data=train)
# Without looking - what's the coefficient? Why?

# Training error:
mae(fitted(model), train$SalaryNormalized)
# This is a big improvement!

# Test (our test, or cross-validation) error:
mae(predict(model, test), test$SalaryNormalized)
# This will (almost always) be worse than training error.


# How consistent is the error?

error_from_fold <- function(n) {
  model <- lm(SalaryNormalized ~ 1, data=subset(alltrain, fold != n))
  test <- subset(alltrain, fold == n)
  error <- mae(predict(model, test), test$SalaryNormalized)
  return(error)
}

# Let's look at all the folds
sapply(1:10, error_from_fold)
# Why are these different? Are they very different?
mean(sapply(1:10, error_from_fold))


# Finally, we need to work with the actual test data
realtest <- read.csv("test.csv")

# We should train our final model with all the training data
finalmodel <- lm(SalaryNormalized ~ 1, data=alltrain)

predictions <- predict(finalmodel, realtest)
# What are these predictions going to be?

# Put the submission together and write it to a file
submission <- data.frame(Id=realtest$Id,
                         Salary=predictions)
write.csv(submission, "my_submission.csv", row.names=FALSE)


# Note this difference between lm/glm and glmnet:
# glmnet only takes numeric data!

# This works with lm because R auto-dummies the categorical field:
model <- lm(SalaryNormalized ~ ContractType, data=train)
# By the way, will this have better or worse loss than the constant model?

# This does NOT work because glmnet does not auto-dummy:
library(glmnet)
model <- cv.glmnet(matrix(train$ContractType), matrix(train$SalaryNormalized))
# FAIL

# You have to do this (or something with the same effect):
model <- cv.glmnet(model.matrix(~train$ContractType), matrix(train$SalaryNormalized))
# Be aware of the cross-validation that's happening here! It is not yours!
as.vector(predict(model, model.matrix(~test$ContractType), s="lambda.min"))


# Look again at distribution of salaries in train. Look. Again.

# Re-doing with log trainsform...
model <- lm(log(SalaryNormalized) ~ 1, data=train)

# Training error:
mae(exp(fitted(model)), train$SalaryNormalized)
# Test (our test, or cross-validation) error:
mae(exp(predict(model, test)), test$SalaryNormalized)
# This is a substantial improvement!
```
