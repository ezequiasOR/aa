n, k = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

m = 999999999999999
for i in range(k+1):
    diff = a[n - k - 1 + i] - a[i]
    m = min(m, diff)

print(m)
