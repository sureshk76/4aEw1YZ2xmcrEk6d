<h1>Models predicting a Customer Satisfaction</h1>

<p><b>Description:</b> Building various machine learning models based on a very limited sample of customer survey to predict how happy the customer is with the services provided by the company using scikit learn.</p>

<p><b>Results: </b> the results of the models tried are as below and Decision tree classification seems to provide the best results.</p>

<b> Decision Tree Classification:</b>

Model Accuracy:  0.8076923076923077

Confusion Matrix: 
 [[13  2]
 [ 3  8]]

Classification Report: 
               precision    recall  f1-score   support

           0       0.81      0.87      0.84        15
           1       0.80      0.73      0.76        11

    accuracy                           0.81        26
   macro avg       0.81      0.80      0.80        26
weighted avg       0.81      0.81      0.81        26

<b> Support Vector Machine:</b>
Model Accuracy:  0.8421052631578947

Confusion Matrix: 
 [[7 3]
 [0 9]]

Classification Report: 
               precision    recall  f1-score   support

           0       1.00      0.70      0.82        10
           1       0.75      1.00      0.86         9

    accuracy                           0.84        19
   macro avg       0.88      0.85      0.84        19
weighted avg       0.88      0.84      0.84        19

<b> Random Forest:</b>
Model Accuracy:  0.8421052631578947

Confusion Matrix: 
 [[ 5  3]
 [ 0 11]]

Classification Report: 
               precision    recall  f1-score   support

           0       1.00      0.62      0.77         8
           1       0.79      1.00      0.88        11

    accuracy                           0.84        19
   macro avg       0.89      0.81      0.82        19
weighted avg       0.88      0.84      0.83        19

<b> K-Nearest Neighbours:</b>
Model Accuracy:  0.8421052631578947

Confusion Matrix: 
 [[ 5  2]
 [ 1 11]]

Classification Report: 
               precision    recall  f1-score   support

           0       0.83      0.71      0.77         7
           1       0.85      0.92      0.88        12

    accuracy                           0.84        19
   macro avg       0.84      0.82      0.82        19
weighted avg       0.84      0.84      0.84        19

<b> Logistic Regression:</b>
Model Accuracy:  0.8076923076923077

Confusion Matrix: 
 [[ 5  5]
 [ 0 16]]

Classification Report: 
               precision    recall  f1-score   support

           0       1.00      0.50      0.67        10
           1       0.76      1.00      0.86        16

    accuracy                           0.81        26
   macro avg       0.88      0.75      0.77        26
weighted avg       0.85      0.81      0.79        26

