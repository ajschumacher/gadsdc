### Before

Read Paul Graham's [Plan for Spam](http://www.paulgraham.com/spam.html).

Optional:

 * Explore more from Paul Graham with, for example, [Better Bayesian Filtering](http://www.paulgraham.com/better.html).
 * Read [Bayesian statistics: principles and benefits](http://edepot.wur.nl/134085) for an exposition of Bayesian vs. Frequentist approaches generally.
 * Read the very interesting [History of Bayes' Theorem](http://lesswrong.com/lw/774/a_history_of_bayes_theorem/).


### Questions

 * What determines the complexity of a linear model, as it relates to model bias and variance? How can you control this complexity?
 * Paul Graham makes some predictions in his Plan for Spam. How well has he done with these predictions?
 * There are several adjustments to a "pure" Bayesian algorithm in what Paul Graham describes in his Plan for Spam. What are they, and how do you think they were arrived at?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

> "Probability, like time, is a concept invented by humans, and humans have to bear the responsibility for the obscurities that attend it." ([John Archibald Wheeler](http://en.wikipedia.org/wiki/John_Archibald_Wheeler))

*Objective for the day*: Create a function that takes a string representation of an email as input and returns `True` if the email is spam, `False` if the email is not spam.

Exercise: Diagram the necessary steps or flow to achieve this objective. (This could be a flow chart, for example.) What will you need, and when will you need it? After you have a complete plan, you can also consider how to evaluate the function you create.

[Slides](slides.pdf) on probability and Bayesian classification.

Go through the simple example from [Bayes' Rule for Ducks](http://planspace.org/2014/02/23/bayes-rule-for-ducks/).

Note the usefulness of logarithms for changing the multiplication of a bunch of small numbers into the addition of reasonable numbers. Logarithms are useful all over the place.

With Bayes, we're principally concerned with learning the likelihood. There are many ways of doing so.


#### Exercise

Create a function that takes a string representation of an email as input and returns `True` if the email is spam, `False` if the email is not spam.

Step 1. Acquire source data.

```
http://spamassassin.apache.org/publiccorpus/
```

Step 2. Make source data accessible.

The easiest way to do this will be to extract the compressed files. You may need [help with `tar`](http://xkcd.com/1168/?use tar xvjf filename).

Step 3. Load source data into Python.

([`glob`](https://docs.python.org/2/library/glob.html) might be helpful.)

Step 3.1 (optional): Consider and implement pre-processing of the source data. Should you use all the available text? Should you use some transformations, such as [stemming](nltk_stemming.md)?

Step 4. Choose your own adventure!

Step 4a. Implement a Naive Bayes spam classifier from scratch. It works fairly nicely with basic Python data structures, and you'll get an intimate look at the workings of the algorithm.

Step 4b. Implement a Naive Bayes spam classifier using `sklearn`. You'll get good practice in using the pre-built components of the library and an understanding of the standard formats that `sklearn` expects.

Step 4c. Do both (4a) and (4b)!

Step 5. Examine model fit. What are the "spammiest" words? The "hammiest"?

Step 6. Examine model performance. Check training performance. Get test set performance. Try cross-validating.


### After

Optional:

 * Write your own Naive Bayes spam classifier in `R`. It should have a training function that takes some features (decide how you want to pass in features) and labels as input. This function should return a data structure that somehow keeps track of what it's learned from the training data. There should be a second function that takes some features (in the same format as your training function) and a learned data structure (from your training function) and returns predicted labels. This could be a more or less major undertaking. You can put a `name.R` (or similar) file in the `06-naive_bayes/classifier/` directory of the class repo.
 * Read [ML, MAP, and Bayesian — The Holy Trinity of Parameter Estimation and Data Prediction](https://engineering.purdue.edu/kak/Trinity.pdf) - "The Trinity Tutorial"
 * Read Naive-Bayes Classification using Python, NumPy, and Scikits (http://thinkmodelcode.blogspot.com/2013/04/naive-bayes-classification-using-python.html) Provides a good and step by step tutorial for Naive Bayes in Python.
