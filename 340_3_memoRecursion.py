# https://atcoder.jp/contests/abc340/tasks/abc340_c
## (input)
# N = input()
# S = int(input())
# A, B = map(int,input().split())
## (Reference)
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14
# https://harinez2.hateblo.jp/entry/atcoder-template-python
## input() for debug mode
import sys,os
if os.path.exists('input.txt'):
    r = open('input.txt','r')
    def input():
        return r.readline()
    from pdb import set_trace as test
def IIn(): return int(input().rstrip())
def SIn(): return input().rstrip()
def LIIn(): return list(map(int,input().rstrip().split()))
def LSIn(): return list(input().rstrip().split())
def main():
    # S = SIn()
    # A = LIIn()
    N = IIn()
    print(myFunc(N))

dic = dict()
def myFunc(N):
    if N == 1:
        return 0
    if N in dic:
        return dic[N]
    X = 0
    X += N
    if N%2 == 0:
        X += 2*myFunc(N//2)
    else:
        X += myFunc(N//2) + myFunc((N+2-1)//2)
    dic[N] = X
    return X

if __name__ == '__main__':
    main()