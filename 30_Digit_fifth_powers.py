def is_sum_fifth_power_digits(x):
    num_str = str(x)
    s = 0
    for i in range(len(num_str)):
        s += int(num_str[i]) ** 5
    if s == x:
        return True
    return False
    
l = [a for a in range(2, 1000000) if is_sum_fifth_power_digits(a)]
s = sum(l)

print(s)
