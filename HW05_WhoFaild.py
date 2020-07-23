import numpy as np
import pandas as pd

def shuffle(r):
    for i in range(len(r)):
        j = np.random.randint(len(r))
        r[i], r[j] = r[j], r[i]

def genNames(n):
    dfName = pd.read_csv("input.txt", header=None)
    names = []
    rng = list(range(len(dfName)))
    shuffle(rng)
    for i in range(n):
        names.append(dfName[0][rng[i]])
    return names

def gencsv():
    seed, n = map(lambda x: int(x), input().split())
    np.random.seed(seed)
    dic={'姓名':genNames(n),
         '英文':np.random.randint(np.random.randint(0,51), 101, n),
         '離散':np.random.randint(np.random.randint(0,51), 101, n),
         '機率':np.random.randint(np.random.randint(0,51), 101, n),
         '程設':np.random.randint(np.random.randint(0,51), 101, n),
         '奧賽':np.random.randint(np.random.randint(0,51), 101, n)}
    df = pd.DataFrame(dic)
    df.to_csv('score.csv', index=False)

def main():
    gencsv()
    df = pd.read_csv("score.csv")
    print(df.loc[(df[list(df)].iloc[0:,1:].apply(func=lambda row: row.between(left=0, right=59).sum(), axis=1) >= 3)].iloc[0:,0:1].to_string(header = False, index = False))
    
main()