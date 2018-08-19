# najvecje stevilo, ki se bere z ene strani isto k iz druge pa
#produkt dveh tromestnih ... kaj?


def stevilo_stevk(x):
    stevke = 1
    while x / 10 > 1:
        stevke = stevke + 1
        x = x // 10
    return stevke


def is_palindrome(x):
    string = str(x)
    rev = string[::-1]
    if string == rev:
        return True
    else:
        return False


def the_palindrome (stevilo_stevk):
    naj = 1
    for x in range (10 ** (stevilo_stevk - 1), 10 ** stevilo_stevk):
        for y in range (10 ** (stevilo_stevk - 1), 10 ** stevilo_stevk):
            zmnozek = x * y
            if zmnozek > naj:
                if is_palindrome(zmnozek):
                    naj = zmnozek
    return (naj)

print(the_palindrome(3))






















    
    
