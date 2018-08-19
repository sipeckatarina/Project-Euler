'''PE99base_exp.txt'''
import math


def table_ij(file, split_with = ' '):
    table = []
    with open(file) as input:
        for line in input:
            l = line.split(split_with)
            column = []
            for x in l:
                column.append(int(x))
            table.append(column)
    return table

table = table_ij('PE99base_exp.txt', ',')


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

def main():
    trenutna_osnova = table[0][0]
    trenutna_potenca = table[0][1]
    for i in table[1:3]:
        osnova = i[0]
        potenca = i[1]
        razcep_osnove = prime_factors(osnova)
        print (osnova, potenca, trenutna_osnova, trenutna_potenca)
        print (razcep_osnove)
        
