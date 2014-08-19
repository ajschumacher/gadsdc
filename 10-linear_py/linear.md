## Linear regression in Python with `statsmodels` / `sklearn`

Statsmodels uses Patsy to provide formula syntax similar to `R`'s.


Formulas in `R` look like this:

```R
Y ~ X1 + X2 + X3
```


In Python, start with data in `pandas` data frames:

```Python
import pandas as pd

url = "http://data.princeton.edu/wws509/datasets/salary.dat"
data = pd.read_csv(url, sep='\s+')
```


`patsy` can produce design matrices from formula specifications:

```Python
from patsy import dmatrices

y, X = dmatrices('sl ~ sx + yr + rk', data=data, return_type='dataframe')
```


`statsmodels` includes `patsy` for model specification and provides an array of modeling techniques with output that resembles Stata's.

```Python
import statsmodels.formula.api as smf

model = smf.ols(formula="sl ~ yr", data=data).fit()
model.summary()

model = smf.ols(formula="sl ~ sx + yr + rk", data=data).fit()
model.summary()

model = smf.ols(formula="sl ~ sx + yr + rk", data=data).fit()
model.summary()
```


`sklearn` does not integrate `patsy`, but it offers far more modeling options.

```Python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model = model.fit(X,y)
model.score(X, y)
```

```Python
from sklearn.linear_model import Ridge

model = Ridge(alpha = .5)
model.fit(X, y)

print model.coef_
```

```Python
from sklearn.linear_model import RidgeCV

model = RidgeCV(alphas=[0.1, 1.0, 10.0])
model.fit(X,y)

print model.coef_
print model.alpha_
```
