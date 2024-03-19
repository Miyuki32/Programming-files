tuplex = (4, 6, 2, 8, 3, 1)

print(tuplex)

tuplex = tuplex + (9,)

print(tuplex)

tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]

print(tuplex)

list_tup = list(tuplex)
list_tup.append(30)
tuplex = tuple(list_tup)

print(tuplex)