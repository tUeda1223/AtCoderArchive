import numpy as np
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
A = np.array(A) # (N x 2)
# print(A)
ind = np.argsort(A[:,1])[::-1]
A = A[ind]
# print(A)
score = 0
flavor1 = A[0,0]
score1 = A[0,1]
for n in range(1,N):
    flavor2 = A[n,0]
    score2 = (A[n,1]//(2 if flavor1 == flavor2 else 1))
    scoreTmp = score1 + score2
    score = max(scoreTmp,score)
    # print(score2)
    # print(scoreTmp)
    # print('---')
print(score)