def main():
    # Put your code below
    pass
    input1 = [int(n) for n in input().split()]
    input2 = [int(n) for n in input().split()]
    m = input1[0]
    h = input1[1]
    n = input1[2]
    #print(input1)
    ans = 1
    sum = 0
    #print(input2)
    for i in range(len(input2)):
      if i == 0 : sum += (m*input2[i]) + input2[i]
      if i == h-1 : sum += (input2[i]*n) + n
      if i > 0 :
        sum += input2[i-1] * input2[i] + input2[i]
    total = sum
    print(total)
main()