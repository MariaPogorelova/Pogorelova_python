# В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два раза./
### Вариант 8
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
N = int(input("Введите номер столбца N(1-4): "))

# Увеличение элементов столбца N в 2 раза
for row in matrix:
    row[N-1] *= 2

print("Исходная матрица после преобразования:")
for row in matrix:
    print(row)