# Spark

## Overview

Apache Spark is a distributed data processing system written in Scala. It builds on the ideas of map-reduce (fault-tolerant distributed data processing on commodity machines) with the addition of caching data between processing operations and smart construction of job dependencies for scheduling and error recovery.

[Apache Spark](https://spark.incubator.apache.org/)

## RDD - Resilient Distributed Datasets

The RDD is the core abstraction of Apache Spark. It's collection of records that are partitioned across the machines of the cluster.  It supports many common data manipulation operations.

<!--
## AWS Setup

Please follow the AWS Setup Instruction available here: 
-->
## Launching a cluster

```sh
git clone https://github.com/apache/spark
cd spark/ec-2
./spark-ec2 -i <keypair_file> -k <keypair_name> launch <cluster_name>
```

You can set `<cluster_name>` to anything you like and the keypair comes from Amazon AWS.  You can create an account at [Amazon AWS](http://aws.amazon.com/) and navigate to EC2 -> Access Keys to create a new access key. Once you've got an access key `.pem` file you will need to change the permissions

```sh
chmod 600 <keypair_file>

# Set Amazon Keys (these are available under Account > IMA > Users > Create User
export AWS_ACCESS_KEY_ID=<>
export AWS_SECRET_ACCESS_KEY=<>
```
Once the cluster been launched, you can login through `ssh`.

```sh
# master_address.com is the address of the root node on aws, you can retrieve from the command below if you don't know it
ssh -i  <keypair_file> root@<master_address.com>

# retrieve master address
./spark-ec2 -i <keypair_file> get-master <cluster_name>
```

Most importantly, remember to kill the cluster when you are done with it otherwise you may start to build up a bill

```sh
./spark-ec2 -i <keypair_file> destroy <cluster_name>
```

More complete instructions are available at [AMPLab Tutorials](http://ampcamp.berkeley.edu/4/exercises/launching-a-bdas-cluster-on-ec2.html)

#### Accessing S3

If you want to access files on S3, you'll need to set your ACCESS_KEY in your core-site.xml configuration file.

This is available at `ephemeral-hdfs/hadoop/conf/core-site.xml`.  Open this file and add the following lines:

```
<property>
  <name>fs.s3.awsAccessKeyId</name>
  <value>ACCESS_KEY</value>
</property>

<property>
  <name>fs.s3.awsSecretAccessKey</name>
  <value>SECRET</value>
</property>

<property>
  <name>fs.s3n.awsAccessKeyId</name>
  <value>ACCESS_KEY</value>
</property>

<property>
  <name>fs.s3n.awsSecretAccessKey</name>
  <value>SECRET</value>
</property>

```

## PySpark

Most importantly for us, Spark supports a Python API to write Python Spark jobs or interact with data on cluster through a shell

### pyspark-shell

We can launch the pySpark shell with the following command:

```sh
./spark/bin/pyspark

or

IPYTHON=1 ./spark/bin/pyspark
```

Once we've opened up `pyspark` we have access to the `sc` object which gives access to `SparkContext`.  SparkContext gives us access to functions to interact with the Spark environment, for example loading data from HDFS.

```python

data = sc.textFile('hdfs:// ...')
print data.count()

```

### Data Processing

```python
#Load Data
data = sc.textFile("s3n://elasticmapreduce/samples/pig-apache/input")

#Preview data
data.take(1)

# Count data points
data.count()

# Get first 10 IP addresses
data.map( lambda x: x.split()[0] ).take(10)
```

Spark supports many of the common data operations you may want (count, filter, groupBy, etc.).  Otherwise a `map` function is available on the RDD (similar to the map function on a Pandas data frame it will perform some function on every row of the dataset) and a `reduce` function to aggregate the values.

```
# Get Count Of Hits Per IP using Map/Reduce

data.map(lambda x: (x.split()[0], 1)).reduceByKey(lambda a, b : a + b).collect()

# Alternatively Use the Built-In aggregation functions

ips = data.map(lambda x: x.split()[0])

# Using GroupBy
ips.groupBy(lambda x: x).map( lambda kv: (kv[0], len(kv[1]))).collect()

# Using .keyBy and .countValuesByKey
ips.keyBy(lambda x: x).countValuesByKey()

# Using .countByValue()
ips.countByValue()
```

### Movie Lens Dataset

#### Getting the data
First get the MovieLens Dataset, "10 million ratings and 100,000 tag applications applied to 10,000 movies by 72,000 users"

```sh
wget http://files.grouplens.org/datasets/movielens/ml-10m.zip
unzip ml-10m.zip
```

Next move the ml-10m directory to HDFS.

```sh
hadoop fs .... #How do you move the file to HDFS?
```

<!--
ephemeral-hdfs/bin/hadoop fs -copyFromLocal ml-10M100K/ .
-->

#### Loading in PySpark

```sh
spark/bin/pyspark
```

Loading the data

```python
movie_data = sc.textFile('ml-10M100K/movies.dat')
ratings_data = sc.textFile('ml-10M100K/ratings.dat')
```

Let's answer some simpler questions first ... 

```python
# How many movies do we have?
movie_data.???

# How many ratings do we have?
ratings_data.????

# How many movies are tagged with Horror?
# First we need to retrieve the tags
tags = movie_data.map( lambda x : x.split("::")[-1] )
tags.filter( lambda tag: 'Horror' in tag )

# Did anything happen on that last command?
tags.filter( lambda tag: 'Horror' in tag ).count()

# How can I keep the movie names with the tags?
tags = movie_data.map( lambda x : (x.split("::")[1], x.split("::")[-1]) )
tags.filter( lambda (movie, tag): 'Horror' in tag ).take(20)
```

_Exercise:_
Find all movies that contain horror and comedy 

_Exercise:_

Using the IP example above, how can we count the number of movies per category?

```python
#TODO(you)
```
*_HINT:_ You can't ... what's missing?*

Spark also support a `join` operation, but first we need to *key* our datasets on something to join on.

```python

keyed_ratings = ratings_data.keyBy(lambda x: x.split("::")[1])
keyed_movies = movie_data.keyBy(lambda x: x.split('::')[0])
```

Then we can join our datasets.  Joining two keyed datasets return a single keyed dataset where each row is a tuple
where the first value is the `key` and the second value is *another* tuple.

In the second tuple the first value is the matched row from dataset 1 and the second is the matched row from dataset 2.
```
row = ( <key> , (dataset_1_row, dataset_2_row))
```

```python
joined = keyed_movies.join(keyed_ratings) # This will take some time

```

We only care about a small amount of this data, the movie, the user, the category and rating.  So let's create a simpler dataset that just stores that

```
def createMovieRow( joined_row ):
    movie_row = joined_row[1][0]
    ratings_row = joined_row[1][1]
    title = movie_row.split("::")[1]
    tags = movie_row.split("::")[-1]
    user = ratings_row.split("::")[0]
    rating = float(ratings_row.split("::")[2])
    return (title, tags, user, rating)

data = joined.map(createMovieRow)

# How many reviews per movie
#TODO(you)

# How many reviews per tag
#TODO(you)

# How many average users per movie
#TODO(you)

# Compute the average rating per tag
tag_ratings = data.flatMap( lambda x: [(tag, x[-1]) for tag in x[1].split("|")] )
tag_ratings.groupBy(lambda x : x[0]).map( lambda (tag, ratings): (tag, sum(r[1] for r in ratings)/len(ratings))).collect()

```

### Machine Learning

Spark has a common library for machine learning functionality called mllib (http://spark.apache.org/docs/0.9.0/mllib-guide.html), however the functionality is still sparse.  Additionally, there have been efforts to integrate scikits-learn and Spark (https://gist.github.com/MLnick/4707012), (https://github.com/ogrisel/spylearn)

Spark has some advantages for machine learning in that it can support multiple passes over a dataset in-memory, a vital operation for machine learning algorithms that require iteration.
