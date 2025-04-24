# В двумерном списке элементы кратные 3 увеличить в 3 раза.//
### Вариант 18
import random
# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Увеличение элементов, кратных 3, в 3 раза
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] % 3 == 0:
            matrix[i][j] *= 3
print("Исходная матрица после преобразования:")
for row in matrix:
    print(row)