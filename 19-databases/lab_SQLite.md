# SQLite Lab

It's common to use SQL with a server, often set up and loaded with data by someone else. The performance wins of having your data in a database sometimes justify doing it yourself, and you have a lot of options. To avoid having to run a server, and often still get performance gains and the convenience of SQL, the serverless [SQLite](https://www.sqlite.org/) is quite popular. It has some peculiarities, such as its commands starting with a dot, and is actually pretty limited in handling CSV, but overall SQLite is really very useful.

Install `sqlite3`. It may already be on Macs. On Ubuntu:

```bash
apt-get install sqlite3
```

To get an interactive SQL prompt, just run `sqlite3 filename` at the command line, where `filename` is a file that contains (or will contain) the database contents. (SQLite will handle writing and reading this file.)

We'll continue with our [previous lab](lab_API.md)'s data. We have to create tables and then load in the data itself, in this case from our CSV files. (This loading process will vary by database.) To avoid confusing SQLite with a header row in the CSVs, we can make some headerless files for it.

```bash
sed '1d' lab_API-budget.csv > lab_API-budget-nohead.csv
sed '1d' lab_API-deficit.csv > lab_API-deficit-nohead.csv
```

Now we're ready to work inside SQLite. `sqlite3 lab_SQLite.db`

```SQL
.mode csv

create table budget (count int, percentage float, total int, year int);
.import lab_API-budget-nohead.csv budget

create table deficit (count int, percentage float, total int, year int);
.import lab_API-deficit-nohead.csv deficit

.quit
```

That sets up two tables. Note that we can also work with data in an SQLite database from the command line, piping in SQL statements.

```bash
echo "select * from budget where year > 2010;" | sqlite3 lab_SQLite.db
```

We could now, for example, use SQL to calculate the ratio of utterances of "deficit" to "budget". (Try to do this!)

```SQL
select b.year as year, d.count as deficit, b.count as budget, 100*d.count/b.count as dtob from budget as b join deficit as d on b.year=d.year where b.year > 2010;
```
