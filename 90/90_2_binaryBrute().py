# https://atcoder.jp/contests/typical90/tasks/typical90_b
def makeStr(n,N):
    arr = str(format(n, '0%db'%N))
    arr = arr.replace('1',')').replace('0','(')
    return arr

def evalStr(S):
    score = 0
    for s in S:
        score += 1 if s == '(' else -1
        if score < 0:
            return False
    if score == 0:
        return True
    else:
        return False

N = input()
if N%2 == 0:
    for n in range(2**N):
        s = makeStr(n,N)
        if evalStr(s):
            print(s)