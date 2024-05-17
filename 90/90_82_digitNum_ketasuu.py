def mySum(m,M):
    # digit*(m + ... + M)
    # print(m)
    # print(M)
    assert len(str(m)) == len(str(M))
    digit = len(str(m))
    if m == M:
        return digit*M
    else:
        return digit*(M*(M+1)-m*(m-1))//2
MAX = 10**9+7
L, R = map(int,input().split())
lengthL = len(str(L))
lengthR = len(str(R))
# print(lengthL)
# print(lengthR)
count = 0
for digit in range(lengthL,lengthR+1):
    m = max(10**(digit-1),L)
    M = min(10**digit-1,R)
    count = (count + mySum(m,M))%MAX
print(count)