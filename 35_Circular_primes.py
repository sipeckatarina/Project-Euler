def primes_to(n):
    primes = [i for i in range (n)]
    primes[1] = 0
    for j in range (2, n):
        if int(primes[j]) != 0:
            for k in range (j ** 2, len(primes), j):
                primes[k] = 0
                #print(primes)
    return primes

primes = list(set(primes_to(1000000)))


def is_fensi(x):
    x_str = str(x)
    for i in range(len(x_str)):
        x_str = str(x)
        x = int(x_str[-1] + x_str[:-1])
        #print (x_str)
        if not(x in primes):
            return False
    return True


def  find_all_to(funkcija, maks):
    tabela = [2, 5]
    for i in range(1, maks, 2):
        if set(str(i * 10000 + 1397)) == set(str(1973)):
            if funkcija(i):
                tabela.append(i)
                #print(tabela)
    return(tabela)

print(len(find_all_to(is_fensi, 1000000)))

'''
[0, 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79,
 97, 193, 197, 337, 397, 733, 937, 991]
'''
