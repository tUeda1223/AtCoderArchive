# https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
K = int(input())
List = make_divisors(K)
count = 0
for c in List:
    for b in List:
        if b<= c:
            if K %(b*c) == 0:
                a = K//(b*c)
                if a <= b:
                    # print('%d, %d'%(b,c))
                    count += 1
print(count)

## Brute
# count = 0
# for c in range(1,10**4):
#     for b in range(1,c+1):
#         if K %(b*c) == 0:
#             a = K//(b*c)
#             if a <= b:
#                 print('%d, %d'%(b,c))
#                 count += 1
# print(count)
##