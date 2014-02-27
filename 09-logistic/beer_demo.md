# TODO: clean up!

##Logistic Regression in R

First let's start as always by loading some data
```R
beer <- read.csv('http://www-958.ibm.com/software/analytics/manyeyes/datasets/af-er-beer-dataset/versions/1.txt', header=TRUE, sep='\t')
head(beer)
```

This data is the beer ratings dataset used in on the assignments.  We want to turn this into a classification problem, to label beers as GOOD or BAD.  How do we define those?  In this case we are going to say the top-rated beers are GOOD are others are BAD.

```R
summary(beer$WR)
beer$good <- (beer$WR > 4.3)
```

We also want to build some relevant features, things we might think relate to that.  We could use the 'Type' field, but we saw that that field was fairly granular, so let's extract some large categories from it.

```R
beer$Ale <- grepl('Ale', beer$Type)
beer$IPA <- grepl('IPA', beer$Type)
beer$Stout <- grepl('Stout', beer$Type)
beer$Lager <- grepl('Lager', beer$Type)

head(beer)
```

Let's use these elements to see if we can classify our beers as GOOD or BAD.

```R
model <- glm(good ~ Ale + Stout + IPA + Lager, data=beer, family='binomial')
```

The new value here is `family`.  This defines how to interpret our output variable. In linear regressions we interpreted as Gaussian or Normal, which is the default family.


Next, we'll want to build training and test sets to see how well we can predict.

```R
train.idx <- sample(1:nrow(beer), .7*nrow(beer))
training <- beer[train.idx,]
test <- beer[-train.idx,]

model <- glm(good ~ Ale + Stout + IPA + Lager, data=training, family='binomial')

```

We can build a model on the training set and predict on the test, but how do we measure success?

One measure is accuracy, another precision.  R has these built into the ROCR package.

```R
install.packages('ROCR')
library('ROCR')

pred <- prediciton(test.predict, test$good) 
perf <- performance(pred, measure='acc') #Simple accuracy, what % were right?

perf <- performance(pred, measure='prec') #What % of the elements I predicted to be in the class actually?
perf <- performance(pred, measure='recall') #What % of the elements that are in class, did I predict to be in this class?

perf <- performance(pred, measure='f') #F-measure a balance between them
perf <- performance(pred, measure='auc') #Area Under the Curve, another way to balance them

```
