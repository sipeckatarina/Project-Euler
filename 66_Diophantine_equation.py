import math

r = [x for x in range(1001)]
for i in range(1001):
    if i ** 2 > 1000:
        break
    r.remove(i ** 2)


def minimal_x(D):
    x = 2
    while True:
        y = math.sqrt(((x ** 2) - 1) / D)
        if y % 1 == 0:
            return x
        x += 1

maksi_x = 0
maksi_D = 0
for D in r:
    if minimal_x(D) > maksi_x:
        print(maksi_D, maksi_x)
        maksi_D = D
        maksi_x = minimal_x(D)

print(maksi_D, maksi_x)
    
