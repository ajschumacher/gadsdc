# Linear Regression Assignment


### The Problem

In this assignment, we are going to recreate (in part) the Kaggle [competition](http://www.kaggle.com/c/job-salary-prediction) to predict salaries based on job descriptions. This problem came from a company called [Adzuna](http://www.adzuna.co.uk/), "The UK's Search Engine for Jobs, Property and Cars." They wanted to be able to predict the salary of a job based on it's description.


### The Data

We've pared down the problem a bit to make the dataset small and allow you to complete it in a reasonable amount of time. There are four [files available](https://github.com/ajschumacher/gadsdata/tree/master/salary).

1. `train.csv`
2. `location_tree.txt`
3. `test.csv`
4. `solution.csv`

You can treat `train.csv` and `location_tree.txt` as the only data available to you for model development. `location_tree.txt` has a fairly simple but non-standard format for the a hierarchy of UK locations. You may use it to generate suplemental features, or you may use just the features in `train.csv`. You want to predict `SalaryNormalized`.

The file `test.csv` represents data that your model would eventually be used on in production. (Someone inputs a job description on the Adzuna site, and your model provides an estimated salary.) So don't use the `test.csv` file in developing your model. When you have your final model done, you can make predictions for the rows in `test.csv`, and evaluate how well you've done using `solution.csv`.

The product that you submit should be an R markdown document including your documented code and any visualizations as appropriate. Include the final test set performance of your model!


### Possible steps

There are a lot of things you could try in this process. This will list some of them, in rough order of increasing difficulty. It is _not_ the case that you need to do all of these or do all of them in order.

 * Split the `train.csv` data into your own training and test sets. Use one as your training set and the other for validation. At the end you may train your final parameters on the full dataset.

 * Use cross-validation to evaluate your model performance. The `DAAG` `R` package includes `cv.lm` function which you might investigate. It may or may not be better than using your own.

 * Build an OLS-fitted linear regression model using available categorical variables. Try adding and dropping features and see if they improve the model. Try adding interaction effects to improve your model. (Note: Be aware of the computational overhead!)

 * Use `location_tree.txt` to add features to your data. Does this improve performance?

 * Use `grep` to add one-word features based on raw text to your data. Does this improve performance?

 * Use the `tm` package to create even more features based on text. You may want to restrict the number of features that this adds.

 * For all the feature engineering techniques you try, be sure to think about not just the training data, but the eventual test data.

 * Use the `glmnet` package to experiment with regularized fits. Can you improve performance this way?

 * If you're bored, jump ahead a little - try to fit a model using vowpal wabbit. (This is not an `R` technique - this component is _highly_ optional.)


### Note on `location_tree.txt`

If you're having trouble getting started with `location_tree.txt`, this might help:

```bash
cat location_tree.txt | sed 's/~/,/g' | sed 's/"//g' > location_tree.csv
```

This little hack will change "~" to a comma and remove quote marks. It still won't quite be a proper CSV file really, but it might be easier to work with this way.
