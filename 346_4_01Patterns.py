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
    N = IIn()
    S = list(map(bool,[int(s) for s in LSIn2()]))
    C = LIIn()
    S01 = [False,True]*(N//2)+[False]*(N%2)
    S10 = [True,False]*(N//2)+[True]*(N%2)
    SxS01 = listXOR(S,S01)
    SxS10 = listXOR(S,S10)
    C01Left = [None]*N
    C10Left = [None]*N
    C01Right = [None]*N
    C10Right = [None]*N
    C01Left[0] = C[0] if SxS01[0] else 0
    C10Left[0] = C[0] if SxS10[0] else 0
    C01Right[-1] = C[-1] if SxS01[-1] else 0
    C10Right[-1] = C[-1] if SxS10[-1] else 0
    for n in range(1,N):
        C01Left[n] = C01Left[n-1] + (C[n] if SxS01[n] else 0)
        C10Left[n] = C10Left[n-1] + (C[n] if SxS10[n] else 0)
        C01Right[-(1+n)] = C01Right[-n] + (C[-(1+n)] if SxS01[-(1+n)] else 0)
        C10Right[-(1+n)] = C10Right[-n] + (C[-(1+n)] if SxS10[-(1+n)] else 0)
    minCost = 10**18
    for n in range(N-1):
        costTmp = C01Left[n]+C10Right[n+1]
        # print(costTmp)
        minCost = min(minCost,costTmp)
        costTmp = C10Left[n]+C01Right[n+1]
        # print(costTmp)
        minCost = min(minCost,costTmp)
    print(minCost)
    # printTF201(S)
    # printTF201(S01)
    # printTF201(S10)
    # printTF201(SxS01)
    # printTF201(SxS10)
    # print(C01Left)
    # print(C10Left)
    # print(C01Right)
    # print(C10Right)

def myFunc():
    return 0

################ Local functions ################
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def printTF201(S): STmp = [1 if s else 0 for s in S]; print(STmp)
def yesno(c): print('Yes' if c else 'No')
def gcd(a,b):
    while b: a, b = b, (a%b)
    return a
def lcm(a,b): return a * b // gcd(a, b)
def list2NP(matrix): import numpy as np; print(np.array(matrix))
def bisectLeft(List,value): return bisect.bisect_left(List,value)
def listXOR(A,B): return [a^b for a,b in zip(A,B)]
def listAdd(A,B): return [a+b for a,b in zip(A,B)]
def listSub(A,B): return [a-b for a,b in zip(A,B)]
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