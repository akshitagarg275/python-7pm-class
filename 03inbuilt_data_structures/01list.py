# List , list()
'''
lists are mutable, iterable
lists have indexing to identify unique elements
index numbers start from 0
'''

colors = ["blue" , "red", "purple", "orange", "green"]
# print(colors)
# print(type(colors))
# print(dir(colors))

# TODO: mutability
# colors[0] = "yellow"
# print(colors)

# TODO: indexing
# print(colors[0])
# print(colors[0], colors[2])

# print(colors[-1])

# TODO: slicing
# list_name[start_index: end_index : step]
colors = ["blue" , "red", "purple", "orange", "green"]


# print(colors[1:4])
# print(colors[3:])
# print(colors[:])

# copy_list = colors[:]

# copy_list[0] = "yellow"

# print(colors)
# print(copy_list)

# print(colors[-4: -2])

# print(colors[: : 2])
# print(colors)

# print(colors[1:3])

# TODO: len
# print(len(colors))


# TODO: append
# print("colors before: ", colors)
# colors.append("gray")

# colors.extend(["brown", "gray"])
# print("colors after: ", colors)

# TODO: insert
# print("colors before: ", colors)

# colors.insert(1, "maroon")

# print("colors after: ", colors)

# colors.clear()
# del colors
# print(colors)
colors = ["blue" , "red", "purple", "orange", "green", "blue"]
# TODO: to count the occurrence of a particular element
# print(colors.count("blue"))
# print(colors.count('gray'))

# print(colors.index("blue"))
# print(colors.index("red"))

# print("colors before: ", colors)

# TODO: we provide the index value
# print(colors.pop())
# print(colors.pop(1))

# TODO: we provide the element value
# print(colors.remove("purple"))

# print("colors before: ", colors)

# TODO: sort
colors = ["blue" , "red", "purple", "orange", "green"]
# colors.sort()
# print(colors)

# colors = sorted(colors)
# print(colors)

# print(sorted(colors))

# TODO: reverse
# colors.reverse()
# print(colors)
# print(colors[: : -1])