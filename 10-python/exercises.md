# Python exercises

###Lahman Baseball Dataset

Available here: [Lahman Baseball Dataset](http://seanlahman.com/files/database/lahman-csv_2013-12-10.zip)

1. Without using Pandas, read in Salaries.csv and output average salary by playerID.

** 2. Without using Pandas, read in Salaries.csv and Master.csv and output salary by nameFirst and nameLast.

###Amazon Reviews Dataset

Up until now, we've worked mainly with CSV data that has been easy to import. However, often its not the modeling part that is difficult (once we understand the models) but getting data into a format that we can use for modeling.

Today we'll look at 2 datasets from Amazon. The first is a collection of movie reviews (the original set of 7 million reviews is also available) and the second is meta data on products including which customers reviewed it. However, neither is in a ready-to-use format so we must work on that first.

####Amazon Movie Reviews

A limited version of this data is available here: https://www.dropbox.com/s/9uv12p0jhysd7st/movies.txt.small and the full data set is available here: http://snap.stanford.edu/data/web-Movies.html

1. Create a tab-separated file from the file above the contains the following columns: ASIN, review text, helpfulness score (as a numeric value) and review score (as a numeric value).

Note: What are the issues with helpfulness?  How can you resolve them?

Ensure that you have a properly formatted TSV and that you can parse it back in with Pandas.

####Amazon Metadata
A limited version of this data is available here: https://www.dropbox.com/s/bm5wpeqekdm8vil/amazon-meta.txt.small and the full data set is available here: http://snap.stanford.edu/data/amazon-meta.html

1. The task here is to parse this file into a collection of product ids (ASIN), title and list of customers (by id) who have reviewed the product.

```
#### Output
### productID, title, [customer1, customer2]
```

**2. If you'd like create a review class that holds the customer id and star rating. Use this to output a product id, title and list of reviews.

***3. Create a product class that holds the id, title and collection of reviews.
