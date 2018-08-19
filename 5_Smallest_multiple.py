def is_prime(x):
    a = True
    for y in range (2, x // 2 + 1):
        if x % y == 0:
            a = False
    return a

def najmanjsi_veckratnik_manjsih(x):
    veckratnik = 1
    for deljitelj in range (2, x):
        if is_prime(deljitelj):
            najvisja_potenca = 1
            while najvisja_potenca < x / deljitelj:
                najvisja_potenca = najvisja_potenca * deljitelj
        else:
            najvisja_potenca = 1
        veckratnik = veckratnik * najvisja_potenca
#        print(najvisja_potenca)
#        print(veckratnik)
    return(veckratnik)

print(najmanjsi_veckratnik_manjsih(20))
