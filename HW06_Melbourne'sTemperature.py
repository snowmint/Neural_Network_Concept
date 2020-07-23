# Import packages
import numpy as np
import pandas as pd
import datetime
import math
# You can define some functions here

def main():
    # Put your code below
    web = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"
    df_temp = pd.read_csv(web, header=0, parse_dates=True)
    df_temp['Date'] = pd.to_datetime(df_temp['Date'])
    df_temp['month'] = pd.DatetimeIndex(df_temp['Date']).month
    monthName = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    while True:
        try:
            input_line = input()
        except EOFError:
            break
        
        inp = input_line.split(" ")
        startyear = int(inp[1])-1
        start_date = str(startyear)+"-12-31"
        end_date = inp[2]+"-12-31"
        mask = (df_temp['Date'] > start_date) & (df_temp['Date'] <= end_date)
        dateinrange = df_temp.loc[mask]
        if inp[0] == "1":
            print(" 月   均溫")
            for i in range(1,13):
              maskJ = (df_temp['month'] == i)
              dateJ = dateinrange.loc[maskJ]
              sumJ = dateJ.sum(axis = 0)
              dateJ.set_index('Date', inplace=True)
              dateJ.index = pd.to_datetime(dateJ.index)
              meanJ = dateJ.mean(axis = 0)
              rowJ, colJ = dateJ.shape
              sumOfMonth = round(sumJ['Temp'], 1)
              ans = sumOfMonth/rowJ
              down3is5 = math.floor(meanJ['Temp']*1000%5)
              if down3is5 != 0 : print("{:s}{:7.2f}".format(monthName[i-1], round(meanJ['Temp'], 2)))
              else : print("{:s}{:7.2f}".format(monthName[i-1], round(meanJ['Temp']+0.0001, 2)))
        if inp[0] == "2":
            print(" 月 最低溫")
            for i in range(1,13):
              maskJ = (df_temp['month'] == i)
              dateJ = dateinrange.loc[maskJ]
              minJ = dateJ.min(axis = 0)
              rowJ, colJ = dateJ.shape
              print("{:s}{:7.2f}".format(monthName[i-1], minJ['Temp']))
        if inp[0] == "3":
            print(" 月 最高溫")
            for i in range(1,13):
              maskJ = (df_temp['month'] == i)
              dateJ = dateinrange.loc[maskJ]
              maxJ = dateJ.max(axis = 0)
              rowJ, colJ = dateJ.shape
              print("{:s}{:7.2f}".format(monthName[i-1], maxJ['Temp']))
        
        print()

main()