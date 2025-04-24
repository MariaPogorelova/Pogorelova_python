# В двумерном списке найти среднее арифметическое положительных элементов.//
### Вариант 26
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Нахождение среднего арифметического положительных элементов
positive_elements = [num for row in matrix for num in row if num > 0]
avg = sum(positive_elements) / len(positive_elements) if positive_elements else 0
print(f"Среднее арифметическое положительных элементов: {avg}")