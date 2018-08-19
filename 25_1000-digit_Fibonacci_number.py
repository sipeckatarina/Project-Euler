def first_fobonaffi_with(x):
    a, b = 0, 1
    c = 1
    i = 1
    while len(str(c)) < x:
        #print (c)
        c = a + b
        a = b
        b = c
        i += 1
    return i

print (first_fobonaffi_with(1000))
