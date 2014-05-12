### Before

 * Read a [Walkthrough of Hulu's Recommendation System](http://tech.hulu.com/blog/2011/09/19/recommendation-system/).

Optional:

 * Read a more in-depth corresponding paper, [Automatic Generation of Recommendations from Data: A Multifaceted Survey](http://www.deakin.edu.au/sebe/it/research/docs/trc11-4.pdf).


### Questions

 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

[Slides](slides.pdf) on recommender systems.

(The matrix factorization model in the slides is taken from [Matrix Factorization Techniques for Recommender Systems](http://www2.research.att.com/~volinsky/papers/ieeecomputer.pdf).) For more, and some code and explanation on implementing solutions with alternating least squares, see [Alternating Least Squares Method for Collaborative Filtering](http://bugra.github.io/work/notes/2014-04-19/alternating-least-squares-method-for-collaborative-filtering/).

There are also recommendation system libraries:

 * [mrec](http://mendeley.github.io/mrec/): a Python package developed at [Mendeley](http://www.mendeley.com/) to support recommender systems development and evaluation
 * [crab](http://muricoca.github.io/crab/): a recommender framework in Python
     * `crab` seems to be unfortunately extinct, but some of the materials could still be worthwhile.
 * [LensKit](http://lenskit.grouplens.org/): a Java-based open source toolkit for building, researching, and studying recommender systems


### After

Optional:

 * It might be fun to check out yhat's notebook on a [beer recommender](http://nbviewer.ipython.org/gist/glamp/20a18d52c539b87de2af).
 * An engineer from Spotify gave an interesting [talk](http://www.slideshare.net/erikbern/collaborative-filtering-at-spotify-16182818) about how they do collaborative filtering.
 * For more on ALS, see [Large-scale Parallel Collaborative Filtering for the Netﬂix Prize](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.173.2797&rep=rep1&type=pdf).
 * For more advanced recommenders, see  [Factorization Meets the Neighborhood: a Multifaceted Collaborative Filtering Model](http://public.research.att.com/~volinsky/netflix/kdd08koren.pdf).)
 * See also [Collaborative Filtering for Implicit Feedback Datasets](http://labs.yahoo.com/files/HuKorenVolinsky-ICDM08.pdf).
 * For an interesting data-enrichment technique, see [Using Filtering Agents to Improve Prediction Quality in the GroupLens Research Collaborative Filtering System](http://files.grouplens.org/papers/filterbot-CSCW98.pdf).
 * And there's Xavier Amatriain's graphic-rich [presentation](http://www.cikm2013.org/slides/xavier.pdf) on recommending at Netflix.
