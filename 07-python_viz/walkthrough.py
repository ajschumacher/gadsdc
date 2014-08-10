# Base Python

a = range(3)
b = range(3, 6)
a + b
c = [a, b]
c[1][1]
len(c)


# Vectorization (etc.) with numpy
import numpy as np

x = np.array(a)
y = np.array(b)
x + y
np.concatenate((x, y))
z = np.array([a, b])
z[1, 1]
z.shape


# DataFrame (etc.) with pandas
import pandas as pd

# Making an example DataFrame
data = pd.DataFrame({'score': [10, 4, 29],
                     'comment': ['it was okay',
                                 'it was so bad',
                                 'it was so good']})

# Reading a DataFrame from a file
master = pd.read_csv('../../gadsdata/baseball/master.csv')

master. # tab completion
master.shape
master.duplicated?
master.duplicated(cols="birthState").sum()
master.birthState.value_counts() #etc.

salaries = pd.read_csv('../../gadsdata/baseball/salaries.csv')

master_salaries = master.merge(salaries, on='playerID')
master_salaries.head()

import matplotlib.pyplot as plt

plt.hist(master_salaries.salary)
plt.title("Distribution of Salaries")
plt.xlabel("Salaries")
plt.ylabel("Count of Players")

player_stats = master_salaries.groupby(['nameFirst', 'nameLast', 'playerID']
                                      ).salary.mean()

batting = pd.read_csv('../../gadsdata/baseball/batting.csv')
player_stats = master_salaries.merge(batting, on='playerID')

hr_rbi = player_stats.groupby('HR').RBI.mean()
plt.plot(hr_rbi) # problem
plt.plot(hr_rbi.index, hr_rbi)
hr_rbi.plot()
