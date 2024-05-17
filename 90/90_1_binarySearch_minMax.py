# https://atcoder.jp/contests/typical90/tasks/typical90_a
def ceilDiv(A,B): return (A+B-1)//B
def isCut(A,L,x,K):
    # A: (list)
    # L: length
    # x: cut length
    # k: pieces
    A += [L]
    aBottom = 0
    k = 0
    for i,a in enumerate(A):
        aTmp = a-aBottom
        # print(aTmp)
        if aTmp >= x:
            aBottom = a
            k += 1
    return k >= K+1

N,L = map(int,input().split()) 
K = int(input())
A = list(map(int,input().split()))

left = 1
right = L
while(left+1 != right):
    middle = ceilDiv(left+right,2)
    if isCut(A,L,middle,K):
        left = middle
    else:
        right = middle
print(left)