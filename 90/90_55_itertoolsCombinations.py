import itertools
N,P,Q = map(int,input().split())
A = list(map(int,input().split()))
# print(A)
count = 0
for C in itertools.combinations(A,5):
    X = 1
    for c in C:
        X = (X*c)%P
    count += 1 if X == Q else 0
print(count)