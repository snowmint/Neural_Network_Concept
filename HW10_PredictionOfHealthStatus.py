# import some necessary packages here

# parameters: RandomForestClassifier(n_estimators=30, max_depth=10, random_state=1)

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier # Import Random Forest Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix 

def main():
    # Put your code below
    df = pd.read_csv("parkinsons.data")

    test_size_input = float(input())
    random_state_input = int(input())
    importance_input = int(input())
    
    features = df.columns[:]
    features = features.drop('name')
    features = features.drop('status')
    X = df[features]
    y = df['status']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_input, random_state=random_state_input)
    
    clf = RandomForestClassifier(n_estimators=30, max_depth=10, random_state=1)

    # Train Decision Tree Classifer
    clf.fit(X_train,y_train)
    
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    
    # output
    print("Classification report:")
    print(classification_report(y_test, y_pred))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    #===========first_time end=============#
    
    #print(clf.feature_importances_)
    feature_imp = pd.Series(clf.feature_importances_,index=features).sort_values(ascending=False)
    features = feature_imp.index[0:importance_input]
    #print(features)
    
    XX = df[features]
    y = df['status']

    XX_train, XX_test, yy_train, yy_test = train_test_split(XX, y, test_size=test_size_input, random_state=random_state_input)
    clf2 = RandomForestClassifier(n_estimators=30, max_depth=10, random_state=1)
    
    # Train Decision Tree Classifer
    clf2.fit(XX_train,yy_train)
    
    #Predict the response for test dataset
    yy_pred = clf2.predict(XX_test)
    
    # output
    #print("Classification report:")
    #print(classification_report(yy_test, yy_pred))
    
    #print("\nConfusion Matrix:")
    #print(confusion_matrix(yy_test, yy_pred))
    
    print("\nThe", importance_input, "most important features:")
    for i in range(importance_input):
        print(features[i])
    
main()