### Before

 * Read the Tidy Data paper on structuring data. Optionally also check
   out the corresponding slides and presentation video.
   [[paper]](http://vita.had.co.nz/papers/tidy-data.pdf)
   [[github]](https://github.com/hadley/tidy-data)
   [[slides]](http://stat405.had.co.nz/lectures/18-tidy-data.pdf)
   [[video]](http://vimeo.com/33727555)

Optional:

 * Go through Zed Shaw's work-in-progress
   [Learn SQL the Hard Way](http://sql.learncodethehardway.org/book/),
   which will still take you through even more SQL with SQLite that
   we'll do in class.


### Questions

 * Consider thinking of boolean multinomial Naive Bayes likelihood
   probabilities as coefficients on word dummy features. How are they
   similar or different as compared with logistic regression
   coefficients?
 * How can binary classifiers be used for multiclass problems? That
   is, if a technique only gives a probability of "yes" vs. "no" (for
   some question) how can you use the technique for questions with
   more than two possible answers?
 * How do K Nearest Neighbors, Naive Bayes, and linear models compare
   in terms of model interpretability? How/when could this inform
   model choices?
 * What are the negatives of "tidy data"? When would it not be a good
   idea to have data in a "tidy" format?
 * What other thoughts, comments, concerns, and questions do you have?
   What's on your mind?


### During

Application presentation.

Question review.

Slides on databases.

[SQL lab](lab_SQL_Northwind.md) on SQL, with data pre-populated.

[SQL lab](lab_SQLite.md) on using [SQLite](http://www.sqlite.org/)
with your own data.

On the structured side of the spectrum, this summarizes a lot of the
data structure and software map:

Structure | Format | Software | Servers
--- | --- | --- | ---
Tabular | [CSV](http://en.wikipedia.org/wiki/Comma-separated_values) etc. | most; [SQLite](http://www.sqlite.org/) | [MySQL](http://www.mysql.com/), [PostgreSQL](http://www.postgresql.org/), [etc.](http://en.wikipedia.org/wiki/Relational_database)
Nested | [JSON](http://www.json.org/), [XML](http://www.w3.org/XML/) | [rjson](http://cran.r-project.org/web/packages/rjson/index.html), [lxml](http://lxml.de/), etc. | web etc.
Graph | various | [networkx](http://networkx.github.io/), [Gephi](https://gephi.org/), etc. | [Neo4j](http://www.neo4j.org/), [etc.](http://en.wikipedia.org/wiki/Graph_database)


### After

Optional:

 * For more introductory SQL, check out the [Mode Analytics "SQL School"](http://sqlschool.modeanalytics.com/).
 * [Install PostgreSQL on your Ubuntu machine](https://help.ubuntu.com/community/PostgreSQL) and play with it.
 * Look into two [ways](RODBC_sqldf.md) of using SQL from `R`.
 * Check out [RPostgreSQL](RPostgreSQL.md) for combining `R` with PostgreSQL.
 * Check out the `python` module [dataset](http://dataset.readthedocs.org/en/latest/), which tries to combine the ease of JSON with relational databases.
 * Read this chapter from the Bad Data Handbook: "When Databases Attack: A Guide for When to Stick to Files"
 * Explore Kristof Kovacs' [Comparison of NoSQL Databases](http://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis).
