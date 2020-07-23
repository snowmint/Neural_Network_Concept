# import necessary packages here 
import numpy as np
from sklearn import datasets
from sklearn.tree import export_graphviz
import graphviz
import pydotplus
from IPython.display import Image  
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    # Put your code below
    
    test_size_input = float(input())
    random_state_input = int(input())
    criterion_input = input()
    deepth_input = int(input())
    random_state_tree_input = int(input())
    
    #read data
    iris = datasets.load_iris()
    
    #clip data
    iris.feature_names
    
    # use 'sepal length (cm)' and 'sepal width (cm)' as features
    X = iris.data[:,0:2]
    #print(X)
    y = iris.target
    #print(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=test_size_input,random_state = random_state_input) 
    
    #create decision tree classifier learning
    dt_clf = DecisionTreeClassifier(criterion = criterion_input, max_depth = deepth_input, random_state = random_state_tree_input)
    dt_clf.fit(X_train,y_train)
    y_pred = dt_clf.predict(X_test)
    
    #accuracy_score
    acc = accuracy_score(y_test, y_pred)
    print("{:.3f}".format(acc))
    
    dot_data=export_graphviz(dt_clf, out_file=None, feature_names=['sepal length (cm)','sepal width (cm)'])
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_png('tree1.png')
    Image(graph.create_png())
    
    #read data
    iris = datasets.load_iris()
    
    #clip data
    iris.feature_names
    
    # use 'petal length (cm)' and 'petal width (cm)' as features
    X = iris.data[:,2:4]
    #print(X)
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=test_size_input,random_state = random_state_input) 
    
    #create decision tree classifier learning
    dt_clf = DecisionTreeClassifier(criterion = criterion_input, max_depth = deepth_input, random_state = random_state_tree_input)
    dt_clf.fit(X_train,y_train)
    y_pred = dt_clf.predict(X_test)
    
    #accuracy_score
    acc = accuracy_score(y_test, y_pred)
    print("{:.3f}".format(acc))
    
    dot_data=export_graphviz(dt_clf, out_file=None, feature_names=['petal length (cm)','petal width (cm)'])
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_png('tree2.png')
    Image(graph.create_png())
    
    
main()