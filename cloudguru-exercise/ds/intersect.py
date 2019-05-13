def intersect(a, b):
    c = [i for i in a if i in b]
    # for i in a:
    #     if i in b:
    #         c.append(i)
    print c
    print list(set(a).intersection(b))


list_a = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9]
list_b = [1, 2, 2, 3, 8, 8]
intersect(list_a, list_b)
