import itertools
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A = [a%46 for a in A]
B = [a%46 for a in B]
C = [a%46 for a in C]
# print(A)
# print(B)
# print(C)
counter = 0
tmpA = [A.count(n) for n in range(46)]
tmpB = [B.count(n) for n in range(46)]
tmpC = [C.count(n) for n in range(46)]
for X in itertools.product(set(A),set(B),set(C)):
    if sum(X)%46 == 0:
        counter += tmpA[X[0]] * tmpB[X[1]] * tmpC[X[2]]
print(counter)