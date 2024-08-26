# dictionary, dict()
'''
mutables, iterables

{key: value}
Individual value can be uniquely accessed using the 
key in dictionaries

- Key of dictionaries can only be immutable datatype
(string, float, int, tuple)
'''

# stu = {
#     "fname" : "John",
#     "lname" : "Doe",
#     "class" : ["python", "programming"],
#     "age" : 23
# }

# print(stu)
# print(type(stu))
# print(len(stu))

# print(stu["fname"])

# stu["fname"] = 'Jane'

# stu["country"] = "USA"
# print(stu)

# print(dir(stu))

# print(stu.keys())
# print(stu.values())
# print(stu.items())

# print("before: ", stu)
# stu.pop("class")
# stu.pop("absd")

# stu.popitem()

# stu.clear()
# print("after: ", stu)


# keys = ["name", "age", "class"]

# student = dict.fromkeys(keys,"default")
# print(student)

# TODO: get

# print(stu)
# print(stu.get("fname"))

# print(stu.get('Name'))
# print(stu.get('Name', 'NA'))
# print(stu['Name'])





stu = {
    "fname" : "John",
    "lname" : "Doe",
    "class" : ["python", "programming"],
    "age" : 23
}

# a = {}
# print(type(a))

# new_stu = dict(**stu, country = "USA")
# print(new_stu)
