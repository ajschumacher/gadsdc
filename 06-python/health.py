
# Example solution to the `health.csv` exercise

from __future__ import division
import csv

# "Read health.csv into a list of (row) lists."
with open('health.csv', 'rU') as f:
    r = csv.reader(f)
    header = r.next()
    health = [line for line in r]

# Now `header` contains the column names,
# and the values are in the `health` list of lists.

# "Isolate the age column in a list."
assert(header[2] == 'age')
# (Using a `DictReader` would avoid ref-by-column-number.)
ages = [int(line[2]) for line in health]

# "Calculate the average age."
print 'average age:', sum(ages) / len(ages)

# "Construct a list that has, for each row, the sum of health2 and health5."
assert(header[5] == 'health2')
assert(header[8] == 'health5')
sum2and5 = [int(line[5]) + int(line[8]) for line in health]

# "Use comprehension(s) to calculate the average male and female ages."
assert(header[1] == 'gender')
genders = [line[1] for line in health]
males = [age for age, gender in zip(ages, genders) if gender == 'M']
females = [age for age, gender in zip(ages, genders) if gender == 'F']
male_ave = sum(males) / len(males)
print 'average male age:', male_ave
female_ave = sum(females) / len(females)
print 'average female age:', female_ave

# "Write out a csv file with two columns, sex and average_age,
#  and one row containing the values."
with open('ages.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(['sex', 'average_age'])
    w.writerow(['male', male_ave])
    w.writerow(['female', female_ave])

# Extensions:
#  * Re-write, defining your own `mean` function
#  * Re-write using `DictReader`
