v1 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
v2 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
v3 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
v4 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
v5 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
v6 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
v7 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
v8 = [99, 65, 4, 28, 6, 16, 70, 92]
v9 = [88, 2, 77, 73, 7, 63, 67]
v10 = [19, 1, 23, 75, 3, 34]
v11 = [20, 4, 82, 47, 65]
v12 = [18, 35, 87, 10]
v13 = [17, 47, 82]
v14 = [95, 64]
v15 = [75]

vrstice_piramide = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15]

for n in range(14):
    vn = vrstice_piramide[n]
    vp = vrstice_piramide[n + 1]
    for x in range(len(vn) - 1):
        m = max(vn[x], vn[x + 1])
        vp[x] = vp[x] + m

print(int(v15[0]))
