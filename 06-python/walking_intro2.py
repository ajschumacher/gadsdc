# Walking intro to Python

"""
You can work with Python in a number of ways;
this is an introduction to "Python base".
"""

# Some core Python types:
type(42)                    # int
type(4.2)                   # float
type(True); type(False)     # bool
type("dog")                 # str

# Type coercion happens to some degree
42 + 4.2
4 + True - False

# But not everything is as expected
7/3

# without help:
from __future__ import division
7/3

# And we also have operator overloading
# that coerces somewhat less than JavaScript
'big' + ' ' + 'dog'
"cloud " + 9
5 - '3'

# We can coerce explicitly:
"cloud " + str(9)
5 - int('3')

# In Python, everything is an object - even strings
x = 'the lowly string'
x.startswith("the")
x.title()
x.split()

# Composite data structures
type(())   # tuple; also use tuple()
type([])   # list;  also use  list()

# You can put things of any types in here
x = (42, 4.2, True, "dog", ("a", "tuple"), 'last')
y = [42, 4.2, True, "dog", ("a", "tuple"), 'last']

# Different functions different ways
y.count(42)
len(y)
sum(range(11))

# Indexing/slicing on tuples and lists
x[0]
y[-1]
x[1:4]
y[::2]
x[::-1]

# Tuples are immutable, lists are mutable
x[0] = "first"
y[0] = "first"
y

# Lists are *very* mutable
z = y
y.append("more for y")
z # wat

# tuple (un)packing is the bee's knees
x, y = (1, 2)
x, y = y, x # wow!
# also for returning multiple things from functions

# You can make sets from lists and tuples
x = set(range(1, 5))
y = set(range(3, 8))
x | y
x & y
x - y

# Python dicts (hash, map, associative array)
d = {'key1': 'value1',
     4: ['thing', True]}
d['key1']
d[4]
d[4][0]
d[23]
d.get(23, 'not there!')
d.setdefault('keyboard', []).append('thing')
# see also: collections.defaultdict
d.keys()
d.values()
d.items()
# see also: collections.Counter

# `in` is useful in many ways
5 in range(3, 8)
5 in tuple(range(3, 8))
5 in set(range(3, 8))
5 in dict(zip(range(3, 8), "asdf"))
str(5) in "5 cows in a field"

# Flow control

for i in range(5):
    print i**2

for k, v in d.iteritems():
    print v, k

# `enumerate` is useful sometimes

for i, v in enumerate("a happy string"):
    print i, v

# There are other control facilities

while True:
    pass # forever!

while True:
    break # out!

while True:
    continue
    print "made it this time"
