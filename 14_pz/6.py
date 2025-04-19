### Вариант 6 В двумерном списке элементы первого столбца возвести в куб
import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
for row in matrix:
    print(row)

# Возведение элементов первого столбца в куб
for row in matrix:
    row[0] = row[0] ** 3

print("Исходная матрица после преобразования:")
for row in matrix:
    print(row)