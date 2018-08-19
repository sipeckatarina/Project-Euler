'Highly divisible triangular number'
import math

def prime_factors(x):
    koren = int (math.sqrt(x))
    deljitelj = 2
    stevilo = x
    naj = x
    prafaktorji = []
    potenca = 0
    while deljitelj <= int(koren) + 2:
        while stevilo % deljitelj == 0:
            stevilo = stevilo // deljitelj
            potenca += 1
        if potenca >=1:
            prafaktorji.append([deljitelj, potenca])
        potenca = 0
        deljitelj = deljitelj + 1
        if stevilo % deljitelj == 0:
            naj = deljitelj
    return (prafaktorji)


def num_of_divisors(x):
    l = prime_factors(x)
    num_of_divisors = 1
    for i in range(len(l)):
        num_of_divisors *= l[i][1] + 1
    return num_of_divisors


def main():
    num = 0
    trian = 1
    i = 2
    while num < 500:
        num = num_of_divisors(trian)
        trian += i
        i += 1
    #print(num, trian, i)
    naj = trian - i + 1
    return naj

        
