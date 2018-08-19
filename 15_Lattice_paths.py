# permutacije x-tih desno (1) in x-tih dol (0)


def fakulteta(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
    return a


def stevilo_poti(x):
    desno = x
    dol = x
    #pot je sestavljena iz desno in dol
    stevilo_poti = (fakulteta(desno + dol)) // (fakulteta(desno) ** 2)
    return stevilo_poti

