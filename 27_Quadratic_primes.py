def primes_to(n):
    primes = [i for i in range (n)]
    primes[1] = 0
    for j in range (2, n):
        if int(primes[j]) != 0:
            for k in range (j ** 2, len(primes), j):
                primes[k] = 0
                #print(primes)
    return sorted(list(set(primes)))

prastevila = primes_to(100000)
baza_n = primes_to(1000)
baza_n.append(1)
baza_n.sort()

par = [0, 0]
maksi_prastevil = 0
for n in baza_n:
    for m in primes_to(1000):
        for x in range(200):
            trenuten = x
            if x ** 2 + n * x + m not in prastevila:
                break
        if trenuten > maksi_prastevil:
            maksi_prastevil = trenuten
            par = [n, m]
            print(n, m, trenuten, par)
        for x in range(200):
            trenuten = x
            if x ** 2 - n * x + m not in prastevila:
                break
        if trenuten > maksi_prastevil:
            maksi_prastevil = trenuten
            par = [-n, m]
            print(n, m, trenuten, par)
        for x in range(200):
            trenuten = x
            if x ** 2 + n * x - m not in prastevila:
                break
        if trenuten > maksi_prastevil:
            maksi_prastevil = trenuten
            par = [n, -m]
            print(n, m, trenuten, par)
        for x in range(200):
            trenuten = x
            if x ** 2 - n * x - m not in prastevila:
                break
        if trenuten > maksi_prastevil:
            maksi_prastevil = trenuten
            par = [-n, -m]
            print(n, m, trenuten, par)

print(par)
print(par[0] * par[1])
