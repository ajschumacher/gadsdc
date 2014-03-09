# SQL Lab

_Structured Query Language_ (SQL) is a very useful [declarative language](http://en.wikipedia.org/wiki/Declarative_programming) for working with data. It is usually supported (with some variation) by relational databases. The tutorialspoint [SQL Quick Guide](http://www.tutorialspoint.com/sql/sql-quick-guide.htm) is a handy cheat sheet for a lot of the syntax. As a data user, access to data will usually consist of a more or less complicated `SELECT` statement.

This lab uses the SQL playground provided in-browser by [W3Schools](http://www.w3schools.com/).

 * [trysql_select_all](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

This is a pre-populated data environment with nothing to install and no risk of breaking anything. The data there is from a commonly-used example database ([info](http://northwinddatabase.codeplex.com/)). Nice!


### Guided

Let's walk through a few examples:

1) Retrieve all Customers from Madrid

```sql
SELECT * FROM Customers WHERE City='Madrid'
```

2) How many customers are there in each City?

```sql
SELECT City, COUNT(*) FROM Customers GROUP BY City
```

3) What is the most common city for customers? (Can you make it easier to find the answer?)

```sql
SELECT City, COUNT(*) as count FROM Customers GROUP BY City ORDER BY count DESC
```

3) What category has the most products?

```sql
SELECT CategoryName, COUNT(*) FROM Categories JOIN Products on (Categories.CategoryID = Products.CategoryID) GROUP BY CategoryName
```


### Practice

Basic:

 * What customers are from the UK?
 * What is the name of the customer who has the most orders?
 * What supplier has the highest average product price?
 * What category has the most orders?

Intermediate:

 * What employee made the most sales (by number of sales)?
 * What employee made the most sales (by value of sales)?
 * What Employees have BS degrees? (Hint: Look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
 * What supplier of two or more products has the highest average product price? (Hint: Look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)
