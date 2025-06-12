#вывести список через цикл
bts = ["V", 'J-Hope', 'RM', 'Jungkook', 'Jin', 'Jimin', 'Suga']
for member in bts:
    print(member)

#сумма от 1 до 100
print("Sum of integers from 1 to 100:", sum(range(1, 101)))

#сумма от 1 до 100 с использованием step
sum_even = 0
for number in range(2, 101, 2):
    sum_even += number

print("Sum of even numbers from 1 to 100:", sum_even)

#сумма нечетных чисел от 1 до 100
print("Sum of odd numbers from 1 to 100:", sum(range(1, 101, 2)))

#матрица
n = int(input("Enter n: "))
matrix = []
num = 1
for row in range(n):
    if row % 2 == 0:
        matrix.append(list(range(num, num + n)))
    else:
        matrix.append(list(range(num + n - 1, num - 1, -1)))
    num += n
for row in matrix:
    print(' '.join(map(str, row)))

