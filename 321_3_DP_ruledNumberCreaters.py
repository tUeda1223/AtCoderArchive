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
K = IIn()
if K <= 9:
    print(K)
else:
    Q = collections.deque(range(1,10))
    k = 9
    while(True):
        q = Q.popleft()
        q1 = q%10
        for d in range(q1):
            tmp = 10*q+d
            # print(tmp)
            Q.append(tmp)
            k += 1
            if k == K:
                print(tmp)
                sys.exit()
