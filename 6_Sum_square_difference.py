def vsota_kvadratov(x):
    vsota = 0
    for a in range (1, x + 1):
        vsota = vsota + (a ** 2)
    return(vsota)


def kvadrat_vsote(x):
    vsota = 0
    for a in range (1, x + 1):
        vsota = vsota + a
    kvadrat = vsota ** 2
    return(kvadrat)


def razlika(x):
    a = kvadrat_vsote(x)
    b = vsota_kvadratov(x)
    razlika = a - b
    return (razlika)

#print(vsota_kvadratov(100))
#print(kvadrat_vsote(100))
print(razlika(100))
