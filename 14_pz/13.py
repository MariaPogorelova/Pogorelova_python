# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов
### Вариант 13

import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]

# Нахождение среднего арифметического для строк с нечетными номерами
for i in range(len(matrix)):
    if i % 2 != 0:
        avg = sum(matrix[i]) / len(matrix[i])
        print(f"Среднее арифметическое строки {i}: {avg:.2f}")

print("\nИсходная матрица:")
for row in matrix:
    print(row)