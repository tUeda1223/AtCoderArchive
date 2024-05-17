import sys
K = int(input())
MAX = 10**9+7
if K%9 != 0:
    print(0)
    sys.exit()
D = [1 for k in range(K+1)]
for k in range(1,K+1):
    m = max(0,k-9)
    tmp = D[m:k]
    # print('%d, %s'%(k,tmp))
    D[k] = sum(D[m:k])
print(D[-1]%MAX)