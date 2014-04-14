#!/usr/bin/env python

import sys
import csv
import re
from nltk.stem.snowball import SnowballStemmer

not_alpha = re.compile("[^abcdefghijklmnopqrstuvwxyz ]")
stemmer = SnowballStemmer("english")

reader = csv.reader(sys.stdin)
if len(reader.next()) == 12:
  train = True
  title_index = 1
else:
  train = False
  title_index = 2

for line in reader:
  salary = ""
  if train:
    salary = line[10]
  title = line[title_index]
  title = title.lower()
  title = re.sub(not_alpha, "", title)
  title_words = [stemmer.stem(word) for word in title.split()]
  title = " ".join(title_words)
  print salary + " |title " + title
