# TODO: Merge or make an appropriate add-on

# Exploring census data

R functions to know:
* `help` aka `?`
* `read.csv`
* `str`
* `names`
* `intersect`
* `setdiff`
* `[]`
* `<-`
* `$`
* `toupper`
* `merge`
* `sum`
* `mean`

Necessary commands only; this is a summary of the functional but not the exploratory steps.

```R
census1 <- read.csv('census_data_2000.csv', as.is=TRUE)
census2 <- read.csv('census_demographics.csv', as.is=TRUE)
names(census1)[names(census1)=='State'] <- 'state'
census1$state <- toupper(census1$state)
census <- merge(census1, census2, by="state")
```

Always check for sanity! Investigate documentation (even [implicit](https://github.com/jseabold/538model/blob/master/get_census_data.py) [documentation](https://github.com/jseabold/538model/blob/master/historical_adjustment.py)) and compare to [other](http://www.multpl.com/united-states-population/table) [sources](http://en.wikipedia.org/wiki/Voter_turnout_in_the_United_States_presidential_elections).

What else would we have to do to use these two data sets together?

Here are a few more data manipulations.

R functions to know:
* `rbind`
* `c`
* `melt` (from `reshape`)
* `cast` (from `reshape`)
* `ddply` (from `plyr`)

```R
# combining by appending
census1$year <- 2000
census2$year <- 2012
census2 <- census2[, names(census1)]
census <- rbind(census1, census2)

# wide-long transformation
install.packages('reshape') # if needed
library(reshape)
molten = melt(census, id.vars=c("state", "year"))
# do the reverse with 'cast'

# start to think about aggregation
install.packages('plyr') # if needed
library(plyr)
moltenmeans = ddply(molten, c("state", "variable"), summarise, ave=mean(value))
```

Start to explore visually with `ggplot`. See also this [basic reference](https://github.com/arahuja/GADS4/wiki/Basic-reference-for-ggplot2). What follows are just a few possibilities.

R functions to know:
* `order`

From `ggplot2`:
* `ggplot`
* `aes`
* `geom_*`
* `scale_*`

```R
p <- ggplot(data=census1, aes(x=median_income, y=pop_density))
p + geom_point()
p + geom_text(aes(label=state))

p <- ggplot(data=census1, aes(x=state, y=vote_pop))
p + geom_bar(aes(fill=per_vote), stat="identity") + coord_flip()
  + scale_x_discrete(limits=census1$state[order(census1$vote_pop)])
  + theme_classic() + theme(legend.position="none")
```

Make a quick choropleth map:

```R
install.packages('maps') # if needed
library(maps)
states <- map_data('state')
census <- census1
census$region <- tolower(census$state)
statecensus <- merge(states, census[, c("region", "per_older")])
ggplot(data=statecensus, aes(x=long, y=lat, group=group, fill=per_older)) + geom_polygon()
```
