import math


a = int(math.sqrt(1020304050607080900))
b = int(math.sqrt(2000000000000000000))
print (a, b)
for i in range(a, b, 10):
    n = str(i ** 2)
    #print(n) 
    if int(n[0]) == 1 and int(n[2]) == 2 and int(n[4]) == 3 and int(n[6]) == 4 and int(n[8]) == 5 and int(n[10]) == 6 and int(n[12]) == 7 and int(n[14]) == 8 and int(n[16]) == 9 and int(n[18]) == 0:
        print(i)
        break
