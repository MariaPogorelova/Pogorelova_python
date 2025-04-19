# В двумерном списке элементы второго столбца заменить элементами из
# одномерного динамического массива соответствующей размерности.

### Вариант 9
import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
for row in matrix:
    print(row)

# Замена элементов второго столбца на элементы из одномерного массива
new_column = [random.randint(1, 10) for _ in range(len(matrix))]
for i in range(len(matrix)):
    matrix[i][1] = new_column[i]

print("Исходная матрица после преобразования:")
for row in matrix:
    print(row)