### Before

Strengthen your R skills by reading these sections from [Advanced R programming](http://adv-r.had.co.nz/):

 * [Data Structures](http://adv-r.had.co.nz/Data-structures.html)
 * [Subsetting](http://adv-r.had.co.nz/Subsetting.html)
 * [Functions](http://adv-r.had.co.nz/Functions.html)

Optional:

 * Also read the part on functional programming in R.


### Questions

 * What have you learned to do with `R` that you didn't previously know? What would you still like to learn?
 * How good are you at identifying patterns? If we put humans up against computers, which side has the upper hand, under what circumstances?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Question review.

Application presentation.

Activity: Human learning on dental data
 * Types of data
 * Possible applications
 * Ways of evaluating
 * Ways of predicting
 * Build your own model!

[Slides](slides.pdf) on machine learning and KNN.

Distance metrics / [norms](http://en.wikipedia.org/wiki/Norm_(mathematics)):
 * [Hamming distance](http://en.wikipedia.org/wiki/Hamming_distance)
 * taxicab distance / L1 norm
 * Euclidean distance / L2 norm
 * [Cosine similarity](http://en.wikipedia.org/wiki/Cosine_similarity)
 * [Jaccard Index](http://en.wikipedia.org/wiki/Jaccard_index)

Introduce homework - illustrate `apply`.


### After

Implement a one-nearest-neighbor algorithm as a function in `R` that takes three arguments:

 * A data frame of numeric columns, the training data.
 * A vector of labels for the training data.
 * A data frame with the same columns as the first data frames, this one the data to predict for.

The function should return a vector of predicted labels for the test data. Choose a function name and a distance metric to use. You can test your function with the `iris` data.

How do you know you're done?

 * You have a file, `name.R`, containing your function definition, in the `04-ML_KNN` directory of the class repo.

Extension:
 * Extend your implementation to handle non-numeric data as well.
 * Extend your implementation to take another parameter specifying the K in KNN.
 * Extend your implementation to allow a choice of distance metrics.
