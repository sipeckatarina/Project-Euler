def is_palindrome(x):
    forward = x
    back = forward[::-1]
    return forward == back

def from_10_to_2(x):
    l = str(x)
    current = []
    while x // 2 > 0:
        if x % 2 == 1:
            current.append(1)
            x = x // 2
        else:
            current.append(0)
            x = x // 2
    current.append(1)
    current = current[::-1]
    return current

def find_all_double_palindromes_to(x):
    l = []
    for i in range(x):
        desetiski = str(i)
        dvojiski = from_10_to_2(i)
        if is_palindrome(desetiski) and is_palindrome(dvojiski):
            l.append(i)
    return l

s = sum(find_all_double_palindromes_to(1000000))
print(s)
