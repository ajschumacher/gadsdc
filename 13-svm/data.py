#!/usr/bin/env python

import numpy as np
import pandas as pd

np.random.seed(42)
x = np.random.uniform(size=1000)
y = np.random.uniform(size=1000)
z = ((x-0.5)**2 + (y-0.5)**2) <= (0.5/np.pi)
x = (x - 0.5) * 0.8
y = y * 100

d = pd.DataFrame({'feature_1': x,
                  'feature_2': y,
                  'label': z})
d.to_csv('data.csv', index=False)
