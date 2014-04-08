# TODO: clean/clarify and probably split across multipe files/days

##Python Shell
Python at it's core is a fancy calculator.  Typing `python` into the command line will give you a prompt
```sh
python

or

ipython
```

IPython provides a more interactive shell and provides a few nice utility functions that make life easier.
For example, starting with a `?`,
```python
?sys
```
will give documentation for function.  Also, IPython provides autocomplete as well.  Additional it provides a few "magic" functions like `%time` and `%paste`, the former of which times function and the latter allows easy copy and paste of code.

##Defining functions
In Python we define functions by using the `def` keyword.  The value of the function is giving in the return statement.

```Python
def addition(x, y):
  return x + y
```
`x` and `y` are the inputs to the function and the `return` keyword tells us what the function responds.  The most important thing to note here is that Python respects whitespace, the second like **must** be indented for this to run.

##Data Structures

Python has a variety of data structures available.  The most basic of them are the basic integer, float and strings.  Python is dynamically typed, so typed do not need to be specified and variables can be respecified to different types

```python
x = 5.0
x = [5.0]
x = "Five Point 0"
```
###Lists

Lists are one of the most common data structures in Python.

```Python 
l = [1,2,3,4] #Setting up a list
l.append(5) #Adding to it using the append function
l += [6] #Adding to it using the addition operation
```

###Dictionaries

Dictionaries in Python are equivalent to Hash Tables in any other language.

```Python
x = {} # Empty Dictionary
y = {'key' : value}
y[key] = "new-value"
```

##Loop Constructs

Like any other programming language, Python has loop constructs, the ability to iterate over different elements.

```Python

l = [1,2,3,4]
for i in l:
  print i
```

However, when possible, Python will perform better using list comprehensions.

```Python
x = [1,2,3,4]

#The following are equivalent
y = []
for i in x:
  y.append(i**2)

#OR

y = [i**2 for i in x]
```

Also, Python can iterate over `generators`, these are functions act as iterators, meaning they give access to elements of a sequence.

For example, `xrange`
```python
for i in xrange(10):
    print x
```
or `enumerate`
for i, el in enumerate(my_list):
   print i, el
```
This will print out the index of the element (starting from 0) and the element.

```

##Pandas
Pandas is a Python library for data analysis that resembles the tools available in R.  It is also optimized for fast I/O and data manipulation.

```Python
import pandas as pd

data = pd.read_csv('Dropbox/src/538model/data/2012_poll_data_states.csv', sep='\t')
#Get a preview of the first six rows
data.head()
```

Get descriptive statistics for any or all columns
```python
data.describe()
```

Bin the values of a column
```python
data['Poll'].value_counts()
```
Aggregate over a particular column
```python
data.groupby('Poll')['Obama (D)'].mean()
```
