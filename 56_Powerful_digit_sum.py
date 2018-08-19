
def vsota_stevk(a):
    stevke = str(a)
    #print(stevke)
    vsota = 0
    for i in range(len(stevke)):
        vsota += int(stevke[i])
    return vsota

s = 0
for a in range(101):
    for b in range(101):
        if vsota_stevk(a ** b) > s:
            s = vsota_stevk(a ** b)

print (s)
