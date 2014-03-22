### Before

Read Paul Graham's [Plan for Spam](http://www.paulgraham.com/spam.html).

Optional:

 * Explore more from Paul Graham with, for example, [Better Bayesian Filtering](http://www.paulgraham.com/better.html).
 * Read [Bayesian statistics: principles and benefits](http://edepot.wur.nl/134085) for an exposition of Bayesian vs. Frequentist approaches generally.
 * Read the very interesting [History of Bayes' Theorem](http://lesswrong.com/lw/774/a_history_of_bayes_theorem/).


### Questions

 * Paul Graham makes some predictions in his Plan for Spam. How well has he done with these predictions?
 * There are several adjustments to a "pure" Bayesian algorithm in what Paul Graham describes in his Plan for Spam. What are they, and how do you think they were arrived at?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Question review.

Application presentation.

[Slides](slides.pdf) on probability and Bayesian classification.

Go through the simple example from [Bayes' Rule for Ducks](http://planspace.org/2014/02/23/bayes-rule-for-ducks/).

With Bayes, we're principally concerned with learning the likelihood. There are many ways of doing so.

Working with code from the [Machine Learning for Hackers](http://shop.oreilly.com/product/0636920018483.do) book [[github]](https://github.com/johnmyleswhite/ML_for_Hackers). First, set up the environment:

```bash
curl -kO https://raw.githubusercontent.com/ajschumacher/ML_for_Hackers/master/03-Classification/email_classify.R
mkdir images
mkdir data
cd data
curl -O http://spamassassin.apache.org/publiccorpus/20030228_spam.tar.bz2
tar zxvf 20030228_spam.tar.bz2
curl -O http://spamassassin.apache.org/publiccorpus/20050311_spam_2.tar.bz2
tar zxvf 20050311_spam_2.tar.bz2
curl -O http://spamassassin.apache.org/publiccorpus/20021010_easy_ham.tar.bz2
tar zxvf 20021010_easy_ham.tar.bz2
curl -O http://spamassassin.apache.org/publiccorpus/20030228_easy_ham_2.tar.bz2
tar zxvf 20030228_easy_ham_2.tar.bz2
curl -O http://spamassassin.apache.org/publiccorpus/20030228_hard_ham.tar.bz2
tar zxvf 20030228_hard_ham.tar.bz2
```

Go through the use of the `tm` package for making a term document matrix. Notice the transformations it does. Mention sparse matrices. The important thing is that this is a kind of feature generation that's happening - features from text.


### Questions:

For these questions, create a `name.md` file that will eventually get to the `06-naive_bayes/code_study/` directory of the class repo.

 * Collect some of the R techniques you learn as you go through the code. Include them here.
 * There are also some negative points to be made about this code. Include observations along those lines here.
 * Running the code, you'll encounter a harmless warning, twice. What is this warning and what does it mean?
 * Later, you'll get an actual error. What is it, why did it occur, and how did you fix it?
 * How many emails are in the training and test sets of this example code as we're running it?
 * Does the code calculate word frequencies? How/does it use them?
 * What is the training step of Naive Bayes? What does it "learn"? How does this compare to KNN?
 * What are what the code calls `density` and `occurrence`? What is used to predict?
 * Which "type" of Naive Bayes does the code implement? (See: http://blog.datumbox.com/machine-learning-tutorial-the-naive-bayes-text-classifier/)
 * What are some of the differences between this code and the method described by Paul Graham? Which method do you think would get better performance?


### After

Prepare a 30-second "elevator pitch" describing your project. (This could be just a current project idea if you aren't sure what you're working on yet, but you should have some idea.) Get a `name.md` file into the `06-naive_bayes/elevator/` directory of the class repo. We'll share these elevator pitches next Wednesday. Keep working on your project!

Optional:

 * Write your own Naive Bayes spam classifier in `R`. It should have a training function that takes some features (decide how you want to pass in features) and labels as input. This function should return a data structure that somehow keeps track of what it's learned from the training data. There should be a second function that takes some features (in the same format as your training function) and a learned data structure (from your training function) and returns predicted labels. This could be a more or less major undertaking. You can put a `name.R` (or similar) file in the `06-naive_bayes/classifier/` directory of the class repo.
