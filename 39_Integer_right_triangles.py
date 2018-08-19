import math

def num_of_triangled(x):
    num_of = 0
    # x = dolzina zice
    for c in range (x // int(2 + math.sqrt(2)), x // 2):
        for a in range (1, ((x - c) // 2) + 1):
            b = x - c - a
            #print (a, b, c)
            if c ** 2 == a ** 2 + b ** 2:
                num_of += 1
    return num_of
        
def maximum_triangles_to(x):
    current = 0
    M = 0
    for i in range (x + 1):
        if num_of_triangled(i) > current:
            current = num_of_triangled(i)
            M = i
            print(M, current)
    return M
