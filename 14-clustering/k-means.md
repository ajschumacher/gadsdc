# TODO: Clean up! Integrate new homework!

# KMeans Clustering In Python

K-Means works in scikits just like the supervised learning algorithms.  We can follow the same paradigm of 

```Python
model = SomeModel( ... params ....)
model = model.fit( feature_matrix )
```

However, we won't be able to `predict` or `score` our model in the same way.  We don't necessarily have a training set or test set.  Kmeans is available in scikits-learn in the cluster package

The main parameter is `n_clusters` which tells us how many clusters to make.

```Python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=20) #Set the model to have 20 clusters
model = model.fit( data )

print model.labels_ # We can print out the cluster for each instance
```

##The Data

Of course, to do interesting clustering we need interesting data.  Up until now, we've worked mainly with CSV data that has been easy to import.  However, often its not the modeling part that is difficult (once we understand the models) but getting data into a format that we can use for modeling.

Today we'll look at 2 datasets from Amazon.  The first is a collection of movie reviews (the original set of 7 million reviews is also available) and the second is meta data on products including which customers reviewed it.  However, neither is in a ready-to-use format so we must work on that first.

### Amazon Movie Reviews

A limited version of this data is available here: https://www.dropbox.com/s/9uv12p0jhysd7st/movies.txt.small and the full data set is available here: http://snap.stanford.edu/data/web-Movies.html

1) The task here is to parse this file into a collection of product ids (ASIN) and review text.  The output should have on each line the id, followed by a list of reviews.  There should be one product per line and every line should have a unique product.

```Python Starter
#### Output
### product, ['review1', 'review2']

movie_reviews = dict()
for line in open('movies.txt.small'):
  pieces = line.split(':')
  if len(pieces) > 1:
    key = pieces[0]
    value = ':'.join(pieces[1:]).strip()
    if key == 'product/productId':
      id = value
    if key == 'review/text':
      movie_reviews.setdefault(id, []).append(value)
for movie, reviews in movie_reviews.items():
  print movie, reviews
```

### Amazon Product Data

A limited version of this data is available here: https://www.dropbox.com/s/bm5wpeqekdm8vil/amazon-meta.txt.small and the full data set is available here: http://snap.stanford.edu/data/amazon-meta.html

1) The task here is to parse this file into a collection of product ids (ASIN), title and list of customers (by id) who have reviewed the product.

**2) If you'd like create a review class that holds the customer id and star rating.  Use this to output a product id, title and list of reviews.

***3) Create a product class that holds the id, title and collection of reviews.


##KMeans

Now we can return to the clustering.  Either data set is available for clustering.  We can 
1) Cluster the movies by the text of their reviews.  We would send each review to CountVectorizer (TfidfVectorizer) to generate a feature matrix.
2) Cluster the products by who reviewed them.  (Here we will need to use DictVectorizer).  This clustering would be great without a lot of data, since the overlap will be sparse.

At the end if we have a list of titles or IDs we should be able to see what cluster they belong to

```Python
print sorted(zip(model.labels_ , titles))
```
