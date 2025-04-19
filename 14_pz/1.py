### Вариант 1.
# Перенести в новый двумерный список Matr1 элементы, которые не находятся в
# первых и последних строках и столбцах матрицы Matr2 произвольного размера.
import random

# Создание случайной матрицы Matt2
rows = random.randint(3, 5)
cols = random.randint(3, 5)
Matt2 = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

# Перенос элементов, не находящихся в первых и последних строках и столбцах
Matt1 = [row[1:-1] for row in Matt2[1:-1]]

print("Исходная матрица Matt2:")
for row in Matt2:
    print(*row)
print("\nНовая матрица Matt1:")
for row in Matt1:
    print(row)