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

Walk-through for doing map-reduce on Amazon Elastic MapReduce (EMR):

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

There is a [command line interface](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-cli-reference.html) for [Elastic Map Reduce](https://aws.amazon.com/elasticmapreduce/) as well, but it's a bit old, and depends on Ruby 1.8.7.


#### More abstraction

[Pig](http://pig.apache.org/) lets you write [Pig Latin](http://pig.apache.org/docs/r0.7.0/piglatin_ref2.html) scripts for doing complex map-reduce tasks more easily. [Hortonworks](http://hortonworks.com/) has an introductory [tutorial](http://hortonworks.com/hadoop-tutorial/how-to-process-data-with-apache-pig/). [Mortar](http://www.mortardata.com/) has a [tutorial](http://help.mortardata.com/technologies/pig/learn_pig) as well. You can also run [Pig on Amazon EMR](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-pig-launch.html).

[Hive](http://hive.apache.org/) adds some more structure to data and let's you write [HiveQL](https://cwiki.apache.org/confluence/display/Hive/LanguageManual), which is very close to SQL. You can also run [Hive on Amazon EMR](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-hive.html).

 * [mrjob](https://github.com/Yelp/mrjob) is a Python library from [Yelp](http://www.yelp.com/) that wraps map-reduce and can run jobs on EMR.
 * [Luigi](https://github.com/spotify/luigi) is a Python library from [Spotify](https://www.spotify.com/us/) that lets you write map-reduce workflows more easily.
 * [Cascading](http://www.cascading.org/) is a layer on top of Hadoop that has further layers such as [Scalding](https://github.com/twitter/scalding) ([Scala](http://www.scala-lang.org/)) from [Twitter](https://twitter.com/) - yet another way to simplify working with map-reduce.
 * [RHadoop](https://github.com/RevolutionAnalytics/RHadoop/wiki) provides an interface for running `R` on Hadoop.

Totally separate from Hadoop, [MongoDB](http://www.mongodb.org/) has an internal implementation of map-reduce.


#### Beyond Map-Reduce

Cloudera's [Impala](http://www.cloudera.com/content/cloudera/en/products-and-services/cdh/impala.html) is inspired by Google's [Dremel](http://research.google.com/pubs/pub36632.html). Of course there's also [Drill](http://incubator.apache.org/drill/). And if you want to get Dremel straight from the source, you can buy it as a service from Google as [BigQuery](https://cloud.google.com/products/bigquery/).

[Spark](http://spark.apache.org/) keeps things in memory to be much faster. This is especially useful for iterative processes. See, for example, their [examples](https://spark.incubator.apache.org/examples.html), which feature their nice Python API. There's also [Shark](http://shark.cs.berkeley.edu/), which gives much faster HiveQL query performance. You can [run Spark/Shark on EMR](https://aws.amazon.com/articles/Elastic-MapReduce/4926593393724923) too.


#### `sklearn` for huge data?

Not exactly. But there are some projects that step in that direction:

[Mahout](http://mahout.apache.org/) is a project for doing large scale machine learning. It was originally mostly map-reduce oriented, but in April 2014 announced a move toward Spark.

[MLlib](http://spark.apache.org/docs/0.9.0/mllib-guide.html) is the machine learning functionality directly on Spark, which is actively growing.


### After

Optional:

 * UC Berkeley's [AMP Camp](http://ampcamp.berkeley.edu/) provides great resources for learning a range of technologies including Spark. (Berkeley's [AMP Lab](https://amplab.cs.berkeley.edu/software/) is responsible for a lot of these cool technologies.)
 * This [paper](http://arxiv.org/pdf/1402.6076v1.pdf) describes large-scale machine learning in a very real-world advertising setting.
 * See also [Ad Click Prediction: a View from the Trenches at Google](http://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/41159.pdf).
 * [Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/) is a streaming walk-through that runs Hadoop directly.
 * [An elastic-mapreduce streaming example with python and ngrams on AWS](http://dbaumgartel.wordpress.com/2014/04/10/an-elastic-mapreduce-streaming-example-with-python-and-ngrams-on-aws/) is another walk-through that uses the EMR CLI.
 * Check out an [overview](http://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/) of algorithms over map-reduce.
 * For more on doing joins with map-reduce, see this [thesis](http://www.inf.ed.ac.uk/publications/thesis/online/IM100859.pdf).
 * [Read about](http://www.cs.stanford.edu/people/ang//papers/nips06-mapreducemulticore.pdf) doing ML faster by using more cores, using map-reduce.
 * Go through an old Twitter [deck](http://www.slideshare.net/kevinweil/hadoop-pig-and-twitter-nosql-east-2009) on why Pig is good.
 * Read about why [Spark is a Crossover Hit For Data Scientists](http://blog.cloudera.com/blog/2014/03/why-apache-spark-is-a-crossover-hit-for-data-scientists/).
