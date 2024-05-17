import os
if os.path.exists('input.txt'):
    r = open('input.txt','r')
    def input():
        return r.readline()
    from pdb import set_trace as test
def IIn(): return int(input().rstrip())
def LIIn(): return list(map(int,input().rstrip().split()))
from itertools import product
def calcV3(pos1,pos2,pos3):
    x = max(min(pos1[0],pos2[0],pos3[0])+7-max(pos1[0],pos2[0],pos3[0]),0)
    y = max(min(pos1[1],pos2[1],pos3[1])+7-max(pos1[1],pos2[1],pos3[1]),0)
    z = max(min(pos1[2],pos2[2],pos3[2])+7-max(pos1[2],pos2[2],pos3[2]),0)
    return x*y*z
def calcV2(pos1,pos2):
    x = max(min(pos1[0],pos2[0])+7-max(pos1[0],pos2[0]),0)
    y = max(min(pos1[1],pos2[1])+7-max(pos1[1],pos2[1]),0)
    z = max(min(pos1[2],pos2[2])+7-max(pos1[2],pos2[2]),0)
    return x*y*z
def main():
    # S = SIn()
    # A = LIIn()
    # V1: volume of only one
    # V2: volume of only two
    # V3: Volume of all
    V1,V2,V3 = LIIn()
    ALL = 3*(7**3)
    pos1 = [0,0,0]
    for pos2 in product(range(-1,8),repeat=3):
        for pos3 in product(range(-1,8),repeat=3):
            V3Tmp = calcV3(pos1,pos2,pos3)
            if V3 == V3Tmp:
                V1V2 = calcV2(pos1,pos2)
                V1V3 = calcV2(pos1,pos3)
                V2V3 = calcV2(pos2,pos3)
                V2Tmp = V1V2+V2V3+V1V3-3*V3Tmp
                if V2Tmp == V2:
                    V1Tmp = ALL - 3*V3Tmp - 2*V2Tmp
                    if V1 == V1Tmp:
                        print('Yes')
                        print(' '.join([str(s) for s in pos1])+' '+' '.join([str(s) for s in pos2])+' '+' '.join([str(s) for s in pos3]))
                        import sys; sys.exit()
    print('No')

if __name__ == '__main__':
    main()