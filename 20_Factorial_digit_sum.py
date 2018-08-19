
def fakulteta(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
    return a

def vsota_stevk(a):
    x = fakulteta(a)
    stevke = str(x)
    print(stevke)
    vsota = 0
    for i in range(len(stevke)):
        vsota += int(stevke[i])
    return vsota
