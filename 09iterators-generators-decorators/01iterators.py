# TODO: iterators
'''
__iter__ : iter() method is the initialisation method.
        It returns an iterator object

__next__ : next() method returns the next value for the iterable
'''

# st = "python"
# it = iter(st)
# print(it)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


colors = ["blue", "green", "red", "orange", "yellow"]

# for c in colors:
#     print(c)

it = iter(colors)
print(it.__next__())