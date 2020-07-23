import numpy as np
import pandas as pd

def genSample():
    df_temp = pd.read_csv('input.txt', header=0, index_col=0)
    df_temp.columns=["Temp"]
    df_temp.index = pd.to_datetime(df_temp.index)
    seed= int(input())
    np.random.seed(seed)
    scale = np.random.randint(1,13)
    scrstr = str(scale)+'D'
    df_down = df_temp.resample(scrstr).sum()
    df_down.reset_index(inplace=True)
    df_down.dropna(inplace=True)
    df_down.drop('Date', axis=1, inplace=True)
    df_down.to_csv('sample.csv', header=False, index=False)
#end genSample

# 以上程式請勿進行更改

def main():
    genSample()
    # 將你的程式碼至於下方，以上程式請勿進行更改
    df = pd.read_csv("sample.csv", header=None, names=['value'])
    #做滑動平均
    df_rolling=df.rolling(window=10).mean()
    s_rolling = df_rolling.value
    access = np.array([])
    for i in range(1, s_rolling.count()-1):
        access = np.append(access, s_rolling.autocorr(lag=i))
    s_rolling = pd.Series(access)
    ld = s_rolling.diff(1).apply(lambda x: 0 if np.isnan(x) else x)
    rd = s_rolling.diff(-1).apply(lambda x: 0 if np.isnan(x) else x)
    #第一個 local max 就應該是週期了
    localmax = (ld > 0) & (rd > 0)
    indexlocalmax = list(filter(lambda i: localmax[i], localmax.index))
    print(indexlocalmax[0])
main()