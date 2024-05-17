# https://atcoder.jp/contests/typical90/tasks/typical90_h
# import numpy as np
denom = 7+10**9
N = int(input())
S = input()
template = '_atcoder'
D = [[0 for _ in range(len(template))] for _ in range(N+1)]
D[0][0] = 1
# print(np.array(D))
for nTmp,s in enumerate(S):
    n = nTmp + 1
    for m,sTmp in enumerate(template):
        # print('%d, %d'%(n,m))
        D[n][m] = D[n-1][m] + D[n-1][m-1]*(1 if s == sTmp else 0)
    # print(np.array(D))
# print(np.array(D))
print((D[-1][-1])%denom)