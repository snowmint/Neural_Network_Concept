import numpy as np
import sys

def main():
    # Put your control code below
    while True:
        try:
            first_line = input()
        except EOFError:
            break
        t,k = part = [int(x) for x in first_line.split(" ")]

        array_input = np.arange(1, t+1)

        while True:
            if k == 0:
                break
            input_line = input()
            if input_line == '':
                break

            inp = input_line.split(" ")

            m = int(inp[0])
            n = int(inp[1])
            order = inp[2]
            change1 = int(inp[3])-1
            change2 = int(inp[4])-1

            array_input = array_input.reshape((m, n))
            
            if order == 'R':
                array_input[[change1, change2]] = array_input[[change2, change1]]
            
            if order == 'C':
                array_input[:,[change1, change2]] = array_input[:,[change2, change1]]
        
            k = k - 1
     
        array_input = array_input.flatten()
        ans = [str(x) for x in array_input]
        ans = " ".join(ans)
        print(ans)
        
main()