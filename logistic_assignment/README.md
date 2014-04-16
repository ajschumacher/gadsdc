### Mid-course Data Science Assignment Rubric

# Logistic Regression

### Assignment prompt

Create a logistic regression model using several independent variables. Explain what the model might predict, and why it is relevant to this data set. You may use your own dataset, find one from the [UCI Machine Learning Repositor](http://archive.ics.uci.edu/ml/) or another source, or use the automotive [lemons](https://github.com/ajschumacher/gadsdata/tree/master/lemons) dataset.

As with the linear regression exercise, you can pick your data set, but please either include it with your submission or provide a URL where it can be download. We encourage you to try exploring a different data set from what you did in the linear regression assignment because it's useful to get comfortable processing and parsing different data sets.

This assignment is graded from a score of 0-100. You will be expected to submit the dataset (or a link to it), and the files containing code that creates a logistic regression model using several independent variables, as well as an explanation on your motivation for selecting the dataset and feature set.

[Basic example solution](https://github.com/dennisobrien/GeneralAssemblyDataScience2013/tree/master/HomeworkAssignment_01)

### Rubric

 * Student has selected a dataset suitable for the assignment (20pts)
     * The dataset must be large enough to require training a model, but must not be too large to reproduce its analysis on a single laptop.
     * It must have at least five independent features.
     * The dataset must be appropriate for a binary classification problem.
     * The student has explained why he/she has chosen this dataset, and problem.

 * Student has run a logistic regression on the dataset (50pts)
    * A fitted logistic regression model must be created.
    * Output including coefficient values, standard errors, and residuals should be generated.
    * The student must be able to push new data points through the model to get regression scores.
    * The model results must be reproducible (i.e. for all steps requiring some random aspect, a suitable random seed was set).

 * Student has made a thorough attempt to diagnose accuracy/precision of the model (20 pts)
     * The student has evaluated accuracy and precision through an ROC curve.
     * The student has at least split the dataset into a training/test set to validate OOS error.
     * The student has written a cross-validation framework to train multiple logistic regression models to inform model design.
     * The student has described (in prose) the model and its performance, as well as next steps on how to improve these metrics.

 * Student has visualized results, and written up a 1-2 page report on approach, results, conclusions, and next steps. (10pts)
     * Student has taken the time to formulate a report in human-readable english (as opposed to code only).
     * Student has made a genuine attempt to explain the intuition behind selecting their particular dataset, as well as why its features would be predictive in a logistic regression.
     * Student has visualized either the data and results in a meaningful way that communicates analysis and critical thought.

### Grade levels

 * _90-100_: Student has demonstrated all competencies and exceeded all expectations for the assignment. Student has clearly explained all steps of the data science process, in a manner that is accessible and informative even to nontechnical audiences. Data visualizations are easy to understand, and provide further insight into student's thought process. Analyses in this grade range are suitable for production-level work or publication.

 * _80-90_: Student has demonstrated competency for all assignment expectations. Student has explained most to all steps of the data science process, in a manner that is at least understandable to technical audiences. Data visualizations add material value to analysis.

 * _70-80_: Student has demonstrated technical ability and has met expectations for this assignment. Student has written code for all steps of the data science process, although may or may not have explained in their report what all the steps were. Data visualizations are missing or contribute little.

 * _60-70_: Student has shown promise of technical ability for this assignment. Student is missing some steps of the data science process that could materially change their results. There are no data visualizations or data visualizations are difficult to understand.

 * _50-60_: Student has provided a promising start to the assignment. Student is missing several steps of the data science process that could materially change results. There are no data visualizations, or the few data visualizations that exist actually hamper understanding of their analysis. There is no evidence of an understanding outside of technical implementation.

 * 0-50: Student has not demonstrated any serious facilities with modeling a dataset, explaining its processes, and analyzing its results.
