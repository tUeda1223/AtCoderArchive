## (input)
# N = input()
# S = int(input())
# A, B = map(int,input().split())
## (Reference)
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14
# https://harinez2.hateblo.jp/entry/atcoder-template-python
## input() for debug mode
import numpy as np
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

N,S,M,L = LIIn() 
# N: number of egg
# S: cost of egg 6 
# M: cost of egg 8
# L; cost of egg 12
costMin = 1e20
for NS in range(20):
    for NM in range(20):
        for NL in range(20):
            num = 6*NS + 8*NM + 12*NL
            if num >= N:
                cost = S*NS+M*NM+L*NL
                if cost < costMin:
                    costMin = cost
                    # print('%s, %s, %s'%(NS,NM,NL))
print(costMin)