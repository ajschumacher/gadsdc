### Before

Start reading this collection of the [Top 10 algorithms in data mining](http://www.cs.umd.edu/~samir/498/10Algorithms-08.pdf). It starts and ends with (very specific) trees and includes other algorithms, some of which we've seen and some of which we'll see shortly.

Optional:

 * Read scikit's [documentation on trees](http://scikit-learn.org/dev/modules/tree.html). It's pretty good and of course very close to the implementations that we'll explore.


### Questions

 * We've talked about choosing "cut-points" for classifying based on continuous predicted probabilities. How can you choose such a cut-point? How could you automate this process?
 * We talked about KNN mostly as a classification technique, but mentioned that it can be used for regression as well. How is this done? Can this style of algorithm adaptation (classification to regression or vice versa) be used in general?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

[Slides](slides.pdf) on decision trees.

[Demo](tree.py) with sklearn.


### After

Optional:

 * You might be interested enough to go to the [original CART book](amazon.com/Classification-Regression-Wadsworth-Statistics-Probability/dp/0412048418/).
 * Explore `R` libraries for trees.
     * For CART, see `rpart`. Check out the description at [Quick-R](http://www.statmethods.net/advstats/cart.html).
     * For the well-known tree algorithms of [Quinlan](http://www.rulequest.com/): `RWeka`'s `J48` is C4.5, `C50` has C5.0.
