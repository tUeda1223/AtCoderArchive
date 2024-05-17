N,Q = map(int,input().split())
A = list(map(int,input().split()))
score = sum(A)
diff = [0]+[A[n+1]-A[n] for n in range(N-1)]
diffAbsSum = sum([abs(d) for d in diff])
##
# print(diffAbsSum)
# print(A)
# print(diff)
# print('----')
# debug = True
##
for q in range(Q):
    LTmp,RTmp,V = map(int,input().split())
    L = LTmp -1
    R = RTmp -1
    if L > 0:
        tmpLeft = abs(diff[L])
        diff[L]+=V
        diffAbsSum -= tmpLeft
        diffAbsSum += abs(diff[L])
    if R < N-1:
        tmpRight = abs(diff[R+1])
        diff[R+1]-=V
        diffAbsSum -= tmpRight
        diffAbsSum += abs(diff[R+1])
    print(diffAbsSum)
    ## 
    # listTmp = list(range(L,R+1))
    # # print(listTmp)
    # for l in listTmp:
    #     A[l]+=V
    # print(A)
    # print(diff)
    # print('----')
    ##