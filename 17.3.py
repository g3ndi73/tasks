def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


f = open('task.txt')

a = [int(x) for x in f]
k1, k2 = a[0], a[1]
ans = 0
for i in range(2, len(a)):
    if gcd(k1, a[i]) < k2:
        ans += a[i]
print(ans)
