def primes_to(n):
    primes = [i for i in range (n)]
    primes[1] = 0
    for j in range (2, n):
        if int(primes[j]) != 0:
            for k in range (j ** 2, len(primes), j):
                primes[k] = 0
                #  print(primes)
    while 0 in primes:
        primes.remove(0)
    return primes

primes = primes_to(10000)
while primes[0] < 1000:
    for i in primes:
        if i < 1000:
            primes.remove(i)

trojcki = []


for x in primes:
    if len(trojcki) < 2:
        for razlika in range(1, 5001):
            a = x
            b = x + razlika
            c = x + 2 * razlika
            if (b in primes) and (c in primes):
                if (set(str(a)) == set(str(b))) and (set(str(c)) == set(str(b))):
                    #print(a, b, c)
                    trojcki.append([a, b, c])
                    if len(trojcki) == 2:
                        break 

num = trojcki[1]
print(int(str(num[0]) + str(num[1]) + str(num[2])))
