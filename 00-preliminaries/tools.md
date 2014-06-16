# Get comfortable with tools

This document helps you get up to speed with three tool families:

 * The `R` statistical programming environment.
 * The `python` programming language.
 * Command Line Interface (CLI) tools, organized around the `bash` shell and `git` for version control.
 
For each, you can go as deep as you need to feel comfortable:

 * Installing the software: This is the bare minimum to have the tools available.
 * A gentle introduction: These assume no prior knowledge of the language, and would be useful to complete prior to the course.
 * A deeper dive: These provide much more exposition and extend to advanced topics. If you have completed the introductory material and want even more experience, have at it!


## `R`

### Install

 * Install the appropriate `R` distribution for your system from this [mirror](http://watson.nci.nih.gov/cran_mirror/).
 * Install the [RStudio IDE](http://www.rstudio.com/ide/download/desktop) for `R`. The RStudio site should suggest an appropriate package for your system.

### Gentle Introduction

 * [Try R (Code School)](http://tryr.codeschool.com/): An interactive, in-browser tutorial that will take you an hour or two.
 * [Beginner's guide to R (Computerworld)](http://www.computerworld.com/s/article/9239625/Beginner_s_guide_to_R_Introduction): A six-part tutorial that you could work through in a day. It gives a more background and explanation than "Try R", and covers setup, reading in data, basic data analysis, visualization, syntax quirks, and useful resources.

### Deeper Dive

 * [R Programming (Coursera)](https://www.coursera.org/course/rprog): If you have the time, this course (part of Coursera's [Data Science Specialization](https://www.coursera.org/specialization/jhudatascience/1)) is excellent. It includes detailed video lectures, quizzes, and programming assignments. In addition, there is the opportunity to learn a lot from others in the forums. You can join at any time for free, or wait until the next session starts on July 7.
 * [Advanced R](http://adv-r.had.co.nz/): This is an in-depth guide to R, written by Hadley Wickham and the R community. It will make the most sense once you have written a moderate amount of R code, though it's a useful resource any time you want to understand a particular aspect of R in more depth.
 * [R programming for those coming from other languages](http://www.johndcook.com/R_language_for_programmers.html): A relatively quick summary of the most notable ways in which R is different from other languages.


## `python`

### Install

 * You really want the Anaconda `python` distribution. [Download and install](http://continuum.io/downloads) as appropriate for your system.

### Gentle Introduction

 * [Learn Python (Codecademy)](http://www.codecademy.com/tracks/python): An interactive, in-browser tutorial from Codecademy with 20+ modules and 200+ exercises. It is geared toward novice programmers, and thus glosses over some of the details that programmers coming from other languages might find useful. It would take many hours to work through all of the exercises; skip the projects or the more repetitive exercises if you just want to work through the syntax.
 * [Google's Python Class](https://developers.google.com/edu/python/): A bundle of written materials, video lectures, and programming assignments from an introductory two-day Python class at Google. It's a good follow-up to the Codecademy course (and is more challenging), providing less breadth than Codecademy but more depth on the most important Python topics.
 
### Deeper Dive

 * [Think Python: How to Think Like a Computer Scientist](http://www.greenteapress.com/thinkpython/): A 200-page e-book available for free in PDF or HTML format. It starts out very basic but eventually includes some sophisticated general ideas about programming.
 * [Learn Python the Hard Way](http://learnpythonthehardway.org/book/): This is probably the most popular intro to `python`, with a very distinctive voice, from the same author as the Command Line Crash Course, below.


## `bash` and `git`

Although much of the Data Science course will be taught within a "visual interface" (such as RStudio or IPython or a Python IDE), it is a useful skill to be able to work at the command line (such as `bash`). Some tasks are much faster at the command line, and some tasks require the use of the command line. Thus, we will spend some time working at the command line during the course.

`git` is the tool we will use for version control. The course will not require an advanced knowledge of `git`, but you will be submitting your homework assignments via `git` to the class GitHub repository. Although some data scientists have no knowledge of version control, knowing `git` is a useful skill that will help you stand out from your peers and help you to collaborate more effectively with others.

### Install

 * If you're running Mac OS X, `bash` is what you have by default in `Terminal`. You should [install homebrew](http://brew.sh/#install). Then `brew install git`.
 * If you're running Windows, you should [install Git Bash](http://git-scm.com/downloads).
 * If you're running Linux, you run `bash` or know better, and can install `git`.
 * Create a [GitHub](https://github.com/) account, and then [set up Git](https://help.github.com/articles/set-up-git) using the same email address that you used for your GitHub account.

### Gentle Introduction

 * [The Command Line Crash Course](http://cli.learncodethehardway.org/book/): A quick course in working at the command line. Ignore the stuff about Windows PowerShell; Windows users can just use Git Bash as your command line interface.
 * [Try Git (Code School)](http://try.github.io/): A 15-minute in-browser tutorial. It will help you to get your feet wet, but is very light on explanation.
 * [Introduction to Git and GitHub (Data School)](https://www.youtube.com/playlist?list=PL5-da3qGB5IBLMp7LtN8Nc3Efd4hJq0kD): Kevin's video series (27 minutes) that demonstrates Git, GitHub, and how they work together. Try following along with the demonstrations! Two companion blog posts: [Simple guide to forks](http://www.dataschool.io/simple-guide-to-forks-in-github-and-git/), and [Git quick reference for beginners](http://www.dataschool.io/git-quick-reference-for-beginners/).

### Deeper Dive

 * [Bash Guide for Beginners](http://writers.fultus.com/garrels/ebooks/Machtelt_Garrels_Bash_Guide_for_Beginners_2nd_Ed.pdf): A 200-page PDF book.
 * [Pro Git](http://git-scm.com/book): An excellent online book that teaches the Git concepts and code in an approachable and logical way. You will learn a lot even if you only read the first few chapters!
 * [Git Reference](http://gitref.org/): A handy reference guide for each command, including an explanation of the most common arguments.
 * [Git Tutorials (Atlassian)](https://www.atlassian.com/git/tutorial): It splits the difference between "Pro Git" and "Git Reference": less explanation than a book, but more explanation than a reference guide.
 * [GitHub Guides](https://guides.github.com/): Concise guides that help you to understand GitHub in more depth.


## Even more

There is also a [less selective list](yet_more_tools.md) of resources if you'd like to choose from a wider range.
