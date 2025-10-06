n, q = map(int, input().split())
a = list(map(int, input().split()))
count_ones = a.count(1)

for _ in range(q):
    t, x = map(int, input().split())

    if t == 1:
        a[x - 1] = 1 - a[x - 1]
        if a[x - 1] == 0:
            count_ones -= 1
        else:
            count_ones += 1
    else:
        if x <= count_ones:
            print(1)
        else:
            print(0)
