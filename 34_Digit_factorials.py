
def fakulteta(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
    return a

def is_sum_fifth_power_digits(x):
    num_str = str(x)
    s = 0
    for i in range(len(num_str)):
        s += fakulteta(int(num_str[i]))
    if s == x:
        return True
    return False
    
l = [a for a in range(3, 1000000) if is_sum_fifth_power_digits(a)]
s = sum(l)

print(s)
