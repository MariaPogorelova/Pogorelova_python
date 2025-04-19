# Сгенерировать двумерный список, в которой элементы больше 10 заменяются на 0
### Вариант 30
import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 20) for _ in range(4)] for _ in range(4)]

# Замена элементов больше 10 на 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] > 10:
            matrix[i][j] = 0

print("Исходная матрица после преобразования:")
for row in matrix:
    print(row)