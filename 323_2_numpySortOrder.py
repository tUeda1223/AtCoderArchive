import numpy as np
## (input)
# N = input()
# S = int(input())
# A, B = map(int,input().split())
## (Reference)
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14
# https://harinez2.hateblo.jp/entry/atcoder-template-python
## input() for debug mode
import os
if os.path.exists('input.txt'):
    r = open('input.txt','r')
    def input():
        return r.readline()
    from pdb import set_trace as test
def IIn(): return int(input().rstrip())
def SIn(): return input().rstrip()
def LIIn(): return list(map(int,input().rstrip().split()))
def LSIn(): return list(input().rstrip().split())


N = IIn()
A = [0 for n in range(N)]
for n in range(N):
    S = SIn()
    for m,s in enumerate(S):
        if s == '-':
            pass
        elif s == 'o':
            A[n] += 1
        elif s == 'x':
            pass
B = np.array([(A[n],(N-n)) for n in range(N)],dtype = [('score', int),('ID', int)])
I = np.argsort(B,axis=0,order=('score','ID'))[::-1]
# print(B)
# print(I)
str = '%d'%(I[0]+1)
for i in I[1:]:
    str += ' %d'%(i+1)
print(str)