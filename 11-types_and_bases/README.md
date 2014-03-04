### Before

 * 

Optional:

 * Install a JSON viewer for your browser, such as [JSONview](http://jsonview.com/).
 * Read this chapter from the Bad Data Handbook: "When Databases Attack: A Guide for When to Stick to Files"


### Questions

 * What data formats have you worked with?


### During

Question review.

Application presentation.

Slides on data and formats.

API lab.

Slides on databases.

This [Visual Explanation of SQL Joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) is quite good. (One thing to remember is that "join" will also be known as "merge", often; a cross join is more like `outer()` in `R`.)

SQL lab.

This summarizes a lot of the data structure and software map:

Structure | Format | Software | Servers
--- | --- | --- | ---
Tabular | [CSV](http://en.wikipedia.org/wiki/Comma-separated_values) etc. | most; [SQLite](http://www.sqlite.org/) | [MySQL](http://www.mysql.com/), [PostgreSQL](http://www.postgresql.org/), [etc.](http://en.wikipedia.org/wiki/Relational_database)
Nested | [JSON](http://www.json.org/), [XML](http://www.w3.org/XML/) | [rjson](http://cran.r-project.org/web/packages/rjson/index.html), [lxml](http://lxml.de/), etc. | web etc.
Graph | various | [networkx](http://networkx.github.io/), [Gephi](https://gephi.org/), etc. | [Neo4j](http://www.neo4j.org/), [etc.](http://en.wikipedia.org/wiki/Graph_database)


### After

Optional:

 * Look into two [ways](RODBC_sqldf.md) of using SQL from `R`.
 * Check out [RPostgreSQL](RPostgreSQL.md) for combining `R` with PostgreSQL.
 * Check out the `python` module [dataset](http://dataset.readthedocs.org/en/latest/), which tries to combine the ease of JSON with relational databases.
