# TODO: File Handling

'''
Files are used to store/retrieve the data

text : .doc, .txt, .py, .html
binary: .png, .jpg, .mp3, .mp4, .pdf

modes in file:
r -> read mode (will only be used if the file already exists)
w -> write mode
a -> append mode

modes in binary files:
rb -> read 
wb -> write

open(file_name, mode)
'''

try:

    # file = open("./test.py","r")
    file = open("./01functions.py", "r")
    # print(file)
    # print(file.read())
    # print(file.read(10))
    # file.seek(20)
    # print(file.read(10))
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())

    # print(file.readlines()[1])
    file.close()
except FileNotFoundError as e:
    print("ERROR: ", e)
    print("File does not exist")


# TODO: write in a file
# write mode overrides the existing data
file = open("./random.py","w")
file.write("#Hello, writing using python, Let's learn together")
file.writelines(['line1', 'line2', 'line3'])
file.close()

# TODO: write in a file
# append mode appends the data at the end
# file = open("./test.py","a")
# # file.write("#Hello, writing using python, Let's learn together")
# file.write("\n #Hello there")
# file.close()

# TODO: context manager

# with open("./test.py", "r") as f1:
#     print(f1.read())

# with open("./test.py", "r") as f1, open("./copy.py","w") as f2:
#     for data in f1:
#         f2.write(data)

# TODO: binary files
# with open("./1.png", "rb") as f1:
#     print(f1.read())

with open("./1.png", "rb") as f1, open("./copy.png", "wb") as f2:
    for data in f1:
        f2.write(data)
