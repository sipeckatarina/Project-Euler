i = 1
while True:
    if len(str(2 * i)) == len(str(3 * i)) and len(str(3 * i)) == len(str(4 * i)) and len(str(4 * i))== len(str(5 * i)) and len(str(5 * i)) == len(str(6 * i)):
        if set(str(2 * i)) == set(str(3 * i)) and set(str(3 * i)) == set(str(4 * i)) and set(str(4 * i))== set(str(5 * i)) and set(str(5 * i)) == set(str(6 * i)):
            print(i)
            break
    i += 1
