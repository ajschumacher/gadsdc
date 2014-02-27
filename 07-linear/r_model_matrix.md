# A note on consistent columns for modeling in R

R's formula syntax (`response ~ predictor` etc.) is a convenience, and especially so for categorical predictors. It hides the complexity of creating dummy variables. This is fine if you're only using one data set, but if you want to make a model with some data and then make predictions on other data then the convenience may not be, since the model needs to see data with the same columns - dummy columns included. If you have all the data in advance, you may be better off thinking of dummy variable creation as a substantive data manipulation step that should be done on all the data at once, before splitting to train and test sets, for example.

Here's what this could look like, specifically illustrated for the regression homework's "Category" field, which had a value in the test set that didn't appear in the small training set:

```R
# Read in separate train and test files
train <- read.csv("train.csv")
test <- read.csv("test.csv")

# Combine them for the column(s) we want to use as predictors in our model
all <- rbind(train[, "Category", drop=F],
             test[, "Category", drop=F])

# Explicitly construct all the dummy columns for the Category variable
allx <- model.matrix(~Category, data=all)

# Split out the training and test data, adding in the response variable as well
trainer <- cbind(as.data.frame(allx[1:10000,]), train[,"SalaryNormalized", drop=F])
tester <- cbind(as.data.frame(allx[10001:15000,]), data.frame(SalaryNormalized=NA))

# Now we can train and predict with our model, and we have no NA predictions
model <- lm(SalaryNormalized ~ . -1, data=trainer)
pred <- predict(model, tester)
```
