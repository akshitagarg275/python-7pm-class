# Main file: To perform calculations

import simple_calc

# print(simple_calc.add(1,5))

# from simple_calc import add, sub

# print(add(1,2))
# print(sub(5,3))
# print(dir())

# import aliasing
from complex_calc import area_of_rect as ar

# print(ar(4,5))

# print(__name__)

def main():
    print("area of rectangle is: ", ar(5,6))

if __name__ == '__main__':
    print("This is the entry point")
    main()


