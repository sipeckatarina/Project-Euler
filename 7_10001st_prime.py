'''
def is_prime(x):
    a = True
    for y in range (2, x // 2 + 1):
        if x % y == 0:
            a = False
    return a
tabela = []
for x in range (0, 100000):
    if is_prime(x):
        tabela.append(x)

print(tabela[10000])


def prastevila_do(stev):
    tabela = [2]
    for x in range (2, stev):
        a = True
        for y in tabela:
            if x % y == 0:
                a = False
        if a == True:
            tabela.append(x)
#    print(tabela)
    return(tabela)
'''

def prvih_x_prastevil(stev):
    tabela = [2]
    x = 2
    while len(tabela) < stev:
        a = True
        for y in tabela:
            if x % y == 0:
                a = False
                break
        if a:
            tabela.append(x)
        x = x + 1
    #print(tabela)
    return(tabela)


def ito_prastevilo(i):
    seznam = prvih_x_prastevil(i)
    return seznam[i - 1]


print(ito_prastevilo(10001))



