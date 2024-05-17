import sys
def f(x):
    ret = x
    for s in str(x):
        ret += int(s)
    return ret%10**5

N,K = map(int,input().split())
if N == 0:
    print(0)
    sys.exit()

NTmp = N+0
loopCounter = [0]*(10**5)
loopStart = 10**18
loopCount = 10**18
c = True
k = 0
while k < K:
    NTmp = f(NTmp)
    if loopCounter[NTmp] == 0:
        loopCounter[NTmp] = k
    else:
        if c:
            loopCount = k-loopCounter[NTmp]
            k += (loopCount)*((K-k)//loopCount-1)
            c = False
    k += 1
print(NTmp)