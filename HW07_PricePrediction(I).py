import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def main():
    # Put your code below
    df = pd.read_csv("car-resale-price.csv")
    #print(df)
    test_size_input = float(input())
    random_state_input = int(input())
    
    features = ['km_driven', 'new_price', 'year', 'engine_power']
    X = df[features]
    y = df['resale_price']
    
    lregr = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_input, random_state=random_state_input) 
    
    lregr.fit(X_train, y_train)
    y_predict = lregr.predict(X_test)
    
    print("預測函數︰")
    #print(lregr.coef_) #predict function
    for i in range(4):
      print("{:.5f}*{:s}".format(lregr.coef_[i], features[i]), end="")
      if i != 3:print("+", end="")
    print("{:.5f}".format(lregr.intercept_))
    print("判定係數︰", end = "")
    #print(lregr.score(X, y))
    #r2_score(y, y_predict)
    print("{:.5f}".format(r2_score(y_test, y_predict)))
    print("均方誤差︰", end = "")
    print('%.5f'% mean_squared_error(y_test, y_predict))
    
main()