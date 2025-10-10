a, b = map(int, input().split())
count = 0

for i in range(a, b + 1):
    num = str(i)
    if num[0] == num[4] and num[1] == num[3]:
        count += 1

print(count)
