'Summation of primes'
'Find the sum of all the primes below two million.'


def primes_to(n):
    primes = [i for i in range (n)]
    primes[1] = 0
    for j in range (2, n):
        if int(primes[j]) != 0:
            for k in range (j ** 2, len(primes), j):
                primes[k] = 0
                #  print(primes)
    return primes


def izlocimo_nicle(sez):
    koncen = []
    for i in range (len(sez)):
        if sez[i] != 0:
            koncen.append(int(sez[i]))
    return koncen

# izlocimo_nicle(primes_to())


def vsota_prastevil_do(x):
    primes = izlocimo_nicle(primes_to(x))
    s = sum(primes)
    return s

print(vsota_prastevil_do(2000000))
