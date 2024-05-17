## (input)
# N = input()
# S = int(input())
# A, B = map(int,input().split())
## (Reference)
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14
# https://harinez2.hateblo.jp/entry/atcoder-template-python
## input() for debug mode
import os
import numpy as np
if os.path.exists('input.txt'):
    r = open('input.txt','r')
    def input():
        return r.readline()
    from pdb import set_trace as test
def IIn(): return int(input().rstrip())
def LIIn(): return list(map(int,input().rstrip().split()))

N = IIn()
A = LIIn()
AWithInd = np.array([(A[n],(n)) for n in range(N)],dtype=[('value',int),('ind',int)]) # (N x 2)
AWithInd.sort(axis=0,order='value')
AWithInd = AWithInd[::-1]
aBefore = 1e20
cum = 0
CIndBefore = 0
ret = 0
C = [None]*N # C = [0 for _ in range(N)]
for aTmp in AWithInd:
    a = aTmp[0]
    ind = aTmp[1]
    # print('%d, %d'%(a,ind))
    if a < aBefore:
       C[ind] = cum 
       CIndBefore = cum
    else:
        C[ind] = CIndBefore
    cum += a
    aBefore = a
print(*C)
## Slower version
# text = ''
# for c in C:
#     text += '%d '%(c)
# print(text)