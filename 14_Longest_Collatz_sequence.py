def chain(x):
    string = []
    while not(1 in string):
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        string.append(x)
    return (string)

def max_chain_to(x):
    trenutna_dolzina = 0
    maksi = 0
    for i in range(1, x):
        if len(chain(i)) > trenutna_dolzina:
            trenutna_dolzina = len(chain(i))
            maksi = i
            #print(i, trenutna_dolzina)
    return maksi
            

print(max_chain_to(1000000))
