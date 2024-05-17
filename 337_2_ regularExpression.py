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
    from re import fullmatch
    if fullmatch('A*B*C*', SIn()):
        print('Yes')
    else:
        print('No')


def myFunc():
    return 0

if __name__ == '__main__':
    main()