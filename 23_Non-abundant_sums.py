import math


def is_abundant(x):  #divisors
    s = 1
    koren = math.sqrt(x)
    for i in range (2, int(koren) + 1):
        if x % i == 0:
            s += i + x // i
    if int(koren) == koren:
        s -= koren
    if s > x:
        return True
    return False

abundant = {a for a in range(12, 28123) if is_abundant(a)}


def can_it_be_written(x):
    for i in abundant:
        if i > x:
            return False
        if x - i in abundant:
            return True
    return False

not_sum = {x for x in range(1, 28123) if not can_it_be_written(x)}


'''
def sum_of_to(x):
    l = []
    for i in range(24, x):
        if can_it_be_written(i):
            l.append(i)
        print(l)
    s = sum(l)
    return s



ab = abundant_to(28124)
can = []
lenght = len(ab)
for i in range(1, lenght):
    for j in range(1, lenght):
        a = ab[i]
        b = ab[j]
        can.append(a + b)
print (can)
'''
