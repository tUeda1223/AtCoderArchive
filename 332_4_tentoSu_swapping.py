## (input)
# N = input()
# S = int(input())
# A, B = map(int,input().split())
## (Reference)
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14
# https://harinez2.hateblo.jp/entry/atcoder-template-python
## input() for debug mode
import os, itertools
import numpy as np
if os.path.exists('input.txt'):
    r = open('input.txt','r')
    def input():
        return r.readline()
    from pdb import set_trace as test
def IIn(): return int(input().rstrip())
def SIn(): return input().rstrip()
def LIIn(): return list(map(int,input().rstrip().split()))
def LSIn(): return list(input().rstrip().split())

H,W = LIIn()
def check(A,B):
    return np.all(A==B)
A = np.array([LIIn() for h in range(H)])
B = np.array([LIIn() for h in range(H)])
c = 10**20
for h in itertools.permutations(range(H)):
    for w in itertools.permutations(range(W)):
        if check(B,A[tuple([h])][:,tuple([w])][:,0]):
            tmp = sum([[h[n] > h[i] for i in range(n+1,H)].count(True) for n in range(H-1)]) + sum([[w[n] > w[i] for i in range(n+1,W)].count(True) for n in range(W-1)])
            c = tmp if tmp < c else c
print(-1 if c == 10**20 else c)