import math
# 不要使用numpy套件

def main():
    # Put your code below
    input_dim_n = int(input())
    expect_output_d = int(input()) # 0 or 1
    weight = [float(n) for n in input().split()]
    input_signal = [float(n) for n in input().split()]
    learning_speed_n = float(input())
    #print(weight)
    #print(input_signal)
    
    sum = 0
    for i in range(input_dim_n):
      sum += weight[i]*input_signal[i]
    
    net = sum - weight[input_dim_n] #net = sum - bias
    y = 1 / (1 + math.exp(-net))
    #E = ((expect_output_d - y)*(expect_output_d - y)) / 2
    #print(E)
    
    GED = list()
    for i in range(input_dim_n):
        partialE_partialWi = -1 * (expect_output_d - y) * y * (1-y) * input_signal[i]
        GED.append(partialE_partialWi)
    GED.append((-1) * (expect_output_d - y) * y * (1 - y) * (-1))

    for i in range(len(GED)):
      if i == len(GED)-1 : print("{:.6f}".format(GED[i]))
      else : print("{:.6f}".format(GED[i]), end=" ")
    
    for i in range(len(GED)):
        GED[i] *= (-1)*learning_speed_n
        if i == len(GED)-1 : print("{:.6f}".format(GED[i]))
        else : print("{:.6f}".format(GED[i]), end=" ")
    
main()