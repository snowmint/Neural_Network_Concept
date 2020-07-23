# import some packages here
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd

def main():
    # Put your code below
    
    #np.random.seed(0)
    #x1 = np.random.rand(50)*100 #x1 0~100
    #x2 = np.random.rand(50)*10  #x2 0~100
    #X = np.vstack((x1, x2)).T
    #y = np.array([1 if x<5 else 0 for x in x2])
    
    #=====================================
    df = pd.read_csv("social_Network_Ads.csv")
    #print(df)
    test_size_input = float(input())
    random_state_input = int(input())
    k_nearest_input = int(input())
    
    features = ['Age', 'EstimatedSalary']
    X = df[features]
    y = df['Purchased']
    #print(X)
    #print(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_input, random_state=random_state_input)
    
    #=====================================
    
    knn_clf = KNeighborsClassifier(n_neighbors = k_nearest_input)
    knn_clf.fit(X_train, y_train)#KNN 學習機
    #plot_pred_with_clf(X_train, y_train, X_train, y_train, knn_clf, 'K-NN (Training set)')
    #plot_pred_with_clf(X_train, y_train, X_test, y_test, knn_clf, 'K-NN (Test set)')
    
    y_pred2 = knn_clf.predict(X_test)
    print("Classification report using raw data:")
    print(classification_report(y_test,y_pred2))
    knn_clf.score(X_test, y_test)
    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred2))
    print("")
    #=====================================

    ss = StandardScaler()
    Xs_train = ss.fit_transform(X_train)
    Xs_test = ss.transform(X_test)
    knn_clf.fit(Xs_train, y_train)
    #plot_pred_with_clf(Xs_train, y_train, Xs_train, y_train, knn_clf, 'K-NN (Scaled Training set)')
    #plot_pred_with_clf(Xs_train, y_train, Xs_test, y_test, knn_clf, 'K-NN (Scaled Test set)')
    
    y_pred3 = knn_clf.predict(Xs_test)
    print("Classification report using scaled data:")
    print(classification_report(y_test,y_pred3))
    knn_clf.score(X_test, y_test)
    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred3))
    
    #=====================================
    

main()