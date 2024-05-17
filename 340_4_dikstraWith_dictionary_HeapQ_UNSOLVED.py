# https://atcoder.jp/contests/abc340/tasks/abc340_d
## (input)
# N = input()
# S = int(input())
# A, B = map(int,input().split())
## (Reference)
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14
# https://harinez2.hateblo.jp/entry/atcoder-template-python
## input() for debug mode
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
import sys,heapq

def main():
    N = IIn()
    dics = [dict() for n in range(N)]
    for n in range(N-1):
        A, B, X1=LIIn()
        X = X1-1
        dics[n][n+1] = A
        dics[n][X] = B
    print(dijkstra(dics))

def dijkstra(dics,start=0):
    # (input)
    # dics: list of dic
    # (output)
    N = len(dics)
    visited = [False for n in range(N)]
    distance = [10**18 for n in range(N)]
    distance[start] = 0
    distanceCurrentQ = [(0,start)]
    while distanceCurrentQ:
        dist, current = heapq.heappop(distanceCurrentQ)
        if visited[current]:
            continue
        visited[current] = True
        for next, cost in dics[current].items():
            if visited[next]:
                continue
            distanceNextTmp = distance[current]+cost
            if distanceNextTmp < distance[next]:
                distance[next] = distanceNextTmp
                heapq.heappush(distanceCurrentQ ,(distanceNextTmp,next))
    return distance[-1]

if __name__ == '__main__':
    main()