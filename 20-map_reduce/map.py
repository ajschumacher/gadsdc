#!/usr/bin/env python
import sys

for line in sys.stdin:
  try:
    print eval(line)['user']['screen_name']
  except:
    pass
