# strings , str()

'''
iterbale, immutable, indexable
'''

st = "python"
# print(st)
# print(type(st))
# print(len(st))

# TODO: iterable
# for s in st:
#     print(s)

# print(dir(st))

# print(st[0])

# TODO: immutable
# st[0] = "Z"
# print(st)

st = "python"

# print(st.capitalize())
# print(st.lower())
# print(st.upper())
# print(st.endswith('on'))
# print(st.startswith('P'))

# print(st.find("yt",3))

# print(st.index('yh'))

# print(st.center(50,'*'))
# print(st.count('p'))

st="PYTHON12"
# print(st.isupper())
# print(st.islower())

# print(st.isalpha())
# print(st.isalnum())

# print(st.isdigit())

# passwd = "             "
# print(passwd.isspace())

# print(st.isidentifier())

# TODO: replace
email = "xyz@gmail.com.i"
# print(email.replace('@','-'))
# print(email.replace('.','@'))
# print(email.replace('.','#',1))

# TODO: join
fname = "john"
lname = "doe"
uname = '.'.join([fname,lname])
# print(uname)
domain = "xyz.com"
email = '@'.join([uname, domain])
# print(email)

# TODO: split
msg = "we are learning python"
# print(msg.split())
# print(msg.split(" ", 2))
# print(msg.split('a'))

# TODO: strip
passwd = "            password           "
# print(passwd.lstrip())
# print(passwd.rstrip())
# print(passwd.strip())


# TODO: concatentation
num1 = 5
num2 = 2
ans = num1 + num2
# 5 + 2 = 7
# print(str(num1) + " + " + str(num2) + " = " + str(num1+num2))


# TODO: format
# res = "{} + {} = {}".format(num1,num2,ans)
# res = "{1} + {0} = {2}".format(num1,num2,ans)

# print(res)

# TODO: f-strings
# print(f"{num1} + {num2} = {ans}")

# TODO: raw strings
'''
\b -> backspace
\t -> tab
\n -> new line
\\ -> \
\' -> '
\a -> alert
'''

# path = r'C:\new_folder\temp\app'
# print(path)

# TODO: slicing
st="PYTHON12"
# print(st[2:5])