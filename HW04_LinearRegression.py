import numpy as np
from math import pow

def linearRegression(x, y):
    a = np.vstack((x, np.ones(x.size))).T
    pseudoInverse = np.linalg.inv(a.T@a)@a.T
    return pseudoInverse@y

def main():
    input_x = np.array(input().split(", ")).astype(float)
    input_y = np.array(input().split(", ")).astype(float)
    totalSize = input_x.size

    # calculate coefficient
    a, b = linearRegression(input_x, input_y)
    print("{:.3f} {:.3f}".format(a, b))

    # calculate MSSE(Minimum Sum Square Error)
    sum = 0
    opList = list()
    for counter in range(0, totalSize):
        predictRes = input_x[counter] * a + b
        error = (predictRes) - input_y[counter]
        tmp = pow(error, 2)
        sum += tmp
        opList.append([input_x[counter], predictRes, input_y[counter], error, counter])
    print("{:.3f}".format(sum / totalSize))

    # output
    #
    sortedarr = np.array(opList)
    #print(sortedarr.shape)
    sortedarr = sortedarr[np.argsort(sortedarr[:,0])]
    row, col = sortedarr.shape
    for i in range(row):
        for j in range(col-1):
            if j < col-2:
                print("{:.3f}".format(sortedarr[i][j]), end=" ")
            else :
                print("{:.3f}".format(sortedarr[i][j]))

    #opList.sort(key=lambda x: (x[0], x[3]))
    #for element in opList:
    #    print("{:.3f} {:.3f} {:.3f} {:.3f}".format(*element), sep=' ')


main()