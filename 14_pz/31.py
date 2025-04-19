# Сгенерировать двумерный список, в которой нечетные элементы заменяются на 0.
### Вариант 31
import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]

# Замена нечетных элементов на 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] % 2 != 0:
            matrix[i][j] = 0

print("Исходная матрица после преобразования:")
for row in matrix:
    print(row)