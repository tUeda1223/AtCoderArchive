M = int(input())
S1 = input()*3
S2 = input()*3
S3 = input()*3
C = 10**9+1
for i1,s1 in enumerate(S1):
    for i2,s2 in enumerate(S2):
        for i3,s3 in enumerate(S3):
            if (s1 == s2) and (s1 == s3):
                if len(set([i1,i2,i3])) == 3:
                    C = min(max(i1,i2,i3),C)
if C == 10**9+1:
    print('-1')
else:
    print(C)