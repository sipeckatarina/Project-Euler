def is_1_or_89(x):
    a = 0
    n = x
    while n != 89 and n != 1:
        a = str(n)
        l = len(a)
        n = 0
        for i in range(l):
            n += int(a[i]) ** 2
        #print(n)
    return n

s = 0
for i in range(2, 10000000):
    if is_1_or_89(i) == 89:
        s += 1
print(s)
