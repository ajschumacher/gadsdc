# TODO: Fix this up, it's a mess.

# Regression in R

##LM

The main linear regression function in R is the `lm` function.  

###Formulas
This takes a formula and a data set.  A formula in R allows you to write a functional relationship between variables.  

Example:
```R
Y ~ X1 + X2 + X3
```

R automatically assumes there  is an intercept term. You can make this explicit by using 

```R
Y ~ 1 + X1 + X2 + X3
```

or remove the intercept

```R
Y ~ 0 + X1 + X2 + X3
```

As you can see `+` is not acting as an addition operator but as a separator between other variables.  There are other operators that lose their algebraic meaning in a formula.  `:` adds the _interaction_ of two variables.  `*` adds the original terms as well as their interaction effect.

```R
Y ~ 0 + X1 * X2 + X3
```

is equivalent to 

```R
Y ~ 0 + X1 + X2 + X1:X2 + X3
```

The `^` operator still translates to a chain of `*` but the star has a different meaning.

```R
Y ~ (X1 + X2)^2 ---> Y ~ (X1 + X2)*(X1 + X2) ---> Y ~ (X1 + X2)  + (X1 + X2):(X1 + X2)
```
