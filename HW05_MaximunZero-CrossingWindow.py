import numpy as np

def sgn(val):
    if val < 0:return 1
    else: return 0

def main():
    t = int(input())
    while t > 0:
      try:
        first_line = input()
      except EOFError:
        break
      num, w_size = [int(x) for x in first_line.split(" ")]
      this_line = input().rstrip()
      numlist = [int(x) for x in this_line.split(" ")]
      zerocross_record = []
      zcr_array = np.array(zerocross_record)
      if w_size == 1 or w_size == 0: w_size = 2
      for i in range(len(numlist) - w_size + 1):
        zcr = 0
        for j in range(w_size-1):
          zcr += sgn(numlist[j+i]*numlist[j+i+1])
        zcr_array = np.append(zcr_array, zcr)
      maxpos = np.where(zcr_array == np.amax(zcr_array))
      print(maxpos[0][0]+1)
      t -= 1

main()