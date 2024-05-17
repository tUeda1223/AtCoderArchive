import bisect
## (input)
# N = input()
# S = int(input())
# A, B = map(int,input().split())
## (Reference)
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14
# https://harinez2.hateblo.jp/entry/atcoder-template-python
# 表を用いて入出力を明記すること.
# 今までの累積和から新しいモノを生み出せないか考えること.
# 似非漸化式のような形に書き起こせないかを考えてみる. それが案外累積和で表現できるかもしれない.
# 無理にfor文で書かず, 展開したコードから帰納的にfor文にまとめるのも有効である.
# https://atcoder.jp/contests/abc321/tasks/abc321_d

def IIn(): return int(input().rstrip())
def SIn(): return input().rstrip()
def LIIn(): return list(map(int,input().rstrip().split()))
def LSIn(): return list(input().rstrip().split())
N,M,P = LIIn()
A = LIIn()
B = LIIn()

# N: main
# M: sub
# P: minCost
# A: Main
# B: Sub

AWithMinP = [min(a,P) for a in A]
# print(AWithMinP)
PMinusA = [P-a for a in AWithMinP]
PMinusASort = sorted(PMinusA)
# print(PMinusASort)
g = [0 for _ in range(N+1)]
g[0] = sum(AWithMinP)
g[1] = g[0] + N*PMinusASort[0]
for n in range(2,N+1):
    g[n] = g[n-1] + (N-n+1)*(PMinusASort[n-1]-PMinusASort[n-2])
# print(g)
S = 0
for b in B:
    i = bisect.bisect_left(PMinusASort,b)
    tmp1 = (N-i)
    tmp2 = (b-(PMinusASort[i-1] if i>0 else 0))
    # print(i)
    # print(g[i])
    # print(tmp1)
    # print(tmp2)
    tmp = g[i] + tmp1*tmp2
    # print(tmp)
    S += tmp
    # print('----')
print(S)