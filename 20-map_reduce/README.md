### Before

Optional:


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


[Yahoo! Hadoop Tutorial](http://developer.yahoo.com/hadoop/tutorial/)

[Hadoop and Pig at Twitter](http://www.slideshare.net/kevinweil/hadoop-pig-and-twitter-nosql-east-2009) presentation

[MapReduce Patterns, Algorithms, and Use Cases](http://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/)

[Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/)


### After

Optional:
