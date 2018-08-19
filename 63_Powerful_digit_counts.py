import math

s = 0
for osnova in range(1, 10): # ce je osnova 10 ali vec, ima automatsko vec kot "potenca" stevk
    for potenca in range(1, 25): # stevilo stevk 9 ** 25 < 25, razlika pa se le se veca
        stevilo = osnova ** potenca
        l = len(str(stevilo))
        if l == potenca:
            #print(osnova, potenca, l)
            s += 1
print(s)
