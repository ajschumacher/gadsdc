### Before

Optional:

 * Read Léon Bottou's [Large-Scale Machine Learning with Stochastic Gradient Descent](http://leon.bottou.org/publications/pdf/compstat-2010.pdf).
 * Watch this [lecture](https://www.youtube.com/watch?v=5u4G23_OohI) from Andrew Ng on linear regression, including batch and stochastic gradient descent. Maybe not the most recent video from Ng, but not bad, and we can't go the whole class without having something from Ng!


### Questions

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
