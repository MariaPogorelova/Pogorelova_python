### Вариант 4
# В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2 раза.//
import random
n = random.randint(3, 5)
matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Увеличение элементов не на главной диагонали в 2 раза
for i in range(n):
    for j in range(n):
        if i != j:
            matrix[i][j] *= 2

print("Исходная матрица после преобразования:")
for row in matrix:
    print(row)