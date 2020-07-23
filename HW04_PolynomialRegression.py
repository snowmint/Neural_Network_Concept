import numpy as np

def pr(n, x, y):
    A = np.vstack((x * x * x, x * x , x , np.ones(n))).T
    return np.linalg.inv(A.T@A)@A.T@y                                   # return beta

def main():
    # Put your code beloow
    readXY = 2
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
    
    input_line = input()
    inp = [float(x) for x in input_line.split(",")]
    inparrX = np.array(inp)
    
    input_line = input()
    inp = [float(x) for x in input_line.split(",")]
    inparrY = np.array(inp)
    
    a, b, c, d = pr(inparrX.size, inparrX, inparrY)
    print("{0:0.3f}".format(a) + " " + "{0:0.3f}".format(b) + " " + "{0:0.3f}".format(c) + " " + "{0:0.3f}".format(d))
    
    tmp = []
    tmp2 = []
    errorarr = np.array(tmp)
    function_yarr = np.array(tmp2)
    SumError = 0.0
    for i in range(inparrX.size) :
        function_y = float(a*inparrX[i]*inparrX[i]*inparrX[i] + b*inparrX[i]*inparrX[i] + c*inparrX[i] + d)
        error_i = float(inparrY[i]-(function_y))*-1.0
        function_yarr = np.append(function_yarr, float(function_y))
        errorarr = np.append(errorarr, float(error_i))
        SumError += error_i*error_i

    minsse = SumError/float(inparrX.size)
    print("{0:0.3f}".format(minsse))

    inparrX = inparrX.reshape(inparrX.size, 1).astype("float")
    function_yarr = function_yarr.reshape(inparrX.size, 1).astype("float")
    inparrY = inparrY.reshape(inparrX.size, 1).astype("float")
    errorarr = errorarr.reshape(inparrX.size, 1).astype("float")

    z = np.hstack((inparrX, function_yarr, inparrY, errorarr))
    sorted_array = z[np.argsort(z[:, 0])]
    row, col = sorted_array.shape;

    for i in range(row):
        for j in range(col):
            if j < sorted_array[i].size-1 :
                print ("{0:0.3f}".format(sorted_array[i][j]), end=" ")
            else :
                print ("{0:0.3f}".format(sorted_array[i][j]))
    
main()  