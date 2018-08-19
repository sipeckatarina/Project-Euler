import math

def is_one_triangle(x):
    num_of = 0
    # x = dolzina zice
    for c in range (x // int(2 + math.sqrt(2)), x // 2):
        for a in range (1, ((x - c) // 2) + 1):
            b = x - c - a
            #print (a, b, c)
            if c ** 2 == a ** 2 + b ** 2:
                num_of += 1
                if num_of > 1:
                    return False
##    print(num_of)
    if num_of == 1:
        return True
    else:
        return False
        
def count_to(x):
    num = 0
    for i in range (2, x + 1, 2):
        if is_one_triangle(i):
            print (i)
            num += 1
    return num
