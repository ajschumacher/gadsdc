### Before

 * Explore this very nice [k-means IPython Notebook](http://nbviewer.ipython.org/github/temporaer/tutorial_ml_gkbionics/blob/master/2%20-%20KMeans.ipynb) and be very sure to play with the interactive bit at the bottom with the three buttons: "Reset", "Assign", and "Update".

Optional:

 * Read an extensive [chapter](http://www-users.cs.umn.edu/~kumar/dmbook/ch8.pdf) on clustering.


### Questions

 * In the IPython Notebook reading, how do you mentally cluster the Mickey Mouse dataset? What mental processes are involved?
 * In the IPython Notebook reading, what do the three buttons on the interactive ("Reset", "Assign", "Update") each do?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

[Slides](slides.pdf) on clustering, and k-means clustering in particular.

The interactive visual aid from the [reading notebook](http://nbviewer.ipython.org/github/temporaer/tutorial_ml_gkbionics/blob/master/2%20-%20KMeans.ipynb) is probably worth another look.

Possibly mention hierarchical clustering, with optional fun [example application](http://planspace.org/2013/07/24/clustered-r-squared-heat-maps-in-r/) in `R`.

Talk about (unit) testing, in particular with [nose](https://nose.readthedocs.org/).

With [kmeans_exercise.py](kmeans_exercise.py) and [test_kmeans_exercise.py](test_kmeans_exercise.py) in your working directory:

```bash
nosetests
```

To see just the first line, redirect standard error to standard output and use head:

```bash
nosetests 2>&1 | head -1
```

Make those tests pass! (Also, there's at least one place where things could be improved/aligned between code and documentation.)

Once the tests are passing, you could experiment with using k-means on some data in a pipeline, or to create visualizations.


### After

Optional:

 * Complete your `kmeans_exercise.py` (all the tests passing) and submit to the `15-clustering` directory of the class repo.
 * Read [Ben Bengfort](https://twitter.com/bbengfort)'s [How to Develop Quality Python Code](https://districtdatalabs.silvrback.com/how-to-develop-quality-python-code) for a good exposition on how to set up well-organized larger projects.
 * Learn more about [Python Testing](http://pythontesting.net/about/).
 * The sklearn documentation has some neat [examples](http://scikit-learn.org/dev/auto_examples/cluster/plot_cluster_comparison.html) demonstrating characteristics of various clustering algorithms.
 * Check out the [sklearn text clustering example](http://scikit-learn.org/dev/auto_examples/document_clustering.html).
 * Read Cloudera's [post](http://blog.cloudera.com/blog/2013/03/cloudera_ml_data_science_tools/) on scaling k-means.
 * Watch the [Chapter 10 lecture videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) from *An Introduction to Statistical Learning* to learn about hierarchical clustering.
