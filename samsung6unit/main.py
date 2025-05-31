#опыт, если больше 1000, пишется что мастер
game_score = int(input("введите колво опыта: "))
print(f"game_score = {game_score}")
if game_score > 1000:
    print("You are a master")

#проверка числа в диапозоне от -100 до 100
x = int(input("введите число: "))
if -100 < x < 100:
    print(f"x = {x}")
    if x > 0:
        print(f"{x} is natural number")
else:
    print("ошибка: число должно быть между -100 до 100")

#проверка возраст
age = int(input(" введите возраст: "))
if age <= 10:
    print("Kid")
elif age <= 20:
    print("Youth")
else:
    print("Adult")

#возраст и рост
age = int(input(" введите возраст: "))
height = int(input(" введите рост: "))
if age <= 10:
    print("Kid")
elif age <= 20:
    print("Youth")
else:
    print("Adult")
print(f"your height is {height}")
print("you can enter.")