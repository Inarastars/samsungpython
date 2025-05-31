#умножение, создание ареа
width = 30
height = 60
area = width * height
print(f"Area of Rectangle: {area}")

#теорема пифагора
a = int(input("введите основание: "))
b = int(input("введите высоту: "))
c = (a**2 + b**2) ** 0.5
print(c)

#вычилить длину окружности и площадь круга
P = 3.141592
radius = float(input("введите радиус круга: "))
circumference = 2 * radius * P
area = P * radius ** 2
print(f"длина окружности = {circumference}, площадь = {area}")

#таблица чисел в степени 2
print(" a  n  a**n")
for a in range(2, 7):
    n= 2
    result = a**n
    print(f" {a}  {n}  {result}")