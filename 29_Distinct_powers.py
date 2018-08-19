def num_of_distinct_terms(beginning, end):
    l = []
    for a in range (beginning, end + 1):
        for b in range (beginning, end + 1):
            l.append(a ** b)
    s = set(l)
    return len(s)
