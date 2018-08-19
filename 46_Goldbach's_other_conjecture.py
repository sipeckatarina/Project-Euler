

def primes_to(n):
    primes = [i for i in range (n)]
    primes[1] = 0
    for j in range (2, n):
        if int(primes[j]) != 0:
            for k in range (j ** 2, len(primes), j):
                primes[k] = 0
    while 0 in primes:
        primes.remove(0)
    return primes

primes = primes_to(10000)


def is_weird(x):
    for p in primes[:x]:
        for i in range(x // 2): # se še da optimizirati
            if x == p + (2 * (i ** 2)):
                #print(x, p, i)
                return True
    return False


a = 1
i = 3
while a == 1:
    if not(is_weird(i)):
        print(i)
        a = 0
    i += 2
