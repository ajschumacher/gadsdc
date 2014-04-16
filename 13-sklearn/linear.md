## Linear regression in Python with `statsmodels` / `sklearn`

Statsmodels uses Patsy to provide `R` formula syntax:

```R
Y ~ X1 + X2 + X3
```

```Python
import pandas as pd
import statsmodels.formula.api as sm

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

### `sklearn`

`sklearn` also offers the same, but provides more methods.

```Python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model = model.fit(X,y)
model.score(X,y)
```

```Python
from sklearn import linear_model

model = linear_model.Ridge(alpha = .5)
model.fit(X, y)

print model.coef_
```


```Python
from sklearn import linear_model

model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
model.fit(X,y)

print model.coef_
print model.alpha_
```
