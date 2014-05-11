#!/usr/bin/env python
import sys

current_handle = None
counter = 1

for line in sys.stdin:
  line = line.strip()
  if current_handle is None:
    current_handle = line
    continue
  if line == current_handle:
    counter += 1
  else:
    print current_handle, counter
    current_handle = line
    counter = 1
print current_handle, counter
