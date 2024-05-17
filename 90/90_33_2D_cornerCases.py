H,W = map(int,input().split())
if H == 1 or W == 1:
    print(H*W)
else:
    H2 = (H+2-1)//2
    W2 = (W+2-1)//2
    print(H2*W2)