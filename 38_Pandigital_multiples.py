def is_pandigital(n):
    list_n = list(str(n))
    if not('0' in list_n):
        len_n = len(str(n))
        max_n = int(max(list_n))
        return len_n == len(set(str(n))) and len_n == max_n
    return False


m = 0
for i in range(1, 100000):
    s = ''
    j = 1
    while len(s) < 9:
        s += str(i * j)
        j += 1
    s = int(s)
    if is_pandigital(s) and s > m:
        m = s

print(m)