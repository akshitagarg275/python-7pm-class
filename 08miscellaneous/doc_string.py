# Doc strings
# __doc__

# TODO: using triple quotes:
def my_func():
    '''Demonstration of writing doc strings
    using triple quotes'''

# print(my_func.__doc__)
# print(help(my_func))

# TODO: Google style doc-string
def sum(a, b):
    """
    Add two numbers and returns the result.

    Args:
        a(int): The first number.
        b(int): The second number.
    
    Returns:
        int: The sum of a and b.
    """
    return a + b

# TODO: Numpydoc-style doc strings
def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : int
        First Number.
    b : int
        Second Number.
    
    Returns
    -------
    int
        Multiplication of the numbers
    """
    
    return a * b