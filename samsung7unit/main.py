#буква константа или нет
letter = input("Enter the alphabet: ").lower()
if letter in {'a', 'e', 'i', 'o', 'u'}:
    print(f"{letter.upper()} is a vowel")
else:
    print(f"{letter.upper()} is a consonant")

#кратно ли число a b
a, b = map(int, input("Write two integers: ").split())
if a % b == 0:
    print(f"{a} is a multiple of {b}")
else:
    print(f"{a} is not a multiple of {b}")

#является ли числа а кратным b
a = int(input("Enter the intenger: "))
b = int(input("Enter the intenger: "))
if a % b == 0:
    print(f"{a} is a multiple of {b}")
else:
    print(f"{a} is not a multiple of {b}")


#программа арифметических операций
print("1) Addition  2) Subtraction  3) Multiplication  4) Divisio")
choice = input("Enter the desired number of operation: ")

if choice not in ["1", "2", "3", "4"]:
    print("Enterated an incorrect number.")
else:
    print("Enter two numbers for operation.")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice =="1":
        result = num1+num2
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice =="3":
        result = num1*num2
        print(f"{num1} * {num2} = {result}")
    else:
        if num2 == 0:
            print("Error")
        else:
            result = num1/num2
            print(f"{num1} / {num2} = {result}")

#опредение в какой четверти находится координаты
x = int(input("Enter x coordinat: "))
y = int(input("Enter y coordinat: "))
if x>=0 and y>=0:
    print("Coordinats in the first quadrant.")
elif x>=0 and y<=0:
    print("Coordinats in the fourth quadrant.")
elif x<=0 and y<=0:
    print("Coordinats in the third quadrant.")
elif x<=0 and y>=0:
    print("Coordinats in the second quadrant.")

#меню ресторана
print("Welcome to yummy restaurant. Here is the menu.")
print("- Burger(enter b)")
print("- Chicken(enter c)")
print("- Pizza(enter p)")

while True:
    choice = input("Choose a menu (enter b,c,p): ").lower()

    if choice == 'b':
        print("You chose Burger.")
        break
    elif choice == 'c':
        print("You chose Chicken.")
        break
    elif choice == 'p':
        print("You chose Pizza.")
        break
    else:
        print("Enter the menu again:")