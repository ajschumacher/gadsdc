# (This is a draft for now.)

head(model.matrix(~poly(Sepal.Length, 2), data=iris))
head(model.matrix(~poly(Sepal.Length, 2), data=iris))

pace <- read.csv("pace.csv")
plot(speed ~ pop, data=pace)
deg <- 2
m <- lm(speed ~ poly(pop, deg), data=pace)
m <- lm(speed ~ pop + I(pop^2), data=pace)
pops <- seq(1, 7, by=0.01)
predictions <- predict(m, data.frame(pop=x))
points(pops, predictions, type='l', col="blue")

X = model.matrix(~ poly(pop, 14), data=pace)
Y = pace$speed
library(glmnet)

m <- glmnet(X, Y, alpha=0)
plot(m, xvar='lambda')
m <- cv.glmnet(X, Y, alpha=0, nfolds=4)
plot(m)
m$lambda
popsX <- model.matrix(~ poly(pop, 14), data=data.frame(pop=pops))
predictions <- predict(m, popsX, s=m$lambda[100])
predictions <- predict(m, popsX, s='lambda.min')
