### Before

 * Check out a [An introduction to Numpy and Scipy](http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf) from Scott Shell at UCSB.
 * Read at least the first two parts from [Greg Reda on pandas](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/).
 * Go through a [brief matplotlib tutorial](http://jakevdp.github.io/mpl_tutorial/).

Optional:

 * Watch the [10-minute tour of pandas](http://vimeo.com/59324550).
 * David Rojas has over ten [lessons on pandas in IPython Notebooks](https://bitbucket.org/hrojas/learn-pandas).


### Questions

 * How do the abstractions for data that we've seen in Python compare
   to those that we know for R?
 * How does Python's csv module compare to R's read.csv function? What
   are the advantages of the csv module?
 * What other thoughts, comments, concerns, and questions do you have?
   What's on your mind?


### During

Building up from base Python:
 * `import numpy as np` ([tutorial one](http://scipy-lectures.github.io/intro/numpy/array_object.html), [tutorial two](http://wiki.scipy.org/Tentative_NumPy_Tutorial))
 * `import pandas as pd` ([tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html))

Go through the [walk-through](walkthrough.py) together.

Compare R's `rnorm` vs. Python's `np.random.normal`.

Things that could go in here, or in `06-python`: see the `sklearn` and `streaming` directories.

Introduce [IPython Notebook][] and show some basic plotting. Be sure
to check out the [IPython Notebook Viewer][]!

[IPython Notebook]: http://ipython.org/ipython-doc/dev/notebook/
[IPython Notebook Viewer]: http://nbviewer.ipython.org/

Handy shortcut:

    alias nb='ipython notebook --pylab=inline'

(Note that `--pylab=inline` is a blunt instrument; it imports a lot of
things into the root namespace. You might consider loading things as
needed, setting up graphing as needed after starting a notebook with
`%matplotlib inline`, for example. For more, see IPython's
[core.magics.pylab][].)

[core.magics.pylab]: http://ipython.org/ipython-doc/2/api/generated/IPython.core.magics.pylab.html

Exercise: Make a histogram of salaries (from the linear regression
assignment training data) in an IPython Notebook, using Python (i.e.,
not `rpy2`).

There are pretty many Python visualization options now. Here are a few:

 * [Matplotlib](http://matplotlib.org/)
 * [ggplot for Python](https://github.com/yhat/ggplot/) ([introductory blog post](http://blog.yhathq.com/posts/ggplot-for-python.html))
 * [Vincent](https://vincent.readthedocs.org/)
 * [Bokeh](https://github.com/ContinuumIO/bokeh)


### After

 * [Plotting and Visualization in Python](http://nbviewer.ipython.org/urls/gist.github.com/fonnesbeck/5850463/raw/a29d9ffb863bfab09ff6c1fc853e1d5bf69fe3e4/3.+Plotting+and+Visualization.ipynb)
 * [A Gallery of Statistical Graphs in Matplotlib](http://nbviewer.ipython.org/github/cs109/content/blob/master/lec_03_statistical_graphs.ipynb)
 * [Implementation of typographic and design principles in matplotlib and iPython notebook](http://nbviewer.ipython.org/gist/olgabot/5357268)
