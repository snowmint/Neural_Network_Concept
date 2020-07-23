import numpy as np

def main():
    # Put your python code below
    aList = []
    bList = []
    bList_array = np.array(bList)
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "#":
            break
        aList.append(line)

    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "#":
            break
        bList.append(line)
        count = [i for i,item in enumerate(aList) if line == item]
        if len(count) > 0:
            print(line,end=" ")
            print(len(count))
        else:
            print(line,end=" ")
            print("0")
    

main()