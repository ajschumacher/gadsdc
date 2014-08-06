### Before

 * Read [The Unreasonable Effectiveness of Data](http://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/35179.pdf). This is an interesting article from which to think about the costs and benefits of working with larger data sets.
 * Install [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit). This isn't always easy, but give it a shot. Here are instructions for [Mac OS X](http://planspace.org/2013/02/02/install-vowpal-wabbit-on-mac-os-x/) and [Windows](http://mlwave.com/install-vowpal-wabbit-on-windows-and-cygwin/).
 * You should know about hashing, which is used all over the place. There's a [reasonable introduction on stackoverflow](http://stackoverflow.com/questions/730620/how-does-a-hash-table-work) that will give you the basic idea. It's used not just for search, but also for checking identity. It's used inside data structures, inside git, and inside bitcoin, for starters.

Optional:

 * Read [A Reliable Effective Terascale Linear Learning System](http://arxiv.org/pdf/1110.4198v3.pdf), which is largely about Vowpal Wabbit.
 * Watch this [lecture](https://www.youtube.com/watch?v=5u4G23_OohI) from Andrew Ng on linear regression, including batch and stochastic gradient descent. Maybe not the most recent video from Ng, but not bad, and we can't go the whole class without having something from Ng!
 * Read Léon Bottou's [Large-Scale Machine Learning with Stochastic Gradient Descent](http://leon.bottou.org/publications/pdf/compstat-2010.pdf).
 * Read [The Unreasonable Effectiveness of Mathematics in the Natural Sciences](http://www.dartmouth.edu/~matc/MathDrama/reading/Wigner.html). It's so good!


### Questions

 * When do you think more data is "unreasonably effective"? Is it always better to have more data? What differences might there be in various domains or particular situations?
 * How would training time for (word-token binarized multinomial) Naive Bayes change if you doubled the number of examples in the training set? What if you doubled the number of unique words in each example? How would prediction time change?
 * How would training time for KNN change if you doubled the number of examples in the training set? What if you doubled the number of features? How would prediction time change?
 * How would training time change for OLS linear regression if you doubled the number of examples in the training set? What if you doubled the number of features? How would prediction time change? (For this one you might try to figure it out experimentally in R!)
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

Discussion of streaming as a general technique for working with data, for both general processing and also for machine learning.

Brief intro to [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit/wiki) and the `vw` [input validator](http://hunch.net/~vw/validate.html). Pre-processing is a very common necessity, and this is a fine example.

Some words about `vw`:
 * fast
 * out of core / online / streaming with stochastic gradient descent (etc.)
 * combinatoric design
 * reductions

Mention the Python Natural Language ToolKit ([nltk](http://www.nltk.org/)) and its application for [stemming](http://en.wikipedia.org/wiki/Stemming). This also illustrates a common pattern of instantiating and then using objects in Python.

```Python
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
stemmer.stem("managers")
stemmer.stem("management")
# etc.
```

Coding activity two:
 * Write a Python script that reads the linear regression assignment training file and writes out a file that is ready to be read by `vw`. Check some of the output against the [validator](http://hunch.net/~vw/validate.html).
 * After you have a working solution, consider whether it is streaming or batch. Does your solution read the whole dataset into memory and keep it there, or does it go one line at a time?
 * Extension (if not already done): Modify your script to do reading and writing of the training file in a streaming fashion.
 * Extension (if not already done): Modify your script to process the test file as well as the train file.
 * Extension (if not already done): Modify your script to work as a command-line tool, taking input from standard in and sending output to standard out. You might consider the `fileinput` module, for example.

Brief demo of Vowpal Wabbit.
 * The install process for `vw` can be difficult, but on Ubuntu `sudo apt-get install vowpal-wabbit` should get you at least version 6.1, which is fine for our purposes.
 * This [tutorial](http://zinkov.com/posts/2013-08-13-vowpal-tutorial/) goes through quite a lot of `vw` in an understandable way. For more options, see the [command line arguments](https://github.com/JohnLangford/vowpal_wabbit/wiki/Command-line-arguments).
 * There's a lot to like about `vw`, and once you have your data in its format you can easily experiment with a lot of different techniques fairly easily.

Some examples with the training file made with [some_vw.py](some_vw.py):

```bash
vw train.vw --passes 100 -c
vw train.vw --passes 100 -c -q tt
vw train.vw --passes 200 -c --ngram 4
```

And so on. It's easy to add regularization and much more.

Perhaps show accessing the Twitter streaming API with the `TwitterAPI` module:

```Python
from TwitterAPI import TwitterAPI
api = TwitterAPI(consumer_key, consumer_secret,
                 access_token_key, access_token_secret)
r = api.request('statuses/filter', {'track':'search_string'})
for tweet in r.get_iterator():
  print tweet
```


### After

Optional:

 * See what kind of test set performance you can get with `vw` for the linear regression assignment data, and/or check out this [blog post](http://fastml.com/predicting-advertised-salaries/) from someone who used `vw` when the Adzuna competition was running on Kaggle.
 * [Read](http://zinkov.com/posts/2013-08-13-vowpal-tutorial/) [even](http://fastml.com/go-non-linear-with-vowpal-wabbit/) [more](http://www.slideshare.net/pauldix/terascale-learning) [on](http://www.slideshare.net/jakehofman/technical-tricks-of-vowpal-wabbit) [vw](http://fastml.com/large-scale-l1-feature-selection-with-vowpal-wabbit/).
 * Read [Probabilistic Data Structures for Web Analytics and Data Mining](http://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/).
 * Read [Sketching Data Structures](http://lkozma.net/blog/sketching-data-structures/).
 * Read [Streaming Algorithms and Sketches](http://blog.aggregateknowledge.com/tag/count-min-sketch/).
 * Read [Fast, Cheap, and 98% Right: Cardinality Estimation for Big Data](http://metamarkets.com/2012/fast-cheap-and-98-right-cardinality-estimation-for-big-data/)
