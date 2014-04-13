### Before

 * Read [The Unreasonable Effectiveness of Data](http://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/35179.pdf). This is an interesting article from which to think about the costs and benefits of working with larger data sets.
 * Install [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit). This isn't always easy, but give it a shot.

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

Coding activity one:
 * Write a Python script that accepts a stream of numbers entered at the keyboard, using `raw_input()`. After each new number is entered, it should `print` the mean of all numbers entered so far.
 * After you have a working solution, consider the long term memory usage of your script. If your solution is not yet constant memory, modify it to work in constant memory (neglecting overflow issues).
 * Extension: Test your script for behavior on problematic input and adjust as needed.
 * Big extension: Change your script so that instead of accepting keyboard input with `raw_input()`, it runs as a web service and accepts input via HTTP POST requests, maintaining the running mean as the GET response. (This is well outside the scope of the class but it's kind of fun and you could work it out if you wanted to.)

Discussion of streaming as a general technique for working with data, for both general processing and also for machine learning.

Brief intro to [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit/wiki) and the `vw` [input validator](http://hunch.net/~vw/validate.html). Pre-processing is a very common necessity, and this is a fine example.

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

Perhaps show accessing the Twitter streaming API with the `TwitterAPI` module:

```Python
from TwitterAPI import TwitterAPI
api = TwitterAPI(consumer_key, consumer_secret,
                 access_token_key, access_token_secret)
r = api.request('statuses/filter', {'track':'search_string'})
for tweet in r.get_iterator():
  print tweet
```

Logistic in `vw`:

*** 4) Try out Vowpal Wabbit to build a logistic regression model.

```sh
git clone git://github.com/JohnLangford/vowpal_wabbit.git
cd vowpal_wabbit
make install
```

*** 4a) ... on Ubuntu:
```sh
sudo apt-get install vowpal-wabbit
```

Create a training file for vowpal wabbit using Python:
```sh
<Insult> | This is comment 1, no feature building needed
0 |c i really don't understand your point.\xa0 It seems that you are mixing apples and oranges.
0 |c Yeah and where are you now?
1 |c your such a dickhead...
```

This would work without editing the text at all, but you may want to remove stopwords, lowercase things and remove punctuation to clean it up.

Try the following:
```sh
vw -c -k train.vw --loss logistic -f model
vw -c -k train.vw --loss logistic -f model -l1 0.0001 ##for l1 loss
vw -c -k train.vw --loss logistic -f model -l2 0.0001 ## for l2 loss

vw -c -k -t test.vw -i model -p test.predictions
```

*** 5) Try out quadratic or cubic features in Vowpal Wabbit. 

```sh
vw -c -k train.vw --loss logistic -f model -q cc #makes quadaratic (all pairs of words) features for the 'c' feature namespace
vw -c -k train.vw --loss logistic -f model --cubic ccc #makes cubic (all triplets of words) features for the 'c' feature namespace

vw -c -k -t test.vw -i model -p test.predictions
```


### After

Optional:

 * Read [Probabilistic Data Structures for Web Analytics and Data Mining](http://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/).
 * Read [Sketching Data Structures](http://lkozma.net/blog/sketching-data-structures/).
 * Read [Streaming Algorithms and Sketches](http://blog.aggregateknowledge.com/tag/count-min-sketch/).
 * Read [Fast, Cheap, and 98% Right: Cardinality Estimation for Big Data](http://metamarkets.com/2012/fast-cheap-and-98-right-cardinality-estimation-for-big-data/)
