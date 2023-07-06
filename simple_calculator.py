# defining functions for the calculator : add, sub, mul , div
# printing options to the user
# asking for values
# calling functions
# loop till the user exits the program

def add(a,b):
    answer = a + b
    print(str(a)+"+"+str(b)+"=" + str(answer))


def sub(a,b):
    answer = a - b
    print(str(a)+"-"+str(b)+"=" + str(answer))


def mul(a,b):
    answer = a * b
    print(str(a)+"x"+str(b)+"=" + str(answer))


def div(a,b):
    answer = a / b
    print(str(a)+"/"+str(b)+"=" + str(answer))


print("""A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Exit""")
while True:
    choice = str.upper(input("Input your choice: "))

    if choice == 'A':
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number:"))
        add(a, b)
    elif choice == 'B':
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number:"))
        sub(a, b)
    elif choice == 'C':
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number:"))
        mul(a,b)
    elif choice == 'D':
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number:"))
        div(a,b)
    elif choice == 'E':
        print("End")
        quit()

