##Statsmodels linreg in python

Statsmodels is a relatively new package, but provides better utilities for investigating the results of a model.  It use's Patsy to provide R formula syntax

A formula allows you to write a functional relationship between variables.  
Example:
```R
Y ~ X1 + X2 + X3
```

It automatically assumes there  is an intercept term. You can make this explicit by using 

```R
Y ~ 1 + X1 + X2 + X3
```

As you can see `+` is not acting as an addition operator but as a separator between other variables.  There are other operators that lose their algebraic meaning in a formula.  `:` adds the _interaction_ of two variables.  `*` adds the original terms as well as their interaction effect.


```Python
import statsmodels.formula.api as sm
import pd as pd

data = pd.read_csv("http://data.princeton.edu/wws509/datasets/salary.dat", sep='\s+')

model = sm.ols(formula="sl ~ yr", data=data).fit()
model.summary()
```

```Python
model = sm.ols(formula="sl ~ sx + yr + rk", data=data).fit()
model.summary()

model = sm.ols(formula="sl ~ sx + yr + rk", data=data).fit()
model.summary()
```


```Python
from patsy import dmatrices

y, X = dmatrices('sl ~ sx + yr + rk', data=data, return_type='dataframe')
```

###Sklearn

Scikits-learn also offer the same, but also provides regularization operations and more robust methods.

```Python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model = model.fit(X,y)
model.score(X,y)
```

```Python
from sklearn import linear_model

model = linear_model.Ridge(alpha = .5)
model.fit(X,y)

print model.coef_
```


```Python
from sklearn import linear_model

model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
model.fit(X,y)

print model.coef_
print model.alpha_
```
