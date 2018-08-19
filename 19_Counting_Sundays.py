# 1.1.1900 ponedeljek
# koliko sobot je na prvi dan v mesecu v letih [1901, 2000]

stevilo_dni_v_mesecu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# za februar v prestopnem pristej 1

def je_prestopno_leto(leto):
    if leto % 400 == 0:
        return True
    if leto % 100 == 0:
        return False
    if leto % 4 == 0:
        return True
    else:
        return False

def main():
    dan_po_vrsti = sum(stevilo_dni_v_mesecu)
    stevilo_sobot = 0

    #preverimo ce je 1900 prestopno
    if je_prestopno_leto(1900):
        dan_po_vrsti += 1

    for leto in range(1901, 2001):
        if je_prestopno_leto(leto):
            stevilo_dni_v_mesecu[1] = 29
        else:
            stevilo_dni_v_mesecu[1] = 28

        for mesec in stevilo_dni_v_mesecu:
            if dan_po_vrsti % 7 == 5:
                stevilo_sobot += 1
            dan_po_vrsti += mesec

    return stevilo_sobot

print(main())
