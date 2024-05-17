# https://atcoder.jp/contests/typical90/tasks/typical90_g
import numpy as np
import bisect  
N = int(input())
A = [int(s) for s in input().split(' ')]
A.sort()
A = [-np.inf]+A+[np.inf] # -10*9+1 3200 4000 4400 5000 10*9+1
Q = int(input())
for q in range(Q):
    b = int(input())
    aIndex = bisect.bisect_left(A,b)
    # print(aIndex)
    print(min(abs(A[aIndex]-b),abs(A[aIndex-1]-b)))