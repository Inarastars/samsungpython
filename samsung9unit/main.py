#умножение на 2
i = 1
while i <= 9:
    print(f"2 * {i} = {2 * i}")
    i += 1

#вывод от 1 до 9 через умножение
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1

#является ли число палиндромом
number = input("Enter an integer: ")

if number == number[::-1]:
    print(f"{number} is a palindrome number")
else:
    print(f"{number} is not a palindrome number")

#игра угадай число
import random
secret_number = random.randint(1, 100)
attempts = 0

print("Guess a number between 1 to 100")

while True:
    guess = int(input("Enter a number: "))
    attempts += 1

    if guess < secret_number:
        print("Higher!")
    elif guess > secret_number:
        print("Lower!")
    else:
        print(f"Congratulations. Total try = {attempts}")
        break