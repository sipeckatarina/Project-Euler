'''Truncatable primes'''
import math

def primes_to(n):
    primes = [i for i in range (n)]
    primes[1] = 0
    for j in range (2, n):
        if int(primes[j]) != 0:
            for k in range (j ** 2, len(primes), j):
                primes[k] = 0
                #  print(primes)
    return primes

pra = list(set(primes_to(1000000)))

'''
def  is_prime(x):
    if x in pra:
        return True
    else:
        return False


def  is_right_primes(x):
    tabela = []
    stevilo_stevk = len(str(x))
    for i in range (stevilo_stevk + 1):
#        print (tabela)
        if is_prime(x):
            x = x % 10 ** (stevilo_stevk - i)
            tabela.append(x)
        else:
            return False
    return True


def  is_left_primes(x):
    tabela = []
    stevilo_stevk = len(str(x))
    for i in range (stevilo_stevk):
#        print (tabela)
        if is_prime(x):
            tabela.append(x)
            x = x // 10
        else:
            return False
    return True


def is_special(x):
    tabela = []
    if x < 10 or (x % 10 in [1, 2, 4, 6, 8, 9]) :
        return False
    if is_left_primes(x) and is_right_primes(x):
        return True
    else:
        return False
'''


def is_special(x):
    stevke = str(x)
    a = True
    if not(x in pra) or x < 10:
        return False
    for i in range(1, len(stevke)):
        leva = int(stevke[:i])
        desna = int(stevke[i:])
        print (leva, desna)
        if not ((leva in pra) and (desna in pra)):
            return False
    return True


def  find_all_to(funkcija, maks):
    tabela = []
    for i in range (maks):
        if funkcija(i):
            tabela.append(i)
    return(tabela)


def  find_all_while(funkcija, maks):
    tabela = []
    n = 10
    while len(tabela) < maks:
        if funkcija(n):
            tabela.append(n)
        n += 1
    return (tabela)

print (sum(find_all_while(is_special, 11)))
