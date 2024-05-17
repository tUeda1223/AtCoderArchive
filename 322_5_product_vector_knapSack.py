# import numpy as np
from pdb import set_trace as test
import itertools, copy
# import bisect,collections,copy,heapq,itertools,math,numpy,string, sys
## (input)
# N = input()
# S = int(input())
# A, B = map(int,input().split())
## (Reference)
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14
# https://harinez2.hateblo.jp/entry/atcoder-template-python
# 

## input() for debug mode
# r = open('input.txt','r')
# def input():
#     return r.readline()

INF = 10**18+1

#def IIn(): return int(input().rstrip())
#def SIn(): return input().rstrip()
def LIIn(): return list(map(int,input().rstrip().split()))
#def LSIn(): return list(input().rstrip().split())
N,K,P = LIIn()
# N: test datas
# K: # of parameters
# P: minimum parameter value
C = [0 for n in range(N)]
A = [[] for n in range(N)]
for n in range(N):
    tmp = LIIn()
    C[n] = tmp[0] # (N)
    A[n] = tmp[1:] # (N x K)
C = [INF] + C
A = [[INF for k in range(K)]] + A
# print(C)
# print(A)

def hash(Vec,P):
    ret = 0
    for i,v in enumerate(Vec):
        ret += v*((P+1)**i)
    return ret

def listSub(A,B):
    C = [0 for i in range(len(A))]
    for i in range(len(A)):
        C[i] = A[i]-B[i]
    return C

def listMax(A,P):
    B = [0 for i in range(len(A))]
    for i in range(len(A)):
        B[i] = max(A[i],P)
    return B

E = [INF for _ in range((P+1)**K)]
E [0] = 0
for n in range(1,N+1): # of test datas
    Vectors = itertools.product(range(P+1),repeat=K)
    ETmp = copy.deepcopy(E)
    for nowVec in Vectors:
        hash1 = hash(nowVec,P)
        tmp1 = E[hash1]
        pastVec = listMax(listSub(nowVec,A[n]),0)
        hash2 = hash(pastVec,P)
        pastCost = E[hash2]
        tmp2 = pastCost+C[n]
        ETmp[hash1] = min(tmp1,tmp2)
    E = ETmp
nowVec = tuple([P for k in range(K)])
if E[-1] == INF:
    print(-1)
else:
    print(E[-1])