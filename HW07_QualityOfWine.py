from sklearn import datasets
from sklearn.model_selection import train_test_split
#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
#Import scikit-learn metrics module for accuracy calculation
from sklearn.metrics import accuracy_score

def main():
    #Put your code below
    test_size_input = float(input())
    random_state_input = int(input())
    
    wine = datasets.load_wine()
    #print(wine.feature_names)
    
    X = wine.data[:,:]
    y = wine.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_input, random_state = random_state_input) 
    
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    y_pred = gnb.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    print('Accuracy: ', end="")
    print("{:.5f}".format(acc))
    
main()