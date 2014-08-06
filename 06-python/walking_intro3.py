
# function definitions, named and positional arguments, docstrings

def add(x, y = 5):
    '''add two numbers, or adds five to one number'''
    return x + y

# avoid writing `for` loops when possible with comprehensions

x = []
for i in range(10):
    if i % 2 == 0:
        x.append(i**2)
# don't do that

# do this
x = [i**2 for i in range(10) if i % 2 == 0]

# some functional bits are also available
# and work well with lambda functions
x = map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, range(10)))

# working with files
f = open('data.csv', 'r') # second arg necessary if 'w' for write
x = f.read()
print x
f.close()

# better, use context
with open('data.csv') as f:
    x = f.read()
print x

# reading files iterate over lines
with open('data.csv') as f:
    for line in f:
        print line

with open('data.csv') as f:
    x = [line for line in f]
print x

# loading modules
import csv
with open('data.csv') as f:
    x = [line for line in csv.reader(f)]
print x

from csv import DictReader
with open('data.csv') as f:
    x = [record for record in DictReader(f)]
print x

from csv import *
# no no no
import csv as c
# yes but don't for csv

# Exceptions and `try`ing
try:
    # something dangerous/problematic
    x = 4/0
except:
    x = float('inf')
    # not a real solution

# More on strings:
"|".join(["some", "list", "elements"])
"a big cow".replace("big", "cute")
# and the `re` module...
