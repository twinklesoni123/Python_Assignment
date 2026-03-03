def add(x, y):
    z = x + y
    print("Answer:", z)

def sub(x, y):
    z = x - y
    print("Answer:", z)

def mul(x, y):
    z = x * y
    print("Answer:", z)

def div(x, y):
    z = x / y
    print("Answer:", z)

def mod(x, y):
    z = x % y
    print("Answer:", z)


while True:

    print("\n---- CALC MENU ----")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Modulus")
    print("6 Exit")

    ch = int(input("Enter choice: "))

    if ch == 6:
        break

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    if ch == 1:
        add(x, y)

    elif ch == 2:
        sub(x, y)

    elif ch == 3:
        mul(x, y)

    elif ch == 4:
        div(x, y)

    elif ch == 5:
        mod(x, y)

    else:
        print("Invalid choice")