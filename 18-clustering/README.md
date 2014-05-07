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


### After

Optional:

 * Complete your `kmeans_exercise.py` (all the tests passing) and submit 
 * Check out the [sklearn text clustering example](http://scikit-learn.org/dev/auto_examples/document_clustering.html).
 * Read Cloudera's [post](http://blog.cloudera.com/blog/2013/03/cloudera_ml_data_science_tools/) on scaling k-means.
