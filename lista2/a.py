n, q = map(int, input().split())
x = list(map(int, input().split()))

somas = [0] * (n + 1)

for i in range (1, n+1):
    somas[i] = somas[i-1] + x[i-1]

for _ in range(q):
    a, b = map(int, input().split())
    print(somas[b] - somas[a-1])
