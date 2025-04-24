### Вариант 1.
# Перенести в новый двумерный список Matr1 элементы, которые не находятся в
# первых и последних строках и столбцах матрицы Matr2 произвольного размера.
import random
rows = random.randint(3, 5)
cols = random.randint(3, 5)
Matr2 = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

# Перенос элементов, не находящихся в первых и последних строках и столбцах
Matr1 = [row[1:-1] for row in Matr2[1:-1]]

print("Исходная матрица Matr2:")
for row in Matr2:
    print(row)
print("\nНовая матрица Matr1:")
for row in Matr1:
    print(row)
