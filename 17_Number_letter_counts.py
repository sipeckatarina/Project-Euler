
stevila = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
crke_enice = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
crke_desetice = [0, 4, 6, 6, 5, 5, 5, 7, 6, 6]
#ce je na mestu desetic 1
crke_enice_1 = [0, 2, 2, 4, 4, 3, 3, 5, 4, 4]


def num_of_letters(x):
    if x == 1000:
        return 8 + 3
    else:
        dolzina = 0
        enice = x % 10
        desetice = (x // 10) % 10
        stotice = x // 100
        if x % 100 == 10:
            dolzina = dolzina - 1
        for i in range (1, 10):
            if stotice == int(stevila[i]):
                dolzina += int(crke_enice[i]) + 7 + 3 # pristej se "hundred" in "and"
                #print(stotice, dolzina)
            if desetice == int(stevila[i]):
                dolzina += int(crke_desetice[i])
                #print(desetice, dolzina)
            if enice == int(stevila[i]) and desetice != 1: # brez "-najst"
                dolzina += int(crke_enice[i])
                #print(enice, dolzina)
            if enice == int(stevila[i]) and desetice == 1: # "-najst"
                if enice == int(stevila[i]):
                    dolzina += int(crke_enice_1[i])
        if desetice == 0 and enice == 0: # ce je deljiva s 100 odstej 3 za "and"
            dolzina = dolzina - 3
    return dolzina


def sum_letters_from_to(y, x):
    l = []
    for i in range (y, x + 1):
        n = num_of_letters(i)
        l.append(n)
    print(l)
    s = sum(l)
    return s


print (sum_letters_from_to(1, 1000))

'''
print (sum_letters_from_to(1, 10))
print (sum_letters_from_to(11, 20))
print (sum_letters_from_to(21, 30))
print (sum_letters_from_to(31, 40))
print (sum_letters_from_to(41, 50))
print (sum_letters_from_to(51, 60))
print (sum_letters_from_to(61, 70))
print (sum_letters_from_to(71, 80))
print (sum_letters_from_to(81, 90))
print (sum_letters_from_to(91, 100))
'''







