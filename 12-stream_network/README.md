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

[Sketching Data Structures](http://lkozma.net/blog/sketching-data-structures/)

[Probabilistic Data Structures for Web Analytics and Data Mining](http://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/)

[Streaming Algorithms and Sketches](http://blog.aggregateknowledge.com/tag/count-min-sketch/)

[Fast, Cheap, and 98% Right: Cardinality Estimation for Big Data](http://metamarkets.com/2012/fast-cheap-and-98-right-cardinality-estimation-for-big-data/)

[Algebra for Analytics](http://cdn.oreillystatic.com/en/assets/1/event/105/Algebra%20for%20Scalable%20Analytics%20Presentation.pdf)

Paper by Will Cukierski, Ben Hammer, and Bo Yang - I think before Will worked for Kaggle:
[Graph-based Features for Supervised Link Prediction](http://www.kaggle.com/blobs/download/forum-message-attachment-files/183/supervised_link_prediction.pdf)

 * [Fast Logistic Regression: Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit/wiki)

Does this belong here?

 * [Fast Logistic Regression: LIBLINEAR](http://www.csie.ntu.edu.tw/~cjlin/liblinear/)

Logistic in `vw`:

*** 4) Try out Vowpal Wabbit to build a logistic regression model.

```sh
git clone git://github.com/JohnLangford/vowpal_wabbit.git
cd vowpal_wabbit
make install
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
