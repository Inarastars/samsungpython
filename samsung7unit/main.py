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