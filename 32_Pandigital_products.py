pandigitals = []
for i in range(12, 10000):
    j = 2
    while i * j < 100000:
        s = str(i) + str(j) + str(i * j)
        if len(s) == 9 and set(s) == set(str(123456789)):
            pandigitals.append(i * j)
        j += 1

s_set = set(pandigitals)
s = sum(list(s_set))
print(s)
