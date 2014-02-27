# TODO: Clean up / integrate if beneficial

Homebrew
========
Brew is a fantastic package manager for Mac that will allow you to easily install packages.  
http://mxcl.github.io/homebrew/

###Install Brew
```sh
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go/install)"
```

####GitHub

```sh
brew install git
```

Note: If you have issues with the brew install because of an XCode error, try using this Heroku Toolbelt installation that will include git, or choose an OS based installation from this guide:  http://git-scm.com/book/en/Getting-Started-Installing-Git
On Windows, there's an installer available here: http://git-scm.com/download/win

###Getting the 538 Data
```sh
git clone https://github.com/jseabold/538model
```

OR USE THIS: https://www.dropbox.com/s/ozc48me7z8tj3dl/data.zip

### Processing the data
First, we may want to get some general id of what is in the folder.  Here we will use to two basic command, `cd`, to change directory and ls to list the files
```sh
cd 538model/data
ls
```

Next we want examine the data and perhaps how much data we have in the census file.  We'll use `less` to get a preview of the files or `cat` to print the whole file. `wc` gets a word count of the file and `wc -l` gets a line count.
```sh
less census_demographics.csv
cat census_demographics.csv
wc census_demographics.csv
wc -l census_demographics.csv
```

This file is comma-separated, so we can use the `cut` command to view individual columns.
```sh
cat census_demographics.csv | cut -d',' -f1,3
```

Now, we can also get some basic information on the top educated states.  College-level education rate is the 6th column and `sort` let's us order the results
```sh
cat census_demographics.csv  | cut -d',' -f1,6 | sort -t',' -nr -k2
```

Looking at the poll data, we may want to do some basic aggregation.  Let's find out what states had the most polls.  The 8th field has the state.  `uniq -c` gives us a count of each unique element.  Note, `sort` must always proceed `uniq` as it expects sorted input.  

```sh
cat 2012_poll_data_states.csv  | cut -f8 | sort | uniq -c | sort -nrk2
```

Our results look a bit funny - we've got "State" mixed in since it was a header column.  We can skip that row by using `tail` which gives the last n lines.  `tail +n` gives all but first n lines.

```sh
cat 2012_poll_data_states.csv  | cut -f8 | tail +n2 | sort | uniq -c | sort -nrk2
```

We may want to look at just the September polls, since those were the latest polls in the files.  How many polls were in September.  We can filter using `grep`, a command that let's us search for a string in each line.

```sh
cat 2012_poll_data_states.csv | grep ^9 | wc -l
```

We can also use `grep` to find out how many polls had Obama leading and how many had Romney ahead.

```sh
cat 2012_poll_data_states.csv | grep ^9 | grep "Obama +" | wc -l
cat 2012_poll_data_states.csv | grep ^9 | grep "Romney +" | wc -l
```

Funny enough, this doesn't match the total number of polls in September.  Let's use `grep -v` which returns all lines without the search string to see what the other rows are.

```sh
cat 2012_poll_data_states.csv | grep ^9 | grep -v "Obama +" | grep -v "Romney +"
```

These polls returned are all ties with neither candidate ahead.

###In Class Examples 

- How can we extract all polls that were in Ohio?

```sh
cat 2012_poll_data_states.csv  | grep "OH$" | less
```
- How can we find out which polling company polled most often?
```sh
cat 2012_poll_data_states.csv | cut -f4 | sort | uniq -c | sort -nrk1
```

Other data processing tools available on Unix
- awk
- sed
- perl
