# Reverse of a string

def reverseString(string: str) -> str:
    return string[::-1]

# --------------------------------------------------------------

# Using loop
def reverseString1(string: str) -> str:
    reversed_string=""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

# --------------------------------------------------------------

# Using built-in function
def reverseString2(string: str) -> str:
    return ''.join(reversed(string))

# --------------------------------------------------------------



print(reverseString("HelloWorld"))
print(reverseString1("HelloWorld"))
print(reverseString2("HelloWorld"))