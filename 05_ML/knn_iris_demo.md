# TODO: Clean up!

# KNN Iris Walkthrough

```R
iris

head(iris) #preview the dataset

summmary(iris) #get overview of the data

library('class') #load classification library
knn #display knn source

data <- iris
N <- nrow(data)

train.pct <- .7 #set train/tet split at 70%
train.index <- sample(1:N,  train.pct* N)  #randomly sample indices for your training set

train.data <- data[train.index, ] #separate out those indices to your traing set
test.data <- data[-train.index, ] #everything else goes to your test set
test.labels <- test.data$Species
#TRAIN YOUR MODEL (k = 3, but you could set it as anything)
test.predict <- knn( train = train.data[,c(1,2,3,4)] , test = test.data[,c(1,2,3,4)], cl = train.data$Species, k = 3)

#PRINT CONFUSION MATRIX
print(table(test.data$Species, test.labels))

#OUTPUT ACCURACY
 1 - (sum ( test.data$Species != test.labels ) / nrow(test.data))

```

Also here is a script that does much of the above, but iterates over different values of k.
