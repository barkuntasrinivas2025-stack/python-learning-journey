print("Hello, World!")
a = int(input("Enter a number: "))
b =float(input("Enter a decimal number: "))
c =str(input("Enter an operator (+, -, *, /): "))
if(c == "+"):
    print("The sum of the numbers is: ")
    print(a+b)
elif(c == "-"):
    print("The difference of the numbers is: ")
    print(a-b)
elif(c == "*"):
    print("The product of the numbers is: ")
    print(a*b)
elif(c == "/"):
    print("The quotient of the numbers is: ")
    print(a/b)
else:    print("Invalid operator")