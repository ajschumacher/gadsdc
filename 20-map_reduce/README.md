### Before

Optional:

 * Check out the [original map-reduce paper](http://research.google.com/archive/mapreduce.html) from Google.
 * Install [VirtualBox](https://www.virtualbox.org/) so you can run virtual machines on your local computer. Then download an image with Hadoop set up for you to play with, such as Cloudera's [QuickStart VM](http://www.cloudera.com/content/support/en/downloads/download-components/download-products.html?productID=F6mO278Rvo). Alternatively, you could install Hadoop on your local machine directly. There's an [walk-through](http://blog.tundramonkey.com/2013/02/24/setting-up-hadoop-on-osx-mountain-lion) for installing it on a Mac with `brew`.


### Questions

 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

#### The AWS Command Line Interface (CLI)

Amazon provides an [AWS CLI](https://aws.amazon.com/cli/) for interacting with many of their services, including [S3](http://aws.amazon.com/s3/). It installs easily with [pip](https://pypi.python.org/pypi/pip). You'll need an [AWS](http://aws.amazon.com/) account and an [access key](https://console.aws.amazon.com/iam/home?#security_credential) to configure it.

```bash
pip install awscli
aws configure
```

Now you can easily move files into and out of S3 buckets:

```bash
aws s3 cp myfile s3://mybucket
aws s3 sync s3://mybucket .
```

And so on. (See `aws s3 help`, for example.)

(There is a [command line interface](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-cli-reference.html) for [Elastic Map Reduce](https://aws.amazon.com/elasticmapreduce/) as well, but it is quite old, and depends on Ruby 1.8.7.)


#### Streaming map-reduce with Python

This example uses tweets as the data. The tweets were loaded into Python and then written to disk as stringified dicts. There are about 37 gigs of them at the `gadsdc-twitter` s3 bucket. A manageable chunk containing just 11 tweets is available: [https://s3.amazonaws.com/gadsdc-twitter/out03.txt](https://s3.amazonaws.com/gadsdc-twitter/out03.txt)

Here are simple [map](map.py) and [reduce](reduce.py) scripts. You can run locally:

```bash
cat input | ./map.py | sort | ./reduce.py > output
```

You can also run [streaming jobs on Amazon EMR](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/CLI_CreateStreaming.html).


#### Streaming map-reduce with Pig

You can run [Pig jobs on Amazon EMR](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-pig-launch.html).


[Yahoo! Hadoop Tutorial](http://developer.yahoo.com/hadoop/tutorial/)

[Hadoop and Pig at Twitter](http://www.slideshare.net/kevinweil/hadoop-pig-and-twitter-nosql-east-2009) presentation

[MapReduce Patterns, Algorithms, and Use Cases](http://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/)

[Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/)

Arun's Spark slides...

[Spark on EC2](spark_on_ec2.md)

[Spark Examples](https://spark.incubator.apache.org/examples.html)

[Ampcamp Slides and Exercises](http://ampcamp.berkeley.edu/4/)

[Spark is a Crossover Hit For Data Scientists](http://blog.cloudera.com/blog/2014/03/why-apache-spark-is-a-crossover-hit-for-data-scientists/)

[Machine Learning at Scale at Collective](http://arxiv.org/pdf/1402.6076v1.pdf)

[Ad Click Prediction: a View from the Trenches at Google](http://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/41159.pdf)

 * [Fast Logistic Regression: Mahout](https://cwiki.apache.org/MAHOUT/logistic-regression.html)


### After

Optional:

 * [Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/) is a streaming walk-through that runs Hadoop directly.
 * [An elastic-mapreduce streaming example with python and ngrams on AWS](http://dbaumgartel.wordpress.com/2014/04/10/an-elastic-mapreduce-streaming-example-with-python-and-ngrams-on-aws/) is another walk-through that uses the EMR CLI.
 * Check out an [overview](http://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/) of algorithms over map-reduce.
 * For more on doing joins with map-reduce, see this [thesis](http://www.inf.ed.ac.uk/publications/thesis/online/IM100859.pdf).
 * [Read about](http://www.cs.stanford.edu/people/ang//papers/nips06-mapreducemulticore.pdf) doing ML faster by using more cores, using map-reduce.
 * Go through an old Twitter [deck](http://www.slideshare.net/kevinweil/hadoop-pig-and-twitter-nosql-east-2009) on why Pig is good.
 * See also [mrjob](https://github.com/Yelp/mrjob), a [Yelp](http://www.yelp.com/), a Python interface to Hadoop map-reduce.
