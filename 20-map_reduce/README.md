### Before

 * Check out the [original map-reduce paper](http://research.google.com/archive/mapreduce.html) from Google.

Optional:

 * Install [VirtualBox](https://www.virtualbox.org/) so you can run virtual machines on your local computer. Then download an image with Hadoop set up for you to play with, such as Cloudera's [QuickStart VM](http://www.cloudera.com/content/support/en/downloads/download-components/download-products.html?productID=F6mO278Rvo). Alternatively, you could install Hadoop on your local machine directly. There's an [walk-through](http://blog.tundramonkey.com/2013/02/24/setting-up-hadoop-on-osx-mountain-lion) for installing it on a Mac with `brew`.


### Questions

 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

[Slides](slides.pdf) on map-reduce.

Walk-through for doing map-reduce on Amazon Elastic MapReduce:

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

And so on. (See `aws s3 help` etc.)


#### Streaming map-reduce with Python

This example uses tweets as the data. The tweets were loaded into Python and then written to disk as stringified dicts. There are about 37 gigs of them at the `gadsdc-twitter` s3 bucket. A manageable chunk containing just 11 tweets is available: [https://s3.amazonaws.com/gadsdc-twitter/out03.txt](https://s3.amazonaws.com/gadsdc-twitter/out03.txt)

Here are simple [map](map.py) and [reduce](reduce.py) scripts. You can run locally:

```bash
cat input | ./map.py | sort | ./reduce.py > output
```

You can run cluster [streaming jobs on Amazon EMR](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/CLI_CreateStreaming.html) through the AWS console.

There is a [command line interface](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-cli-reference.html) for [Elastic Map Reduce](https://aws.amazon.com/elasticmapreduce/) as well, but it a bit old, and depends on Ruby 1.8.7.

[mrjob](https://github.com/Yelp/mrjob) is a Python library from [Yelp](http://www.yelp.com/) that wraps map-reduce and can run jobs on EMR.


#### More abstraction

[Pig](http://pig.apache.org/) lets you write [Pig Latin](http://pig.apache.org/docs/r0.7.0/piglatin_ref2.html) scripts for doing complex map-reduce tasks more easily. [Hortonworks](http://hortonworks.com/) has an introductory [tutorial](http://hortonworks.com/hadoop-tutorial/how-to-process-data-with-apache-pig/). [Mortar](http://www.mortardata.com/) has a [tutorial](http://help.mortardata.com/technologies/pig/learn_pig) as well. You can also run [Pig jobs on Amazon EMR](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-pig-launch.html).

[Hive](http://hive.apache.org/) let's you write [HiveQL](https://cwiki.apache.org/confluence/display/Hive/LanguageManual), which is very close to SQL. You can also run [Hive jobs on Amazon EMR](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-hive.html).

Spark.

[Spark Examples](https://spark.incubator.apache.org/examples.html)


Shark.


Mahout

MLlib


### After

Optional:

 * UC Berkeley's [AMP Camp](http://ampcamp.berkeley.edu/) provides great resources for learning a range of technologies including Spark.
 * This [paper](http://arxiv.org/pdf/1402.6076v1.pdf) describes large-scale machine learning in a very real-world advertising setting.
 * See also [Ad Click Prediction: a View from the Trenches at Google](http://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/41159.pdf).
 * You might be interested in the classic [Yahoo! Hadoop Tutorial](http://developer.yahoo.com/hadoop/tutorial/).
 * [Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/) is a streaming walk-through that runs Hadoop directly.
 * [An elastic-mapreduce streaming example with python and ngrams on AWS](http://dbaumgartel.wordpress.com/2014/04/10/an-elastic-mapreduce-streaming-example-with-python-and-ngrams-on-aws/) is another walk-through that uses the EMR CLI.
 * Check out an [overview](http://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/) of algorithms over map-reduce.
 * For more on doing joins with map-reduce, see this [thesis](http://www.inf.ed.ac.uk/publications/thesis/online/IM100859.pdf).
 * [Read about](http://www.cs.stanford.edu/people/ang//papers/nips06-mapreducemulticore.pdf) doing ML faster by using more cores, using map-reduce.
 * Go through an old Twitter [deck](http://www.slideshare.net/kevinweil/hadoop-pig-and-twitter-nosql-east-2009) on why Pig is good.
 * Read about why [Spark is a Crossover Hit For Data Scientists](http://blog.cloudera.com/blog/2014/03/why-apache-spark-is-a-crossover-hit-for-data-scientists/).
