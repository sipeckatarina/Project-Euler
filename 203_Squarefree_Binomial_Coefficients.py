import math

def next_row(row):
    next_r = [1]
    for i in range(1, len(row)):
        next_r.append(row[i-1] + row[i])
    next_r.append(1)
    return next_r


def pascal_triangle_rows_to(n):
    pascal_triangle = []
    pascal_row = [1]
    for i in range(1, n):
        pascal_triangle.append(pascal_row)
        pascal_row = next_row(pascal_row)
    return pascal_triangle


def is_squerefree(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % (i ** 2) == 0:
            return False
    return True


def find_squerefree_numbers(triangle):
    squerefree = set()
    for row in triangle:
        for num in row:
            if num not in squerefree:
                if is_squerefree(num):
                    squerefree.add(num)
    return(squerefree)


s = find_squerefree_numbers(pascal_triangle_rows_to(52))
print(sum(s))
