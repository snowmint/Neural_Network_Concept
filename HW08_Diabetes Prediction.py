# import some packages here
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

def main():
    # Put python code below
    #=====================================
    
    df = pd.read_csv("diabetes.csv")
    #print(df)
    test_size_input = float(input())
    random_state_input = int(input())
    
    features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    X = df[features]
    y = df['Outcome']
    #print(features)
    #print(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_input, random_state=random_state_input)
    
    #=====================================
    #newton cg
    #lbfgs
    logit_reg = LogisticRegression(solver='newton-cg', multi_class='auto')
    # Making a logistic regression model
    logit_reg.fit(X_train, y_train)
    y_pred = logit_reg.predict(X_test)
    print("Classification report:")
    print(classification_report(y_test,y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
main()