# Yelp Review Sentiment Predictor


## Example

The user can specify which type of classification to perform (positive/negative or 5-star), which technique to use (Naive Bayes, SVM, or Logistic Regression), and how much data to use.

Assuming you have the Yelp review dataset in the same directory as `classify.py`, the following will build a Logistic Regression classifier for 5-star classification using 80% of the data:

```
classify.py svm False 80
```

In general, the classifier is used as follows:

```
classify.py <nb/svm/lr> <True/False> <number in [0, 100]>
```

where `True` indicates positive/negative classification, and `False` indicates 5-star classification.



