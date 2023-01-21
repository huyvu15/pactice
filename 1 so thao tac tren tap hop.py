a = {120, 230, 325, 400}
b = {120, 410, 325, 600}


# hop cua 2 tap hop
print("Hợp cua 2 tap hop")
print(a | b )
print(a.union(b))

# giao cua 2 tap hop
print("Giao của 2 tập")
print(a & b)
print(a.intersection(b))

# Hiệu của 2 tập
print("Đây là hiệu của 2 tập")
print(a-b)
print(a.difference(b))

# Hiệu đối xứng của 2 tập
print("Đây là hiệu đối xứng của 2 tập")
print(a^b)
print(a.symmetric_difference(b))
# set lồng nhau
print("set lồng nhau")
rainbow = ('violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red')
other_colors = ('white', 'black', 'pink')

nested_set = set((frozenset(rainbow), frozenset(other_colors)))

for sample_set in nested_set:
    print(sample_set)
    