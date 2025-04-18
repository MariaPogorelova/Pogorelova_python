# В двумерном списке найти среднее арифметическое положительных элементов,
# кратных 3.
### Вариант 27
import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]

# Нахождение среднего арифметического положительных элементов, кратных 3
elements = [num for row in matrix for num in row if num > 0 and num % 3 == 0]
avg = sum(elements) / len(elements) if elements else 0

print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"\nСреднее арифметическое положительных элементов, кратных 3: {avg:.2f}")