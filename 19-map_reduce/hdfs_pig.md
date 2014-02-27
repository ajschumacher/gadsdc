# TODO: Clean up, maybe change examples

##HDFS
At the core of Hadoop is HDFS, a distributed, fault-tolerant filesystem.  Put simply, this file system is not on one machine but spread across multiple machines and if one of those were to fail, data would not be lost.

Hadoop lets us access files on the special filesystem (which coexists with the local files) using similar command line syntax.

To list files, we have something similar to `ls
```sh
hadoop dfs -ls
```

To cat files, we have to also use the `hadoop dfs` command
```sh
hadoop dfs -cat /path/to/file
```

If we want to copy something from the local filesystem to HDFS, we can use the copyFromLocal flag

```sh
hdfs dfs -copyFromLocal <local_file> <folder_on_hdfs>
```

So let's start by downloading the dataset we want to work with, the salary data from earlier in the course.

```sh
wget http://bit.ly/15OA4Kr
mv train* train.tsv
```

This created a file train.csv on our local filesystem.  We can copy it to HDFS as follows:

```sh
hdfs dfs -copyFromLocal train.csv
```

Now we can access this file on hdfs using cat
```sh
hdfs dfs -cat train.csv | less
```

## Apache Pig

Pig is a query language developed for Hadoop.  Instead of writing raw map-reduce code, we are given high-level operators similar to SQL, which create map-reduce jobs behind the scenes.

###Loading Data

Data is Pig, by default, is assumed to be tabular, something like comma-separated or tab-separated files.  It does not support header rows, so we will need to specify the schema to start.

```Pig
table = LOAD '/path/to/file' USING PigStorage(',') as (col1:chararray, col2:int);
```

All this line does is setup the schema of the data we are loading from '/path/to/file' and assign this data to the variable `table`.  We need to specify what columns we expect to be in the file and what type they are.  The basic types available to us are: `int`, `chararray` (a string), `float`.  In the PigStorage function we identify the delimiter between columns.  PigStorage is a built-in function that tells Pig how to load data.

###FOREACH ... GENERATE

This is the Pig equivalent of SELECT.  Instead of SELECT col1, col2 FROM table we would write:

```Pig
data = FOREACH table GENERATE col1, col2;
```
Note the differences: 1) we had to assign the result to variable name and 2) we state the table before the columns.


###FILTER

If we want to select certain rows, instead of a WHERE clause, we use FILTER

```Pig
data = FOREACH (FILTER table col1 = 'value') GENERATE col1, col2;
```


### GROUP ... BY

From the name it is clear this is equivalent to the GROUP BY SQL operator.

```Pig
grouped_data = GROUP data by col1;
```

However, like in SQL, where GROUP BY won't be too useful without using SELECT with it, we often want to pair a GROUP...BY in Pig with a FOREACH ... GENERATE

```Pig
aggregated_grouped_data = FOREACH (GROUP data by col1) GENERATE group, AVG(data.col2);
```

Notice the difference here from SQL.  Instead of selecting col1, the column we grouped on, we select `group`, a special keyword that says what we grouped on.

### JOIN

```Pig
joined_data = JOIN table1 by col1, table2 by col2;
```
Again we want to pair this with a FOREACH ...  GENERATE to extract information out.

```Pig
some_joined_data = FOREACH (JOIN table1 by col1, table2 by col1) GENERATE table1::col1, table1::col2, table2::col2
```
Instead of using `table.column` for scoping we are using the `::` operator.


##Salary Data Set

Let's try and answer a few questions on our salary dataset using Pig.  First we will need to load it in:

```Pig
salary_data = LOAD 'train.tsv' USING PigStorage() as 
              (Id:int,
              Title:chararray,
              FullDescription:chararray,
              LocationRaw:chararray,
              LocationNormalized:chararray,
              ContractType:chararray,
              ContractTime:chararray,
              Company:chararray,
              Category:chararray,
              SalaryRaw:chararray,
              SalaryNormalized:float,
              SourceName:chararray);
```

Now we have loaded data into Pig and setup a table with the columns as above.

1) What is the average salary per Category?

```Pig
category_data = FOREACH (GROUP salary_data BY Category) GENERATE group, AVG(salary_data.SalaryNormalized);
store 
```

2) Print some entries where users are from London

```Pig
london_data = FILTER salary_data by LocationNormalized == 'London';
some_london_data = LIMIT london_data 10;
dump some_london_data;
```

3) What is the title of the highest salary job?

```Pig

title_salaries = FOREACH salary_data GENERATE Title, SalaryNormalized;
ordered_title_salaries = ORDER title_salaries BY SalaryNormalized;
top_titles = LIMIT ordered_title_salaries 10;
dump top_titles;
```

###On your own

1) What is the average salary per source?
2) How many job listings are there per ContractType?
3) What is the most frequently occurring Title?


## Hadoop Streaming


###Mapper

```Python
#category_mapper.py
import sys

for line in sys.stdin:
  line = line.strip()
  fields = line.split('\t')
  category = fields[8]
  salary = fields[10]
  print '%s\t%s' % (category, salary)
```

### Reducer
```
#category_reducer.py

import sys

current_cat = None
current_sum = 0 
current_length = 0

for line in sys.stdin:
  line = line.strip()
  category, salary = line.split('\t',1)
  try:
    category = category.strip()
    salary = float(salary)
  except:
    continue
  if current_cat == category:
    current_length += 1
    current_sum += salary
  else:
    if current_cat:
      print '%s\t%f' % (current_cat, current_sum/current_length)
    current_cat = category
    current_sum = salary
    current_length = 1
if current_cat == category:
  print '%s\t%f' % (current_cat, current_sum/current_length)
```

###Running it on your command line

```sh
cat train.tsv | python category_mapper.py
cat train.tsv | python category_mapper.py | python category_reducer.py
##Why is the last one wrong?
cat train.tsv | python category_mapper.py | sort | python category_reducer.py
