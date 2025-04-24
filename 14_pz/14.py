# Для каждого столбца матрицы с четным номером найти сумму ее элементов.//
### Вариант 14
import random
# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Нахождение суммы элементов столбцов с четными номерами
for j in range(len(matrix)):
    if j % 2 == 0:
        col_sum = sum(row[j] for row in matrix)
        print(f"Сумма столбца {j}: {col_sum}")
