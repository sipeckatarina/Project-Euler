def power_digit_sum(osnova, argument):
    x = osnova ** argument
    stevke = str(x)
    print(stevke)
    vsota = 0
    for i in range(len(stevke)):
        vsota += int(stevke[i])
    return vsota
