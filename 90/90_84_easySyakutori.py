N = int(input())
S = input()
S = '_'+S
count = 0
lastO = 0
lastX = 0
for n in range(1,N+1):
    s = S[n]
    lastO = n if s == 'o' else lastO
    lastX = n if s == 'x' else lastX
    count += lastX if s == 'o' else lastO
print(count)