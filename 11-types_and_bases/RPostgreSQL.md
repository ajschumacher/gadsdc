## RPostgreSQL

PostgreSQL is an open source, relational database.

Read about it here: http://en.wikipedia.org/wiki/PostgreSQL

### What is RPostgreSQL?
RPostgreSQL is an R library that allows you to interact with databases in PostgreSQL in a much more efficient way than your standard ODBC connector.  

Documentation: https://code.google.com/p/rpostgresql/

### Why use RPostgreSQL?
1) Data is often stored in databases.
2) Automated R/DB interaction means less time transferring data and more time doing analysis!

### PostgreSQL basics
From terminal
```shell
psql database_name
```

Try these commands: 
```
\h, \?, \l, \c database\_name, \d, \d table\_name, \du, \e
```

Create a table
```sql
CREATE TABLE my_table (
    id serial primary key,
    some_string varchar(255),
    some_int int,
    some_float float4,
    bigger_float float8,
    some_date date,
    ...
)
```

### Integrating R and PostgreSQL
Setup Connection: 
```r con <- dbConnect(PostgreSQL(), user='user', password='password', dbname='mydb')```

Find your tables: 
```r dbListTables(con)```

Run a Query and Save as R object:
```r
query <- "SELECT some_stuff FROM some_db"
mydata <- dbGetQuery(con, query)
```

Oh noes, query too big!  Return 500 line at a time.
```r
query <- "SELECT tons_of_stuff FROM some_db"
result <- dbSendQuery(con, query)
mydata <- fetch(result, n=500) 
```

Screw it, let the server/database do all the work (beta)
```r 
query <- "SELECT tons_of_stuff FROM some_db"
result <- dbSendQuery(con, query)
findings <- dbApply(result, INDEX='group_by_variables', FUN=some_function)
```
