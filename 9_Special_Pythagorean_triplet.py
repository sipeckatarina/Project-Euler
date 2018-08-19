

def triplet(vsota):
    for b in range (1, vsota // 2):
        for a in range (1, vsota):
            c = vsota - b - a
            if c ** 2 == (a ** 2) + (b ** 2):
                zmnozek = a * b * c
                return(zmnozek)
                break
    return False

print (triplet(1000))
