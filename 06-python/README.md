### Before

 * Be _very sure_ you have a working Python 2.7 installation with
   `numpy` and SciPy installed. [Anaconda][] is highly recommended.
   The Python install that comes with Macs is _not_ sufficient without
   additional work. A fair test of whether your install is ready is
   running `ipython notebook --pylab=inline` at the command line. This
   should open a web browser displaying an interactive environment.
 * Read [PEP 20][]. Try out the Easter Egg.

[Anaconda]: http://continuum.io/downloads
[PEP 20]: http://legacy.python.org/dev/peps/pep-0020/


### Questions

 * What do you think are the relative strengths and weaknesses of R?
   Where is it more/less useful?
 * Have you used Python before? What have you used it for? What would
   you like to learn to do with Python?
 * What other thoughts, comments, concerns, and questions do you have?
   What's on your mind?


### During

Application presentation.

Question review.


Running Python interactively, running Python as a script, running
Python as an executable with a shebang:

```python
#!/usr/bin/env python
```

(Compare to `R` with `Rscript`.)

And the `__main__` setup:

```python
#!/usr/bin/env python

def main():
   pass

if __name__ == '__main__':
   main()
```

Go through the [walking introduction to Python - part 1](walking_intro1.py).


Exercise: [Pair][] up and write FizzBuzz in Python.

[Pair]: http://en.wikipedia.org/wiki/Pair_programming

> Write a program that prints the numbers from 1 to 100. But for
  multiples of three print “Fizz” instead of the number and for the
  multiples of five print “Buzz”. For numbers which are multiples of
  both three and five print “FizzBuzz”.


Introduce IPython (with `?`, tab completion, `%time` and `%timeit`,
`%run`, `%paste`).

Demo some of the environments in which to write Python:

 * Editor + IPython
 * [IDLE][]
 * [Spyder][]
 * [Komodo][]
 * [PyCharm][]

[IDLE]: http://en.wikipedia.org/wiki/IDLE_(Python)
[Spyder]: https://code.google.com/p/spyderlib/
[Komodo]: http://komodoide.com/
[PyCharm]: http://www.jetbrains.com/pycharm/


Go through the [walking introduction to Python - part 2](walking_intro2.py).


Exercise:

 * Write a Python script that accepts a stream of numbers entered at
   the keyboard, using `raw_input()`. After each new number is
   entered, it should `print` the mean of all numbers entered so far.
 * After you have a working solution, consider the long term memory
   usage of your script. If your solution is not yet constant memory,
   modify it to work in constant memory (neglecting overflow issues).
 * Extension: Test your script for behavior on problematic input and
   adjust as needed.
 * Big extension: Change your script so that instead of accepting
   keyboard input with `raw_input()`, it runs as a web service and
   accepts input via HTTP POST requests, maintaining the running mean
   as the GET response. (This is outside the scope of the class but
   it's kind of fun and you could work it out if you wanted to.)


Go through the [walking introduction to Python - part 3](walking_intro3.py).


Stupid Python tricks:

 * `import this`
 * `from __future__ import braces`


Exercise:

 * Read [health.csv](health.csv) into a list of (row) lists.
 * Isolate the `age` column in a list.
 * Calculate the average age.
 * Construct a list that has, for each row, the sum of `health2` and
   `health5`.
 * Use comprehension(s) to calculate the average male and female ages.
 * Write out a csv file with two columns, `sex` and `average_age`, and
   one row containing the values.


Python [slides](slides.pdf) also exist.


### After

Optional:

 * Read [Anti-Patterns in Python Programming](http://lignos.org/py_antipatterns/): "This page is a collection of the most unfortunate but occasionally subtle issues I've seen in code written by students new to writing Python. It's written to help students get past the phase of writing ugly Python code and understand some of the most common idioms."
 * If you'd like to walk through Python basics even more, check out this notebook [Introduction to Python](http://nbviewer.ipython.org/urls/bitbucket.org/amjoconn/watpy-learning-to-code-with-python/raw/3441274a54c7ff6ff3e37285aafcbbd8cb4774f0/notebook/Learn%20to%20Code%20with%20Python.ipynb). Or this one on [Python data structures](http://nbviewer.ipython.org/github/profjsb/python-bootcamp/blob/master/DataFiles_and_Notebooks/02_AdvancedDataStructures/data_structures.ipynb). There are a ton of public notebooks - just have fun exploring the [IPython Notebook Viewer](http://nbviewer.ipython.org/) and follow your interest!
 * You can run `R` code from _within_ IPython! Check out [rmagic](http://ipython.org/ipython-doc/dev/config/extensions/rmagic.html).
 * For some performance benchmarks, check out Cook's [Benchmarking C++, Python, R, etc.](http://www.johndcook.com/blog/2014/06/20/benchmarking-c-python-r-etc/). Python tends to outperform R, and using [numba](http://numba.pydata.org/) can speed Python up even more.
