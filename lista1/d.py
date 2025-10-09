import math

n = int(input())

primes = [True] * (n)
primes[0] = primes[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if primes[i]:
        for j in range(i * i, n + 1, i):
             primes[j] = False

last_prime = 0

for i in range(len(primes)-1, 2, -1):
    if primes[i]:
        last_prime = i
        break

if (last_prime == 0) or (2 + last_prime != n):
    print(-1)
else:
    print(2, last_prime)
