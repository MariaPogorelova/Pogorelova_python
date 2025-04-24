# В двумерном списке элементы последней строки заменить на 0.//
### Вариант 28
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Замена элементов последней строки на 0
matrix[-1] = [0] * len(matrix[0])
print("Матрица после преобразования:")
for row in matrix:
    print(row)
