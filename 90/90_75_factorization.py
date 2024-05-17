import math
# https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
def factorization(n):
    arr = []
    temp = n
    sqrtTmp = math.ceil(math.sqrt(n)+1)
    # print('sqrt(n) = %d'%(sqrtTmp))
    for i in range(2, sqrtTmp):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
N = int(input())
arr = factorization(N)
count = 0
# print(arr)
for tmp in arr:
    count += tmp[-1]
if count == 0:
    print(0)
else:
    log2Count = int(math.ceil(math.log2(count)))
    print(log2Count)