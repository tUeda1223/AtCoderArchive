from math import gcd
a,b = map(int,input().split())
ans = a*b//int(gcd(a,b))
ans = 'Large' if ans > 10**18 else ans
print(ans)