import math
# 不要使用numpy套件

def main():
    input_dim_n = int(input())
    #print(input_dim_n)
    expect_output_d = int(input()) # -1 to 1
    #print(expect_output_d)
    weight = [float(n) for n in input().split()]
    #print(weight)
    input_signal = [float(n) for n in input().split()]
    #print(input_signal)
    learning_speed_n = float(input())
    #print(learning_speed_n)
    sum = 0
    for i in range(input_dim_n):
      sum += weight[i]*input_signal[i]
    net = sum - weight[input_dim_n] #net = sum - bias
    #print("net : ",net)
    y = (2/(1 + math.exp(-2*net))) - 1
    #print("y : ",y)
    GED = list()
    
    #-0.602182
    exp_up2net = (1-y)/(y+1)
    sech_f = (4*exp_up2net)/((exp_up2net+1)*(exp_up2net+1))
    #print("exp_up2net : ", exp_up2net)
    #print("sech_f : ", sech_f)
    #-0.602182
    #exp_up2net = math.exp(-2*net)
    #sech_f = (4*exp_up2net)/((exp_up2net+1)*(exp_up2net+1))
    
    #-0.602182
    #sech_f = 2/((math.exp(net))+(math.exp(-1*net)))
    #sech_f *= sech_f
    
    for i in range(input_dim_n):
        partialE_partialWi = (expect_output_d - y)*( y * y - 1)* input_signal[i]# * (1.4967724)
        GED.append(partialE_partialWi)
    GED.append((expect_output_d - y) * (y * y - 1) * (-1))

    for i in range(len(GED)):
      if i == len(GED)-1 : print("{:.6f}".format(GED[i]))
      else : print("{:.6f}".format(GED[i]), end=" ")
    
    for i in range(len(GED)):
        GED[i] *= (-1)*learning_speed_n
        if i == len(GED)-1 : print("{:.6f}".format(GED[i]))
        else : print("{:.6f}".format(GED[i]), end=" ")
    
main()