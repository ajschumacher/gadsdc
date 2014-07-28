### Before

Read the [Meta-techniques](http://adv-r.had.co.nz/Introduction.html#meta-techniques) section from the [Introduction](http://adv-r.had.co.nz/Introduction.html) of [Advanced R programming](http://adv-r.had.co.nz/).

Optional:

 * Watch this [video](http://www.youtube.com/watch?v=hsFMcen0okI) about data science *discovery* vs. *production* and tools.


### Questions

 * Wickham describes a "scientific mindset" for learning R. What are the limits for the applicability of this approach? Does it apply to data science?
 * What problems have you solved by automation or programming? What problems would you like to use programming or analysis tools to solve?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Question review.

An example of an interesting data/API application: [Ranking DC tech companies based on github data](http://datacommunitydc.org/blog/2013/12/ranking-dc-software-companies-for-fun-and-employment/)

Go through the [walking introduction to R](walking_intro.Rmd).

Also refer to the [shortest introduction to R](http://planspace.org/2014/01/01/the-shortest-introduction-to-r-2/).

[Pair](http://en.wikipedia.org/wiki/Pair_programming) up and write FizzBuzz in R.

> Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

Discuss the Monty Hall problem and the value of simulation. Switch sides in pairs and write a Monty Hall problem simulator in R.

> Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

Solve problem 8 from [Project Euler](http://projecteuler.net/). Solve more, if you like!

Dataset Research assigned.

For a substantial extension based on the Monty Hall problem, go through the concepts in [monty_hall.R](monty_hall.R).


### After

 * Complete your [Dataset Research](../dataset_research/).
 * Read this [paper](http://www.jstatsoft.org/v40/i01/paper) on the split-apply-combine strategy.

Optional:
 * Write up your `R` simulator for the Monty Hall problem. Get a `name.R` file into the `02-R/monty_hall/` directory of the class repo. Your script should output a probability of winning for the always-switching strategy and the never-switching scenario. Feel free to explore and experiment!
 * Write up your `R` solution to [Project Euler](http://projecteuler.net/) problem 8. Get a `name.R` file into the `02-R/problem_8/` directory of the class repo. Your script should output the solution to the problem. (I don't think putting your solution in the class repo violates the spirit of Project Euler's no-solution-publication rule.)
