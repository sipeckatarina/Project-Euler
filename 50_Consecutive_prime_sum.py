def primes_to(n):
    primes = [i for i in range (n)]
    primes[1] = 0
    for j in range (2, n):
        if int(primes[j]) != 0:
            for k in range (j ** 2, len(primes), j):
                primes[k] = 0
                #  print(primes)
    return primes

primes = primes_to(1000000)
i, j, a = 0, 0, 0

while j < 1000:
    j += int(primes[i])
    if j in primes:
        a = j
        #print(a)
    i += 1

print(a)
