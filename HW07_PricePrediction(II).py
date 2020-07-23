import numpy as np
import pandas as pd
import itertools
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def main():
    # Put your code below
    df = pd.read_csv("car-resale-price.csv")
    #print(df)
    test_size_input = float(input())
    random_state_input = int(input())
    
    score_most_high = []
    features = ['km_driven', 'new_price', 'year', 'engine_power']
    X = df[features]
    y = df['resale_price']
    comb_features_list = []
    comb_features = itertools.combinations(features, 2)
    comb_features_list = list(comb_features)
    #print(comb_features_list)
    
    max_score = 0.0
    max_feature = []
    for i in range (6):
      lregr = LinearRegression()
      features_in = [comb_features_list[i][0], comb_features_list[i][1]]
      X = df[features_in]
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_input, random_state=random_state_input) 
      lregr.fit(X_train, y_train)
      y_predict = lregr.predict(X_test)
      now_score = r2_score(y_test, y_predict)
      #print(features_in, end="")
      #print(now_score)
      score_most_high.append(now_score)
      if now_score > max_score : 
          max_score = now_score
          max_feature = features_in
    
    #print("max", max_score)
    #print("max_feature", max_feature)
    
    X = df[max_feature]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_input, random_state=random_state_input) 
    lregr.fit(X_train, y_train)
    y_predict = lregr.predict(X_test)
    now_score = lregr.score(X, y)
    
    print("預測函數︰")
    #print(lregr.coef_) #predict function
    for i in range(2):
      if i != 0 and lregr.coef_[i] > 0 : print("+", end="")
      print("{:.5f}*{:s}".format(lregr.coef_[i], max_feature[i]), end="")
    
    if lregr.intercept_ > 0 : print("+", end="")  
    print("{:.5f}".format(lregr.intercept_))
    print("判定係數︰", end = "")
    #print(lregr.score(X, y))
    #r2_score(y, y_predict)
    print("{:.5f}".format(r2_score(y_test, y_predict)))
    print("均方誤差︰", end = "")
    print('%.5f'% mean_squared_error(y_test, y_predict))
    
main()