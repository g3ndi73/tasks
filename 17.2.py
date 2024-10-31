f = open('task.txt')

a = [int(x) for x in f]
k1, k2 = a[0], a[1]
ans = 0
for i in range(2, len(a)):
    if ((a[i]**2 - k1**2) > k1 and (a[i]**2 - k1**2) < k2)
        or ((a[i]**2 - k1**2) > k1 and (a[i]**2 - k1**2) < k2):
    
        ans += a[i]
print(ans)

