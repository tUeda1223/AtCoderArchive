import bisect,collections,copy,heapq,itertools,math,numpy,string, sys
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
N,X = LIIn()
A = LIIn()
Asort = sorted(A)
# print(Asort)
if N == 3:
    if min(A) < X:
        if X <= 100 and X <= max(A):
            print(X)
        else:
            print(-1)
    else:
        print(0)
else:
    scoreNow = sum(Asort[1:-1])
    # print(scoreNow)
    scoreAdd = X-scoreNow
    if scoreAdd <= min(A):
        print(0)
    elif scoreAdd > max(A):
        print(-1)
    else:
        print(scoreAdd)