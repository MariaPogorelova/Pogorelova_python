# В двумерном списке элементы последнего столбца заменить на -1.//
### Вариант 29
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Замена элементов последнего столбца на -1
for row in matrix:
    row[-1] = -1
print("Матрица после преобразования:")
for row in matrix:
    print(row)