# В двумерном списке найти суммы элементов каждой строки и поместить их в новый
# массив. Выполнить замену элементов третьего столбца исходной матрицы на
# полученные суммы.//
### Вариант 16
import random
# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Нахождение сумм элементов каждой строки
row_sums = [sum(row) for row in matrix]
print('Сумма элементов каждой строки', row_sums)
# Замена элементов третьего столбца на суммы строк
for i in range(len(matrix)):
    matrix[i][2] = row_sums[i]
print("Матрица после преобразования:")
for row in matrix:
    print(row)