# A quick demo to show evaluation metrics
# related to categorical data with confusion matrices

tooth <- ToothGrowth
truth <- tooth$supp

library(class)
set.seed(46)
predicted <- knn(tooth[-2], tooth[-2], truth, k=4)

library(caret)
confusionMatrix(predicted, truth)
