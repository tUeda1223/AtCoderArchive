# https://atcoder.jp/contests/typical90/tasks/typical90_p
MAX = 10000
N = int(input())
A,B,C = map(int,input().split())
num = 9999
for c in range(0,MAX):
    for b in range(0,MAX):
        Ncur = b*B+c*C
        if Ncur == N:
            num = min(num,b+c)
        elif N>Ncur:
            if (N-Ncur)%A==0:
                a = (N-Ncur)//A
                num = min(num,a+b+c)
print(num)