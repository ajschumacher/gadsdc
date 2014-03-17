R Diamonds dataset
====

Diamonds is a standard R dataset that contains prices and attributes of 53940 different diamonds. The 10 attributes used to describe each row in this dataset are:

- price (in US dollars)
- carat [more info](http://diamondse.info/diamonds-carat.asp)
- cut (quality of cut Fair-Ideal) [more info](http://diamondse.info/diamonds-cut.asp)
- colour (J-D) [more info](http://diamondse.info/diamonds-color.asp)
- clarity (l1 -IF) [more info](http://diamondse.info/diamonds-clarity.asp)
- x (length in mm) 
- y (width in mm)
- z (depth in mm)
- depth (z/mean(x,y) [more info](http://diamondse.info/diamonds-total-depth.asp)
- table (width of top of diamond relative to widest point) [more info](http://diamondse.info/diamonds-table-width.asp)

More details on each of these variables can be found in the ?diamonds documentation in R and in the more info links that link to the attribute definition on Diamond Search Engine.

History
---
These nearly 54,000 observations on diamonds come from the [Diamond Search Engine](http://diamondse.info), a collection of pricing and quality data on (as of March 17 2014) 983,482 loose diamonds for sale by leading online jewelers. [1]  The Diamond Search Engine sources pricing information from the online retailers as well as quality information from diamond certifications produced by the GIA, IGI, AGSL or EGL for each individual diamond.

[1] http://had.co.nz/stat480/lectures/07-r-intro.pdf


Acquisition
---
You can acquire the dataset cleanly from inside R. You must install the package ggplot2 first, using the command
<pre>install.packages("ggplot2")</pre>
Then import the library into your current R workspace using
<pre>library("ggplot2")</pre>
You can now work with the dataset simply by calling any functions on "diamonds", a dataframe included in the ggplot2 download.
<pre>head(diamonds) //returns top 10 rows of diamonds
tail(diamonds) // returns bottom 10 rows of diamonds
summary(diamonds) // returns 6 number summary on each of the 10 variables in diamonds
?diamonds // displays help on diamonds, including definitions of each of the 10 variables</pre>


Statistics
---
By running <code>summary(diamonds)</code>, we can get a six number summary on each of the variables. Without reproducing each summary, some interesting takeaways include:

- The average price of a diamond in this dataset is $3,933; the most expensive is $18,823 and the least expensive is $326.
- The average carat of a diamond in this dataset is 0.7979.
- The average dimensions of a diamond in this dataset (length, width, depth) was 5.731 mm, 5.735 mm, 2.539 mm.


