import sys
N = int(input())
A = list(map(int,input().split()))
cakeLength = sum(A)
if cakeLength%10 != 0:
    print('No')
    sys.exit()
cakeLengthPer10 = cakeLength//10
cum = [None]*N
c = 0
for n in range(N):
    c += A[n]
    cum[n] = c
# print(cum)
cumSet = set(cum)
for n in range(N):
    if (cum[n]+(cakeLengthPer10))%cakeLength in cumSet:
        print('Yes')
        sys.exit()
print('No')