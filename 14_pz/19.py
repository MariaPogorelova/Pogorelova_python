# В двумерном списке найти среднее арифметическое элементов последних двух
# столбцов.//
### Вариант 19
import random
# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
# Нахождение среднего арифметического элементов последних двух столбцов
last_two_cols = [row[-2:] for row in matrix]
avg = sum(sum(col) for col in last_two_cols) / (2 * len(matrix))
print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"Среднее арифметическое последних двух столбцов: {avg}")