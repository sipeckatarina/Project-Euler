def fakulteta(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
    return a

def po_vrsti(n, x):
    zaloga = [a for a in range(n + 1)]
    #print(zaloga)
    stevilo = []
    vrsti = 0
    while len(zaloga) > 0:
        for i in range(len(zaloga)):
            if vrsti + (i + 1) * fakulteta(len(zaloga) - 1) >= x :
                vrsti += i * fakulteta(len(zaloga) - 1)
                stevilo.append(zaloga[i])
                zaloga.remove(zaloga[i])
                break
    return stevilo

def list_to_int(l):
    num = 0
    l = l[::-1]
    for x in range(len(l)):
        num += l[x] * (10 ** x)
    return num
        
print(list_to_int(po_vrsti(9, 1000000)))  










