
def fakulteta(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
    return a

def nad(n, r):
    C = (fakulteta(n)) // (fakulteta(n - r) * fakulteta(r))
    return C

s = 0
for n in range(1, 101):
    for r in range(1, n): #zgleda lepse, ce gre le do n, itak pa ni razlike v resitvi
        if len(str(nad(n, r))) >= 7:
            s += 1

print(s)
