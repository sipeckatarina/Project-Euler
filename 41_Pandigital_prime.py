def primes_to(n):
    primes = [i for i in range(n + 1)]
    primes[1] = 0
    for j in range (2, n):
        if int(primes[j]) != 0:
            for k in range (j ** 2, len(primes), j):
                primes[k] = 0
    primes = list(set(primes))
    return primes


primes = primes_to(10000000)

pandigitals = []

for i in primes:
    s = str(i)
    l = str(set(s))
    print(l)
    if len(s) == len(str(123456789)):
        pandigitals.append(i * j)
        j += 1

print(l, pandigitals)


