# import necessary packages here 
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.tree import export_graphviz
import graphviz
import pydotplus
from IPython.display import Image  
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def main():
    # Put your code below
    df = pd.read_csv("pima-indians-diabetes.csv")
    #print(df)
    
    test_size_input = float(input())
    random_state_input = int(input())
    criterion_input = input()
    deepth_input = int(input())
    random_state_tree_input = int(input())
    
    #features = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
    features = df.columns[:-1]
    X = df[features]
    y = df['label']
    #print(X)
    #print(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_input, random_state=random_state_input)
    
    #create decision tree classifier learning
    dt_clf = DecisionTreeClassifier(criterion = criterion_input, max_depth = deepth_input, random_state = random_state_tree_input)
    dt_clf.fit(X_train,y_train)
    y_pred = dt_clf.predict(X_test)
    
    #accuracy_score
    acc = accuracy_score(y_test, y_pred)
    #print("{:.3f}".format(acc))
    print("Classification report:")
    if deepth_input <= 5 :
      dot_data=export_graphviz(dt_clf, out_file=None,filled = True, rounded = True, special_characters=True, feature_names=features, class_names=['0','1'])
      graph = pydotplus.graph_from_dot_data(dot_data)
      graph.write_png('diabetes_tree.png')
      #Image(graph.create_png())
    
    target_names = ['0', '1']
    print(classification_report(y_test, y_pred, labels=[0, 1]))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
main()