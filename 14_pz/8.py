# В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два
# раза.
### Вариант 8
import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
for row in matrix:
    print(row)
N = int(input("Введите номер столбца N: "))

# Увеличение элементов столбца N в 2 раза
for row in matrix:
    row[N] *= 2

print("Исходная матрица после преобразования:")
for row in matrix:
    print(row)