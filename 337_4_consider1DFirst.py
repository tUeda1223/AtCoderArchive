## (input)
# N = input()
# S = int(input())
# A, B = map(int,input().split())
## (Reference)
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14
# https://harinez2.hateblo.jp/entry/atcoder-template-python
## input() for debug mode
# https://atcoder.jp/contests/abc337/tasks/abc337_d
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

def main():
    # S = SIn()
    # A = LIIn()
    H,W,K = LIIn()
    S = [list(SIn()) for h in range(H)] # S[hIndex][wIndex]
    MAX = 10**9
    minCost = 10**9
    cumX = [0]*W
    cumD = [0]*W
    if K <= H:
        for h in range(H):
            for w in range(W):
                s = S[h][w]
                cumX[w] += 1 if s == 'x' else 0
                cumD[w] += 1 if s == '.' else 0
                if h >= K:
                    s = S[h-K][w]
                    cumX[w] -= 1 if s == 'x' else 0
                    cumD[w] -= 1 if s == '.' else 0
                if h >= K-1 and cumX[w] == 0:
                    minCost = min(cumD[w],minCost)
    cumX = [0]*H
    cumD = [0]*H
    if K <= W:
        for w in range(W):
            for h in range(H):
                s = S[h][w]
                cumX[h] += 1 if s == 'x' else 0
                cumD[h] += 1 if s == '.' else 0
                if w >= K:
                    s = S[h][w-K]
                    cumX[h] -= 1 if s == 'x' else 0
                    cumD[h] -= 1 if s == '.' else 0
                if w >= K-1 and cumX[h] == 0:
                    minCost = min(cumD[h],minCost)
    print(minCost if minCost != MAX else -1)

if __name__ == '__main__':
    main()