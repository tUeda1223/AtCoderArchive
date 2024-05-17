import sys
sys.setrecursionlimit(10 ** 9)
from operator import add
## (input)
# N = input()
# S = int(input())
N, M = map(int,input().split())
if N == 1 or M == 0:
    print('0 0')
    sys.exit()

dic = [{} for n in range(N+1)]
for m in range(M):
    A,B,X,Y = map(int,input().split())
    dic[A][B] = [X,Y]
    dic[B][A] = [-X,-Y]
C = ['undecidable' for n in range(N+1)]
C[1] = [0,0]

def func(A=1):
    # print(dic)
    # print(C)
    # print(A)
    for B, relativePosition in dic[A].items():
        # key: B (target)
        # relativePosition: list
        if C[B] == 'undecidable':
            C[B] = list(map(add,C[A],relativePosition))
            func(B)
func()
for c in C[1:]:
    if c == 'undecidable':
        print('undecidable')
    else:
        print('%d %d'%(c[0],c[1]))