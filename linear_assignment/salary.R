library(tm)
library(glmnet)

# A quick example, mostly to illustrate use of Dictionary

# Root Mean Squared Error (RMSE)
rmse <- function(predicted, actual) {
  return(sqrt(mean((predicted-actual)^2)))
}

# Load in data
alltrain <- read.csv("train.csv", as.is=TRUE)
alltest <- read.csv("test.csv", as.is=TRUE)
solution <- read.csv("solution.csv", as.is=TRUE)

# Setting up as if for cross-validation,
# but just running through one train/test
set.seed(42)
folds <- sample(10, nrow(alltrain), replace=TRUE)
fold <- 1

train <- subset(alltrain, folds != fold)
test <- subset(alltrain, folds == fold)
corpus <- Corpus(VectorSource(train$Title))
tdm <- DocumentTermMatrix(corpus, list(stopwords = TRUE,
                                       removePunctuation = TRUE,
                                       removeNumbers = TRUE,
                                       bounds = list(global = c(5,Inf))))
design_matrix <- as.matrix(tdm)
model <- lm(SalaryNormalized ~ ., data=data.frame(cbind(SalaryNormalized=train$SalaryNormalized,
                                                        design_matrix)))
test_corpus <- Corpus(VectorSource(test$Title))
test_tdm <- DocumentTermMatrix(test_corpus, list(stopwords = TRUE,
                                                 removePunctuation = TRUE,
                                                 removeNumbers = TRUE,
                                                 dictionary=Dictionary(tdm)))
test_design_matrix <- as.matrix(test_tdm)
predictions <- predict(model, as.data.frame(test_design_matrix))
#rmse(predictions, test$SalaryNormalized)

# "rank deficient fits" when two or more terms only occur together
#sum(is.na(coef(model)))

# Note that it's also possible to do bigrams etc.

# Let's try L1 regularization
lasso.model <- cv.glmnet(design_matrix, train$SalaryNormalized, alpha=1)
predictions <- predict(lasso.model, test_design_matrix, s='lambda.min')
#rmse(predictions, test$SalaryNormalized)
