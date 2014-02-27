# TODO: clean up!

# More explanation for numbers in logistic regression

```R

data(iris)
iris$sep <- factor(ifelse(iris$Sepal.Length > 6, "big", "small"))
iris$pet <- factor(ifelse(iris$Petal.Length > 4, "long", "short"))
(counts <- with(iris, table(sep, pet)))


model <- glm(pet ~ sep, data=iris, family=binomial)
coef(model)


# So what are we modeling? What are the predictions we get back?

# log odds
(logodds <- predict(model)[49:52])
# probability
(probs <- predict(model, type="response")[49:52])
# log odds relation to probability
exp(logodds) / (1 + exp(logodds))
# And this is the probability we mean:
prop.table(counts, 1)

# could do odds if we wanted to:
exp(logodds)
# and it corresponds to our probabilities like it should
probs / (1 - probs)

# What about the coefficients on the model?
coef(model)

# log odds ratio
coef(model)
# odds ratio
exp(coef(model))

# This is what the coefficients are (for this simple case):
# log odds ratio for short petals given small sepals
with(iris, log(((sum(pet=="short" & sep=="small") / sum(sep=="small")) /
                (1 - sum(pet=="short" & sep=="small") / sum(sep=="small"))) /
               ((sum(pet=="short" & sep=="big") / sum(sep=="big")) /
                (1 - sum(pet=="short" & sep=="big") / sum(sep=="big")))))
```
