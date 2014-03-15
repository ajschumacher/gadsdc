# A Monty Hall simulation can be written step-by-step, following the story
# of the game. This code attempts to mimic the mechanics closely. It also
# demonstrates a range of R functionality and extends the simulation to allow
# an arbitrary number of goats. Notice how the `win_car` function performs
# a very manageable part of the simulation - it is separate from the
# repeating of attempts or the comparison of strategies, for example.
# The `switching` argument is not defaulted, forcing a choice of strategy.
# Determining what functions to write - your own API - is important.

# `win_car` returns a logical indicating whether you've won a car when
# you play Monty Hall's door guessing game, based on whether you choose
# to switch doors or not (`switching`, logical).

win_car <- function(switching, goats=2) {
  prizes <- c("car", rep("goat", goats))
  doors <- setNames(sample(prizes), seq_along(prizes))
  choice <- sample(names(doors), 1)
  opened <- sample(setdiff(names(doors),
                           c(choice, names(doors)[doors=="car"])),
                   length(doors)-2)
  if (switching) {
    choice <- setdiff(names(doors), c(choice, opened))
  }
  return(unname(doors[choice] == "car"))
}

# With this function in hand simulations can be done using `replicate`,
# `sapply`, `vapply`, or `lapply`. Notice that the many simulations done for
# the following graphic do not happen very quickly.

matplot(data.frame(sapply(1:400, function(n) mean(replicate(n, win_car(switching=FALSE)))),
                   sapply(1:400, function(n) mean(replicate(n, win_car(switching=TRUE))))),
        type="p", pch=19, cex=0.6, col=c("red", "blue"),
        ylab="proportion wins", xlab="number of plays",
        ylim=c(0, 1), main="Effectiveness of Monty Hall strategies (story sim)")
legend(x="topright", legend=c("switching", "staying"), pch=19, cex=0.6, col=c("blue", "red"))

# Since we actually do know a closed form solution to the Monty Hall problem,
# we could get better performance by using it.

matplot(data.frame(rbinom(400, 1:400, 1/3)/1:400,
                   rbinom(400, 1:400, 2/3)/1:400),
        type="p", pch=19, cex=0.6, col=c("red", "blue"),
        ylab="proportion wins", xlab="number of plays",
        ylim=c(0, 1), main="Effectiveness of Monty Hall strategies (rbinom sim)")
legend(x="topright", legend=c("switching", "staying"), pch=19, cex=0.6, col=c("blue", "red"))

# Another way to increase performance is to use `mclapply` ("multi-core
# lapply") from the `multicore` package. It works just like `lapply` but
# uses all available compute cores.

system.time(lapply(1:400, function(n) replicate(400, win_car(switching=TRUE))))
library(multicore)
system.time(mclapply(1:400, function(n) replicate(400, win_car(switching=TRUE))))

# This will give you performance gains for "embarassingly parallelizable"
# computations of sufficient number and complexity to outweigh the overhead
# of managing the parallelization.
