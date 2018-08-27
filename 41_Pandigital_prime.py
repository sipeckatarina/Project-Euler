from primes_to import primes_to

#vsota stevk 987654321 (in permutacij) je deljiva z 9, torej ne more biti prastevilo
def is_pandigital(n):
    list_n = list(str(n))
    if not('0' in list_n):
        len_n = len(str(n))
        max_n = int(max(list_n))
        return len_n == len(set(str(n))) and len_n == max_n
    return False

primes = primes_to(87654321)
print('grem po cifrah')
primes = primes[::-1]

for p in primes:
    if is_pandigital(p):
        print(p)
        break