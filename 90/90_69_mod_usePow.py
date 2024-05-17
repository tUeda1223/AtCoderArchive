import sys
MAX = 10**9+7
N, K = map(int,input().split())
if K < 3:
    if N <= K:
        print(K)
    else:
        print(0)
    sys.exit()
else:
    D2 = (K*(K-1))%MAX
    if N == 1:
        print(K)
    elif N == 2:
        print(D2)
    else:
        D = (D2*(pow((K-2),(N-2),MAX)))%MAX
        print(D)