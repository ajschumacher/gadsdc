### Before

Optional:

 * Read [A tutorial on Principal Components Analysis](http://www.cs.otago.ac.nz/cosc453/student_tutorials/principal_components.pdf) for a very friendly introduction that starts from the very basics.
 * Read the [Stanford PCA Tutorial](http://ufldl.stanford.edu/wiki/index.php/PCA), which is just slightly mathier.
 * Read this [step-by-step walk-through](http://sebastianraschka.com/Articles/2014_pca_step_by_step.html) of PCA with Python.
 * Read an excellent paper on [The Fundamental Theorem of Linear Algebra
](http://home.eng.iastate.edu/~julied/classes/CE570/Notes/strangpaper.pdf) which goes through in an intuitive way just what SVD is all about.


### Questions

 * Why would we prefer not to have correlated features? For OLS regression, what happens when two features are identical? What happens when they're almost identical (highly correlated)?
 * What are the possible costs/benefits of having more features rather than fewer? What is a "good" number of features?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

[Slides](slides.pdf) on dimensionality reduction.

Activity:

 * This activity will use the pure spectra data (the reference panel) from the MicroMass dataset. The learning task is to predict whether bacteria are gram positive or gram negative based on mass spectrometry data.
     * Find the data online and download it.
     * Load the spectra data. It should be 571 observations of 1,300 features. What is the sparsity of the data?
     * Load the corresponding metadata and generate from it a label indicating whether each observation is gram positive or gram negative. You'll probably have to refer to the documentation PDF. What percent of observations are gram positive?
 * Once you have the data loaded, the task is not very hard; just about any method will do well. So to make it a fair fight, use a single depth-one tree. What training accuracy do you get?
 * Improve the performance of your stump by reducing the dimensionality of the training data via PCA. What training accuracy do you get now?


### After

Optional:

 * Learn about [random projections](http://users.ics.aalto.fi/ella/publications/randproj_kdd.pdf) and try them [in sci-kit](http://scikit-learn.org/stable/modules/random_projection.html).
 * Learn about t-Distributed Stochastic Neighbor Embedding ([t-SNE](http://homepage.tudelft.nl/19j49/t-SNE.html)), another technique that can be great for making complex data visualizable. It helped [win](http://blog.kaggle.com/2012/11/02/t-distributed-stochastic-neighbor-embedding-wins-merck-viz-challenge/) a Kaggle visualization contest, for example.
