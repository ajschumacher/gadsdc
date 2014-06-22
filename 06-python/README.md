### Before

 * Be _very sure_ you have a working Python 2.7 installation with `numpy` and SciPy installed. [Anaconda](http://continuum.io/downloads) is highly recommended. The Python install that comes with Macs is _not_ sufficient without additional work. A fair test of whether your install is ready is running `ipython notebook --pylab=inline` at the command line. This should open a web browser displaying an interactive environment.
 * Read [PEP 20](http://legacy.python.org/dev/peps/pep-0020/). Try out the Easter Egg.


### Questions

 * Consider thinking of boolean multinomial Naive Bayes likelihood probabilities as coefficients on word dummy features. How are they similar or different as compared with logistic regression coefficients?
 * How can binary classifiers be used for multiclass problems? That is, if a technique only gives a probability of "yes" vs. "no" (for some question) how can you use the technique for questions with more than two possible answers?
 * What do you think are the relative strengths and weaknesses of R? Where is it more/less useful?
 * Have you used Python before? What have you used it for? What would you like to learn to do with Python?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

Python [slides](slides.pdf).

Running Python interactively, running Python as a script, running Python as an executable with a shebang:

    #!/usr/bin/env python

Compare to `R` with `Rscript`, and `rnorm` vs. `np.random.normal`.

Exercise: [Pair](http://en.wikipedia.org/wiki/Pair_programming) up and write FizzBuzz in Python.

> Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

Introduce IPython (with `?`, tab completion, `%time` and `%timeit`, `%run`, `%paste`).

Stupid Python tricks: `from __future__ import division`, mutable lists, `str.join`, etc.

Exercise: Pair up and use IPython to read in the linear regression assignment (salary) training data, using the `csv` module. Use the Python docs! Use Python to calculate the average salary.

Introduce [IPython Notebook](http://ipython.org/ipython-doc/dev/notebook/) and show some basic plotting. Be sure to check out the [IPython Notebook Viewer](http://nbviewer.ipython.org/)!

Handy shortcut:

    alias nb='ipython notebook --pylab=inline'

Exercise: Make a histogram of salaries (from the linear regression assignment training data) in an IPython Notebook, using Python (i.e., not `rpy2`).

There are pretty many Python visualization options now. Here are a few:

 * [Matplotlib](http://matplotlib.org/) ([tutorial](http://jakevdp.github.io/mpl_tutorial/))
 * [ggplot for Python](https://github.com/yhat/ggplot/) ([introductory blog post](http://blog.yhathq.com/posts/ggplot-for-python.html))
 * [Vincent](https://vincent.readthedocs.org/)
 * [Bokeh](https://github.com/ContinuumIO/bokeh)


### After

Prepare three visualizations based on your final project data. Each one should show the viewer something about the data - the viewer should know something more, hopefully something interesting, after viewing the visualization. Clear labels will be important. You can use `R` or `python` (or both) and include code (including R markdown and/or IPython Notebooks) but you should also produce image files that can be viewed separately. Leave your image and source files in the `10-python` directory of the class repo. It would be good to name your files something consistent, like `name01.png`, `name02.png`, `name.R`, etc. The purpose of submitting image files in this way is so that they can be easily viewed all together when they are presented next week Wednesday.

Optional:

 * If you'd like to walk through Python basics even more, check out this notebook [Introduction to Python](http://nbviewer.ipython.org/urls/bitbucket.org/amjoconn/watpy-learning-to-code-with-python/raw/3441274a54c7ff6ff3e37285aafcbbd8cb4774f0/notebook/Learn%20to%20Code%20with%20Python.ipynb). Or this one on [Python data structures](http://nbviewer.ipython.org/github/profjsb/python-bootcamp/blob/master/DataFiles_and_Notebooks/02_AdvancedDataStructures/data_structures.ipynb). There are a ton of public notebooks - just have fun exploring the [IPython Notebook Viewer](http://nbviewer.ipython.org/) and follow your interest!
 * For some performance benchmarks, check out Cook's [Benchmarking C++, Python, R, etc.](http://www.johndcook.com/blog/2014/06/20/benchmarking-c-python-r-etc/). Python tends to outperform R, and using [numba](http://numba.pydata.org/) can speed Python up even more.
 * You can run `R` code from _within_ IPython! Check out [rmagic](http://ipython.org/ipython-doc/dev/config/extensions/rmagic.html).
