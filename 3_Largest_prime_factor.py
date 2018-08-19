# Najveèji deljitelj 600851475143
import math

##def is_prime(x):
##    a = True
##    for y in range (2, x // 2 + 1):
##        if x % y == 0:
##            a = False
##    return a

def najvecji_prafaktor(x):
    koren = int (math.sqrt(x))
    deljitelj = 2
    stevilo = x
    naj = x 
    while deljitelj < koren:
        while stevilo % deljitelj == 0:
            stevilo = stevilo / deljitelj
        deljitelj = deljitelj + 1
        if stevilo % deljitelj == 0:
            naj = deljitelj
    return (naj)

print (najvecji_prafaktor(600851475143))
