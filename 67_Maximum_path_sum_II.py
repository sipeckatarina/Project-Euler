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

table = table_ij('PE67triangle.txt')
table = table[::-1]

for line in range(len(table) - 1):
    vn = table[line]
    vp = table[line + 1]
    for x in range(len(vn) - 1):
        m = max(vn[x], vn[x + 1])
        vp[x] = vp[x] + m

print(int(table[-1][0]))
