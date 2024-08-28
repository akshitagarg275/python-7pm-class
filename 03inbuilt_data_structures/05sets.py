# sets, set()

'''
mutable, iterable
stores only unique values
collection of data
sets do not hold any unique position for the elements

there is no indexing
'''

# a = set()
# print(a)
# print(type(a))

a = {1,2,3,4,5,2,1,5}
# print(a)

# a.add(23)
# a.remove(2)
# a.discard(26)
# a.remove(26)
# print("before: ",a)

a = {1,2,3,4}
b = {4,5,6,7}

# TODO: union
# print(a.union(b))
# print(a | b)

# TODO: intersection

# print(a.intersection(b))
# print(a & b)

# TODO: sum difference

# print(a.difference(b))
# print(b.difference(a))

print(a - b)
print(b - a)