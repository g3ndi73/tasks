
f = open('17.txt')
a = [int(x) for x in f]
k = a[0]
ans = 0
for i in range(1, len(a)):
    if a[i] * k > k**2:
        ans += a[i]
print(ans)
