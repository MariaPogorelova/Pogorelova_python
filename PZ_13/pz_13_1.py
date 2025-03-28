# В двумерном списке найти сумму элементов первых двух строк.
size = int(input("Введите размер массива: "))
matrix = [[i + j * size for i in range(size)] for j in range(size)]

print("Исходная матрица:")
for row in matrix:
    print(*row)