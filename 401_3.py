## (Reference)
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14
# https://harinez2.hateblo.jp/entry/atcoder-template-python
# Factorization: https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
# Yakusuu: https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
# Sosuu rekkyo https://qiita.com/wihan23/items/8aa52bcc4d9c45334b1c
##
# import bisect,collections,copy,heapq,itertools,math,numpy,string, sys
import sys,os, bisect
if os.path.exists('input.txt'):
    r = open('input.txt','r')
    def input(): return r.readline()
    from pdb import set_trace as test
def IIn(): return int(input().rstrip())
def SIn(): return input().rstrip()
def LIIn(): return list(map(int,input().rstrip().split()))
def LSIn(): return list(input().rstrip().split()) # '0 1 0' -> ['0','1','0']
def LSIn2(): return list(SIn()) # '010' -> ['0','1','0']
def main():
    # S = SIn()
    # A = LIIn()
    # X = [list(SIn()) for _ in range(H)] # X[h][w]
    # X = [[0 for _ in range(W)] for _ in range(H)] # X[h][w]
    N, K = LIIn()
    if N <= K:
        print(1)
        import sys; sys.exit()
    from collections import deque
    queue = deque()
    for n in range(K):
        queue.append(1)
    sum = K
    ten9 = 10**9
    for n in range(N-K):
        tmp = sum
        queue.append(tmp)
        left = queue.popleft()
        sum -= left
        sum = (sum + tmp)%ten9
        # print(queue)
    print((sum)%ten9)

def myFunc():
    return 0

################ Local functions ################
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def yesno(c): print('Yes' if c else 'No')
def gcd(a,b):
    while b: a, b = b, (a%b)
    return a
def lcm(a,b): return a * b // gcd(a, b)
def list2NP(matrix): import numpy as np; print(np.array(matrix))
def bisectLeft(List,value): return bisect.bisect_left(List,value)
def listAdd(A,B): return [a+b for a,b in zip(A,B)]
def listErr(A,B): return [abs(a-b) for a,b in zip(A,B)]
def ceilDiv(A,B): return (A+B-1)//B
def floorDiv(A,B): return A//B
def modAdd(A,B,N): return (A+B)%N
def myBin(N): return "{:b}".format(N)
def zeroPad(N,digit=10,pattern='0'): return str(N).rjust(digit,pattern)
def sortWithOrder(A):
    import numpy as np; N = len(A) # (Input) A: (N)
    B = np.array([(A[n],(n)) for n in range(N)],dtype=[('value',int),('ind',int)]) # (N x 2)
    B.sort(axis=0,order='value'); return B # (Output) B: (N x 2)
def encode(List,P): return sum([l*((P+1)**i) for i,l in enumerate(List)])
def swap(A,B): return B,A
def binaryBrute(N):
    from itertools import product
    for bit in product((0,1),repeat=N):
        for n in range(N):
            if bit[n] == 1:
                pass # Do something
        if False:
            print('Yes')

if __name__ == '__main__':
    main()