'''Number spiral diagonals
2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8,
'''


def diagonala_do(x):
    diagonala = []
    nova = 1
    i = 0
    while True:
        i += 2
        for j in range(4):
            diagonala.append(nova)
            nova += i
            if nova > x ** 2:
                return(diagonala)
    return(diagonala)

s = sum(diagonala_do(1001))
print(s)
