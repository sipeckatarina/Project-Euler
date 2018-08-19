a, b = 1, 1
c = 1

vsota = 0

while c < 4000000:
    # print (c)
    c = a + b
    a = b
    b = c
    if c % 2 == 0:
        vsota += c

print (vsota)
