# 4aEw1YZ2xmcrEk6d
Predict Customer Happiness

Models used:  

(1)  Logistic Regression
(2)  Decision Tree Classification 

dataset: happinessSurvery2020.csv

Correlation Matrix:

![image](https://github.com/sureshk76/4aEw1YZ2xmcrEk6d/assets/18317652/f3084738-b46c-4fc6-8bdf-dc498e875331)

Multicollinearity Analysis:

![image](https://github.com/sureshk76/4aEw1YZ2xmcrEk6d/assets/18317652/e049550b-d039-455d-95fb-cb14e346c211)

Data Analysis:
X1 = my order was delivered on time
X2 = contents of my order was as I expected
X3 = I ordered everything I wanted to order
X4 = I paid a good price for my order
X5 = I am satisfied with my courier
X6 = the app makes ordering easy for me

Upon looking at the descriptions, X3, X4 X6 does not seem to be directly related to logistics and delivery service.  More informtion on whether these features could be excluded as we are trying to predict the happiness with regards to logistics and delivery specifically needs to be made available.

X1, X2 and X5 are directly related to LAD(Logistics and delivery)

Upon looking at the correlation matrix, X1 followed by X5 seem to have stronger correlation with the target variable Y.  X2 seems to have negative but negligible correlation with Y.

X1-X5 have strong correlation with each other at 0.433
X1-X6 also have strong correlation with each other at 0.412
X3-X5 has the 3rd largest correlation at 0.358
X3-X4 correlation is at 0.303

These coorelation among indpendent features is greater than any other coorelation of a feature with the target/indepenent variable.  The Variance Inflaction Factor (VIF) does not indicate Multicollinearity though.

