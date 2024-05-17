# https://atcoder.jp/contests/typical90/tasks/typical90_n
N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
A.sort()
B.sort()
C = [abs(a-b) for a,b in zip(A,B)]
print(sum(C))