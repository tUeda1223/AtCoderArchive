# import bisect,collections,copy,heapq,itertools,math,numpy,string, sys
## (input)
# N = input()
# S = int(input())
# A, B = map(int,input().split())
## (Reference)
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14
# https://harinez2.hateblo.jp/entry/atcoder-template-python
# 
def IIn(): return int(input().rstrip())
def SIn(): return input().rstrip()
def LIIn(): return list(map(int,input().rstrip().split()))
def LSIn(): return list(input().rstrip().split())

N,M = LIIn()
A = LIIn()
n = 1
for m in range(M):
    fireDate = A[m]
    while(n<=fireDate):
        print(A[m]-n)
        n += 1