### Before

Optional:

 * Read this chapter from the Bad Data Handbook: "When Databases Attack: A Guide for When to Stick to Files"


### Questions

 * What data formats have you worked with?


### During

Here is a data table:

Structure | Format | Software | Servers
--- | --- | --- | ---
Tabular | [CSV](http://en.wikipedia.org/wiki/Comma-separated_values) etc. | most; [SQLite](http://www.sqlite.org/) | [MySQL](http://www.mysql.com/), [PostgreSQL](http://www.postgresql.org/), [etc.](http://en.wikipedia.org/wiki/Relational_database)
Nested | [JSON](http://www.json.org/), [XML](http://www.w3.org/XML/) | [rjson](http://cran.r-project.org/web/packages/rjson/index.html), [lxml](http://lxml.de/), etc. | web etc.
Graph | various | [networkx](http://networkx.github.io/), [Gephi](https://gephi.org/), etc. | [Neo4j](http://www.neo4j.org/), [etc.](http://en.wikipedia.org/wiki/Graph_database)


Something.
cf. merges


### After

Optional:

 * Look into two [ways](RODBC_sqldf.md) of using SQL from `R`.
 * Check out [RPostgreSQL](RPostgreSQL.md) for combining `R` with PostgreSQL.
 * Check out the `python` module [dataset](http://dataset.readthedocs.org/en/latest/), which tries to combine the ease of JSON with relational databases.
