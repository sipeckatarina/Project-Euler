def table_ij(file, split_with = ' '):
    table = []
    with open(file) as input:
        for line in input:
            l = line.split(split_with)
            column = []
            for x in l:
                column.append(int(x))
            table.append(column)
    return table

l = table_ij('PE59cipher.txt', ',')
l = l[0]
