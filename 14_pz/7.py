# В двумерном списке элементы строки N (N задать с клавиатуры) увеличить на 3.//
### Вариант 7
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)

N = int(input("Введите номер строки N: "))
# Увеличение элементов строки N на 3
for j in range(len(matrix[N])):
    matrix[N-1][j] += 3

print("Исходная матрица после преобразования:")
for row in matrix:
    print(row)