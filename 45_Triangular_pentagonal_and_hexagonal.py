
triangulars = {(n * (n + 1) // 2) for n in range(1000000)}
pentagonals = {(n * (3 * n - 1) // 2) for n in range(800000)}
hexagonals = {(n * (2 * n - 1)) for n in range(600000)}

everything = []
for i in triangulars:
    if i in pentagonals:
        if i in hexagonals:
            everything.append(i)

print(everything[3])
