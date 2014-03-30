# TODO: Update!

# Regression and Regularization

##Loading in data

Let's return to the baseball salary datasets.

```R
batting <- read.csv('path/to/Batting.csv')
salary <- read.csv('path/to/Salaries.csv')
master <- read.csv('path/to/Master.csv')
```

Let's combine these together so all the information is one data frame.

```R
batting_salary <- merge(batting, salary)
data <- merge(master, batting_salary)
```

Next, we'll take a smaller slice of the dataset, this is to easily weed out NA values which might be troublesome for R.
```R
model_data <- data[, c('HR', 'RBI', 'R', 'G', 'height', 'weight', 'salary', 'yearID')]
model_data <- model_data[complete.cases(model_data),] #This removes any rows that had an NA value
```

Now let's build a training set and a test set.  We want to predict salaries for baseball players in 2012 based on previous historical data.

```R
training <- model_data[model_data$yearID == 2011,]
test <- model_data[model_data$yearID == 2012,]
```
We can build a simple model using `lm`.  How do we evaluate it?  Two common techniques are Mean Absolute Error and Mean Squared Error

```R
mae <- function(x,y)
{
    sum( abs(x-y) ) /length(x)
{

mse <- function(x,y)
{
    sum( (x-y)^2 ) /length(x)
{
```

Let's build a variety of models and test their predictions on the held-out set
```R
model1 <- lm(salary ~ HR + RBI + weight + height, data=training)
model2 <- lm(salary ~ HR + RBI + weight + height + R, data=training)

test.predict1 <- predict(model1, test) #Predict using the first model
test.predict2 <- predict(model2, test) #Predict using the model that added in R (Runs)

mae(test.predict1, test$salary)
mse(test.predict1, test$salary)

mae(test.predict2, test$salary)
mse(test.predict2, test$salary)
```

##Using GLMnet

First we have to install and load it.
```R
install.packages('glmnet')
library('glmnet')
```
This let's us build a regularized regression model over different values of lambda (the value that balances lasso and ridge regression)

```R
model.reg <- glmnet( as.matrix(training[,c('HR', 'RBI', 'G', 'R')]), as.matrix(training['salary']) )

#We can also use cross validation
model.regcv <- cv.glmnet( as.matrix(training[,c('HR', 'RBI', 'G', 'R')]), as.matrix(training['salary']) )

test.predict.reg <- predict(model.reg, as.matrix(test[,c('HR', 'RBI', 'G', 'R')]))

test.predict.regcv <- predict(model.reg, as.matrix(test[,c('HR', 'RBI', 'G', 'R')]), s=model.regcv$lambda.min)
mae(test.predict.regcv, test$salary)
mse(test.predict.regcv, test$salary)

coef(model.regcv, s="lambda.min")
print(model.regcv)
```
