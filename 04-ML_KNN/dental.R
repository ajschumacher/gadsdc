
# Pseudo-random pseudo-dental data
# (for human/machine learning)

# Columns of various types
#  * age (years)
#  * sex (male or female)
#  * brushing (frequency: daily, weekly, monthly)
#  * cavities (up to the present)
#  * cavity (at most recent appointment)
#  * timely (percent of appointments kept)
#  * elective (likelhood of opting for procedures)

people <- function(n) {
  age <- round(rweibull(n, shape=2, scale=30))
  sex <- sample(c("male", "female"), n, replace=TRUE)
  brush_freqs <- c("daily", "weekly", "monthly")
  brush_num <- sample(rep(1:3, 3:1), n, replace=TRUE)
  brushing <- brush_freqs[brush_num]
  cavities <- rpois(n, age * brush_num / 12)
  cavity <- cavities %% 3 == 1
  timely <- age + ifelse(sex=="female", 12, 0)
  timely <- round(timely / (1 + max(timely)), 2)
  elective <- cavities / brush_num + runif(n)
  elective <- round(elective / max(elective), 2)
  data.frame(age, sex, brushing, cavities, cavity, timely, elective)
}

#write.csv(people(10000), 
