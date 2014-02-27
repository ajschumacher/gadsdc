# TODO: Fix this up (it's a mess)

# Regression Assignment


##The Problem
In this assignment, we are going to recreate the Kaggle competition to predict salaries based on job descriptions: http://www.kaggle.com/c/job-salary-prediction.  This problem came from a company called [Adzuna](http://www.adzuna.co.uk/), that wanted to be able to predict the salary of a job just based on it's description.

##The Data
We've paired down the problem a bit to make the dataset small and allow you to complete it in a  week.  There are 5 important files available.

1. [train.csv](https://www.dropbox.com/s/i80k8nx540i5qiy/train.csv)
2. [train_50k.csv](https://www.dropbox.com/s/ddla4rp5ivw1r4l/train_50k.csv)
3. [train_100k.csv](https://www.dropbox.com/s/cwtmswdz8qvey9o/train_100k.csv)
4. [train_200k.csv](https://www.dropbox.com/s/lztl58jddpovyxv/train_200k.csv)
5. [test.csv](https://www.dropbox.com/s/dq9e0dftcb6jw8q/test.csv)
6. [Location_Tree.csv](https://www.dropbox.com/s/lf2if5gb31vq76y/Location_Tree.csv)

(Available here : https://github.com/arahuja/GADS4/tree/master/data/kaggle_salary)

The first four files are files you can train you models on, start by using train.csv.  It contains 10k training examples, but the larger files may start to slow down your system requiring you to wait longer while the model trains.  They contain the following columns:

The test files contains all but the final two columns (the salary information)

At the end you will submit your best predictions for the test file, in the format
```
Id, Salary
1234, 77999
2345, 88999
```

Also please submit a commented R file with some of the things you tried.

##Assignment
At any point in the following steps you can use your model to predict salaries on the final test set and submit. 
Some bullets have stars and rank from Basic (no star) to Challenging (3 stars)
* * - 1 star - Try these out but they will be harder
* ** - 2 stars - For those looking for a challenge or really explore the topic
* *** - 3 stars - Test out some of the ideas using different tools a

1) Split the data into training and test sets (using one of the files 1-4 above).  You will use one as your training set and the other for validation.  At the end you may train your final parameters on the full dataset.

2) Build a simple linear regression using the available categorical variables.  Try adding and dropping parameters and see if they improve the model.  Try adding interaction effects to improve your model. (Note: beware of the computational overhead) Compare both R-squared and MAE on your test set. 

3) Install DAAG

**UPDATE : Try out cv.lm, but it will just train (or run) your model on different splits of training and test, but it won't let you retrieve MAE or MSE easily.**

Instead if you do part 5, please try out cv.glmnet.

```R
install.packages('DAAG')
library('DAAG')
```
Use the `cv.lm` command to see if that can improve your model.  This will run cross-validation.

4) Merge Location_Tree.csv on to your dataset - do any features from here improve performance.

**Update: to convert this file to a csv try using shell commands:**

```sh
cat Location_Tree.csv | sed 's/~/,/g' | sed 's/"//g' > Location_Tree2.csv
```
This command will change the ~ to a comma and remove the quote marks.
Note: DO NOT redirect this to the same file, using `>` on a file that exists will wipe it

*5) Using the GLMnet package, try `glm` and `cv.glmnet` to see if you can build a better model.

[Guide For cv.glmnet](http://www.inside-r.org/packages/cran/glmnet/docs/cv.glmnet)

$lambda.min will be available in a model trained with cv.glmnet.

**6) Now let's try adding some text features 
```R
install.packages('tm')
library('tm')

src <- DataframeSource(data.frame(data$Title)) # You can use any of the text columns, not just Title.
c <- Corpus(src)
?DocumentTermMatrix #This creates a matrix of 1/0 values with a row for each description and column for each word.  The value is 1 if the Title contains word.  Try out the different parameters.
dtm<- DocumentTermMatrix(c)

#Here I am creating a column for an 'Analyst' feature which is 1 if the title says analyst and 0 otherwise.  I am also creating an 'Engineering' column.
text_data <- cbind(data, as.matrix(dtm[,'analyst']), as.matrix(dtm[,'engineering']))
new_model <- model ( ... ~ ...  + analyst + engineering, data = text_data)
```
**7) If you were just loading the train.csv file so far, try loading one of the large datasets.  Does the larger dataset improve performance on the held-out?  If possible, try loading an even larger file.

***8) Let's try using the largest dataset, but using a faster package than R.
```sh
git clone git://github.com/JohnLangford/vowpal_wabbit.git
cd vowpal_wabbit
make install
```
Create a training file for vowpal wabbit using your favorite scripting language, the format should be as follows:
```sh
<salary> | This is a text feature | Some other feature | Job Title | 
```
Use the `|` to separate features.  Vowpal Wabbit will handle turning these into dummy variables automatically.  Let's assume you've named your new files `train.vw`

[Vowpal Wabbit Examples](https://github.com/JohnLangford/vowpal_wabbit/wiki/Examples)
[Vowpal Wabbit Input Validator](http://hunch.net/~vw/validate.html)

Try the following:
```sh
vw -c -k train.vw --loss squared -f model
vw -c -k train.vw --loss squared -f model -l1 0.0001 ##for l1 loss
vw -c -k train.vw --loss squared -f model -l2 0.0001 ## for l2 loss

vw -c -k -t test.vw -i model -p test.predictions
```

Load `test.predictions` into R to compute MAE.
