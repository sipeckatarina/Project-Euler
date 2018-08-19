import math

def divisors(x):
    divisors = [1]
    for i in range (2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            if x // i not in divisors:
                divisors.append(x // i)
    return divisors


def d(x):
    divi = divisors(x)
    s = sum(divi)
    return s


def amicable_numbers_to(x):
    s = []
    for i in range(3, x):
        j = d(i)
        if j != i:
            if d(j) == i:
                if i not in s:
                    s.append(i)
                if j not in s:
                    s.append(j)
    return s

def sum_ami_to(x):
    s = sum(amicable_numbers_to(x))
    return s
