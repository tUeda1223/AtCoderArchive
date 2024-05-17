import math
from itertools import permutations; # import numpy as np
def isLike(x,y,S):
    return not ((x,y) in S or (y,x) in S)
N = int(input())
A = [list(map(int,input().split())) for n in range(N)]; # print(np.array(A))
M = int(input())
S = set()
for m in range(M):
    tmp = tuple(map(int,input().split()))
    S.add(tmp); # print(S)
score = math.inf
for P in list(permutations(range(N))):
    likeAll = True
    scoreTmp = 0
    for n in range(N-1):
        x = P[n]
        y = P[n+1]
        likeAll = likeAll and isLike(x+1,y+1,S)
        # A[i][j] ... jth course by ith person
        iTmp = P[n]; jTmp = n
        scoreTmp += A[iTmp][jTmp]
    if likeAll:
        iTmp = P[-1]; jTmp = -1
        scoreTmp += A[iTmp][jTmp]
        # print('%s, %d'%(P,scoreTmp))
        score = min(scoreTmp,score)
score = -1 if score == math.inf else score
print(score)