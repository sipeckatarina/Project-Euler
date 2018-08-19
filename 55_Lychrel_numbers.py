import uporabne_funkcije as f


def obrnjen(n):
    return int(str(n)[::-1])


def rata_palindrom(n):
    ponovitve = 0
    while ponovitve <= 51:
        n = n + obrnjen(n)
        if n == obrnjen(n):
            return True
        ponovitve += 1
    return False


s = 0
sez = []
for num in range(1, 10000 + 1):
    if not(rata_palindrom(num)):
        s += 1
        sez.append((s, num))

for i in sez:
    print(i)
print(s)
