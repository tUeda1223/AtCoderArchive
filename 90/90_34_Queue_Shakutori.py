from collections import deque
N,K = map(int,input().split())
A = list(input().split())
returnLength = 0
myDict = dict()
myDictLength = 0
myQueue = deque()
myQueueLength = 0
for n in range(N):
    a = A[n]
    ## Let right move
    myQueue.append(a)
    myQueueLength += 1
    if not a in myDict:
        myDict[a] = 1
        myDictLength += 1
    elif a in myDict:
        myDict[a] += 1
    ## Let left move
    while myDictLength > K:
        pop = myQueue.popleft()
        myQueueLength -= 1
        if myDict[pop] == 1:
            del myDict[pop]
            myDictLength -= 1
        else:
            myDict[pop] -= 1
    returnLength = max(returnLength,myQueueLength)
    # print(myDict)
    # print(myQueue)
    # print('----')
print(returnLength)