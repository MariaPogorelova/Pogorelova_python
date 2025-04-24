### Вариант 3
# В двумерном списке элементы на главной диагонали увеличить в 2 раза//
import random

# Создание случайной квадратной матрицы
n = random.randint(3, 5)
matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
print("Исходная матрица:")
for row in matrix:
    print(row)

# Увеличение элементов на главной диагонали в 2 раза
for i in range(n):
    matrix[i][i] *= 2

print("Исходная матрица после преобразования:")
for row in matrix:
    print(row)