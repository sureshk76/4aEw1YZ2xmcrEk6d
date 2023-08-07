#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np
import joblib

# split data
def split_data(df, testSize, randomState):
    X = df.drop('Y', axis=1).values
    y = df['Y'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testSize, random_state=randomState)
    data = {'train': {'X': X_train, 'y': y_train}, 'test': {'X': X_test, 'y': y_test}}
    return data

# train model
def train_model(data, args):
    reg_model = KNeighborsClassifier(**args)
    reg_model.fit(data['train']['X'], data['train']['y'])
    return reg_model

# get model metrics
def get_model_metrics(reg_model, data):
    preds = reg_model.predict(data["test"]["X"])
    accuracy = accuracy_score(data['test']['y'], preds)
    cm = confusion_matrix(data['test']['y'], preds)
    cr = classification_report(data['test']['y'], preds)
    return accuracy, cm, cr

def main():
    #Load Data

    df = pd.read_csv(r'../data/processed/happinessSurvey2020Processed.csv')

    #execute split data function to split data into training and testing set
    data = split_data(df, 0.15, 153)
    
    # example parameters
    args = { "n_neighbors" : 5, "metric" : 'minkowski', "p" : 2 }
    
    #train model on training set
    reg = train_model(data, args)
    
    # validate model
    accuracy, confusionMatrix, classificationReport = get_model_metrics(reg, data)
    print('Model Accuracy: ', accuracy)
    print('\nConfusion Matrix: \n', confusionMatrix)
    print('\nClassification Report: \n', classificationReport)
    
    # save Model
    model_name = "KNearestNeighbourModel.pkl"
    joblib.dump(value=reg, filename=model_name)

main()

