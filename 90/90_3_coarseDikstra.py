# https://atcoder.jp/contests/typical90/tasks/typical90_c
# import numpy as np
default = -1
def dikstra(D,start):
    # D: list of set
    # start: int 
    N1 = len(D)
    stack = [start]
    d = [-1 for n in range(N1)]
    d[start] = 0
    distance = -1
    while stack:
        dx = stack.pop()
        for dy in D[dx]:
            if d[dy] == default:
                d[dy] = d[dx]+1
                stack += [dy]
                distance = max(d[dy],distance)
        # print(d)
    return d, distance

N = int(input())
D = [set() for n in range(N+1)]
for n in range(N-1):
    x, y = map(int,input().split())
    D[x].add(y)
    D[y].add(x)
# print(D)
d,distance = dikstra(D,1)
start = d.index(max(d))
# print(d)
# print(distance)
# print(start)
D,distance = dikstra(D,start)
# print(D)
print(distance+1)