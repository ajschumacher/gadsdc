### Before

Strengthen your R skills by reading these sections from [Advanced R programming](http://adv-r.had.co.nz/):

 * [Introduction](http://adv-r.had.co.nz/Introduction.html)
     * The [Meta-techniques](http://adv-r.had.co.nz/Introduction.html#meta-techniques) sub-section is worth reading twice.
 * [Data Structures](http://adv-r.had.co.nz/Data-structures.html)
 * [Subsetting](http://adv-r.had.co.nz/Subsetting.html)
 * [Functions](http://adv-r.had.co.nz/Functions.html)

Optional:

 * Also read the part on functional programming in R.


### During

Application presentation.

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
 * A data frame with columns corresponding to the first data frames', this one the data to predict for.

The function should return a vector of predicted labels for the test data. Choose a function name and a distance metric to use. You can test your function with the `iris` data. 

How do you know you're done?

 * You have a file, `yourname.R`, containing your function definition, in the `04-ML_KNN` directory of the class repo.

Extension:
 * Extend your implementation to handle non-numeric data as well.
 * Extend your implementation to take another parameter specifying the K in KNN.
 * Extend your implementation to allow a choice of distance metrics.
