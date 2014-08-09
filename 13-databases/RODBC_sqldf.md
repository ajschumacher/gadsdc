# SQL in `R` with `RODBC` and `sqldf`

Structured Query Language (SQL) is very popular for working with data, especially when that data lives in a relational database.

There are two main ways that SQL can be used in R:

 * R can act as a client of an external relational database and pull in data with SQL queries.
 * R can generate and use a relational database on the fly using data already in R, which can be convenient and sometimes more performant.


### SQL in `R` with `RODBC`

R can act as a client of an external relational database and pull in data with SQL queries.

This example connects to a Microsoft SQL Server database and pulls some data in from it:

```r
library(RODBC)
db27 <- odbcDriverConnect("driver={SQL Server};server=mtsqlvs27\\mtsqlins27;trusted_connection=true")
results <- sqlQuery(db27, "select * from spr_int.prl.raw_register_audit where year = 2012")
```

The particular library and/or connect string will vary depending on the database you're connecting to.


### SQL in `R` with `sqldf`

R can generate and use a relational database on the fly using data already in R, which can be convenient and sometimes more performant.

```r
library(sqldf)
results <- sqldf("select Species, Date from iris where Petal_Length > 2 limit 6")
```

SQL is a well-known and fairly powerful language for data manipulation. Some people will find it easier to use SQL selects and joins than native R equivalents for working with data.
