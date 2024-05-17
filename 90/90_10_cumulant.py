# https://atcoder.jp/contests/typical90/tasks/typical90_j
import numpy as np
N = int(input())
cumScore = np.zeros((2,N+1),'i8')
for n in range(1,N+1):
    cTmp, p = map(int,input().split())
    c = cTmp-1
    score = (p,0) if c == 0 else (0,p)
    score = np.array(score) 
    cumScore[:,n] = cumScore[:,n-1] + score
# print(cumScore)
Q = int(input())
for q in range(Q):
    startTmp,endTmp = map(int,input().split())
    start = startTmp-1
    end = endTmp
    cumStart = cumScore[:,start]
    cumEnd = cumScore[:,end]
    tmp = cumEnd-cumStart
    print('%d %d'%(tmp[0],tmp[1]))