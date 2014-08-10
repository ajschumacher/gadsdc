### Before

 * Check out a [An introduction to Numpy and Scipy](http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf) from Scott Shell at UCSB.
 * Read at least the first two parts from [Greg Reda on pandas](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/).
 * Go through a [brief matplotlib tutorial](http://jakevdp.github.io/mpl_tutorial/).


### Questions

 * How do the abstractions for data that we've seen in Python compare
   to those that we know for R?
 * How does Python's csv module compare to R's read.csv function? What
   are the advantages of the csv module?
 * What other thoughts, comments, concerns, and questions do you have?
   What's on your mind?


### During

and `rnorm` vs. `np.random.normal`.

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

 * [Matplotlib](http://matplotlib.org/) ([tutorial](http://jakevdp.github.io/mpl_tutorial/))
 * [ggplot for Python](https://github.com/yhat/ggplot/) ([introductory blog post](http://blog.yhathq.com/posts/ggplot-for-python.html))
 * [Vincent](https://vincent.readthedocs.org/)
 * [Bokeh](https://github.com/ContinuumIO/bokeh)


### After

Prepare three visualizations based on your final project data. Each
one should show the viewer something about the data - the viewer
should know something more, hopefully something interesting, after
viewing the visualization. Clear labels will be important. You can use
`R` or `python` (or both) and include code (including R markdown
and/or IPython Notebooks) but you should also produce image files that
can be viewed separately. Leave your image and source files in the
`10-python` directory of the class repo. It would be good to name your
files something consistent, like `name01.png`, `name02.png`, `name.R`,
etc. The purpose of submitting image files in this way is so that they
can be easily viewed all together when they are presented next week
Wednesday.

 * [Plotting and Visualization in Python](http://nbviewer.ipython.org/urls/gist.github.com/fonnesbeck/5850463/raw/a29d9ffb863bfab09ff6c1fc853e1d5bf69fe3e4/3.+Plotting+and+Visualization.ipynb)
 * [A Gallery of Statistical Graphs in Matplotlib](http://nbviewer.ipython.org/github/cs109/content/blob/master/lec_03_statistical_graphs.ipynb)
 * [Implementation of typographic and design principles in matplotlib and iPython notebook](http://nbviewer.ipython.org/gist/olgabot/5357268)
