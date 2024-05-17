import numpy as np
N8,K = map(int,input().split())
for k in range(K):
    N10 = int(str(N8), 8)
    N9  = np.base_repr(N10,9)
    N8 = str(N9).replace('8','5')
    # print(N10)
    # print(N9)
    # print(N8)
print(N8)