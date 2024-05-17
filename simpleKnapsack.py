# import bisect,collections,copy,heapq,itertools,math,numpy,string, sys
## (input)
# N = input()
# S = int(input())
# A, B = map(int,input().split())
## (Reference)
# https://atcoder.jp/contests/abc032/tasks/abc032_d
## input() for debug mode
# import numpy as np
import sys,os
if os.path.exists('input.txt'):
    r = open('input.txt','r')
    def input():
        return r.readline()
    from pdb import set_trace as test
def IIn(): return int(input().rstrip())
def SIn(): return input().rstrip()
def LIIn(): return list(map(int,input().rstrip().split()))
def LSIn(): return list(input().rstrip().split())
def list2NP(matrix): import numpy as np; print(np.array(matrix))
INF = 10**18
N,W = LIIn()
VList = [None]*(N+1)
WList = [None]*(N+1)
VSum = 0
for n in range(1,N+1):
    VList[n],WList[n] = LIIn()
    VSum += VList[n]

def knapsack(VList,WList,W,N,VSum=None):
    # VList: value list 
    # WList: weight list 
    # W: max weights of knapsack
    # N: items
    if (VSum is None) or W < VSum:
        V = [[0 for w in range(W+1)] for n in range(N+1)]
        for n in range(1,N+1):
            v = VList[n]
            wTmp = WList[n]
            for w in range(1,W+1):
                wMin = max(w-wTmp,0)
                tmp1 = V[n-1][w]
                tmp2 = V[n-1][wMin]+v if wMin+wTmp <= w else 0
                V[n][w] = max(tmp1,tmp2)
        # list2NP(V)
        return V[-1][-1]
    else: # VSum <= W
        # Consider the minimum weight on the situations
        # 1. the maximum number of chose (n) is decided
        # 2. the total value (v) is decided.
        # The answer is written into WMin[n][v]
        WMin = [[0]+[INF for v in range(VSum)] for n in range(N+1)]
        for n in range(1,N+1):
            vTmp = VList[n]
            w = WList[n]
            for v in range(1,VSum+1):
                vSub = v-vTmp
                tmp1 = WMin[n-1][v]
                if vSub >= 0:
                    tmp2 = WMin[n-1][vSub]+w
                    WMin[n][v] = min(tmp1,tmp2)
                else:
                    WMin[n][v] = tmp1
        # list2NP(WMin)
        vMax = 0
        for v in range(VSum+1):
            vMax = v if WMin[-1][v] <= W else vMax
        return vMax