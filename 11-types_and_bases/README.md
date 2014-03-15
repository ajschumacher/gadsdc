### Before

 * Read the Tidy Data paper on structuring data. Optionally also check out the corresponding slides and presentation video. [[paper]](http://vita.had.co.nz/papers/tidy-data.pdf) [[github]](https://github.com/hadley/tidy-data) [[slides]](http://stat405.had.co.nz/lectures/18-tidy-data.pdf) [[video]](http://vimeo.com/33727555)

Optional:

 * Install a JSON viewer for your browser, such as [JSONview](http://jsonview.com/).
 * Go through Zed Shaw's work-in-progress [Learn SQL the Hard Way](http://sql.learncodethehardway.org/book/), which will still take you through even more SQL with SQLite that we'll do in class.
 * Read this chapter from the Bad Data Handbook: "Data intended for human consumption, not machine consumption"


### Questions

 * What are the negatives of "tidy data"? When would it not be a good idea to have data in a "tidy" format? 
 * What data formats have you worked with? What are their strengths and weaknesses?
 * How can you get data? What data would you like to get for your final project? Where could you get it? Where have you looked?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Question review.

Application presentation.

Slides on data and formats.

[API lab](lab_API.md) on getting data from the web.

Slides on databases.

[SQL lab](lab_SQL_Northwind.md) on SQL, with data pre-populated.

[SQL lab](lab_SQLite.md) on using [SQLite](http://www.sqlite.org/) with your own data.

On the structured side of the spectrum, this summarizes a lot of the data structure and software map:

Structure | Format | Software | Servers
--- | --- | --- | ---
Tabular | [CSV](http://en.wikipedia.org/wiki/Comma-separated_values) etc. | most; [SQLite](http://www.sqlite.org/) | [MySQL](http://www.mysql.com/), [PostgreSQL](http://www.postgresql.org/), [etc.](http://en.wikipedia.org/wiki/Relational_database)
Nested | [JSON](http://www.json.org/), [XML](http://www.w3.org/XML/) | [rjson](http://cran.r-project.org/web/packages/rjson/index.html), [lxml](http://lxml.de/), etc. | web etc.
Graph | various | [networkx](http://networkx.github.io/), [Gephi](https://gephi.org/), etc. | [Neo4j](http://www.neo4j.org/), [etc.](http://en.wikipedia.org/wiki/Graph_database)


### After

Optional:

 * [Install PostgreSQL on your Ubuntu machine](https://help.ubuntu.com/community/PostgreSQL) and play with it.
 * Look into two [ways](RODBC_sqldf.md) of using SQL from `R`.
 * Check out [RPostgreSQL](RPostgreSQL.md) for combining `R` with PostgreSQL.
 * Check out the `python` module [dataset](http://dataset.readthedocs.org/en/latest/), which tries to combine the ease of JSON with relational databases.
 * Read this chapter from the Bad Data Handbook: "When Databases Attack: A Guide for When to Stick to Files"
