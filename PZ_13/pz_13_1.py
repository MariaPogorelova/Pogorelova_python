# # В двумерном списке найти сумму элементов первых двух строк.
size = int(input("Введите размер массива: "))
matrix = [[i + j * size for i in range(size)] for j in range(size)]

print("Исходная матрица:")
for row in matrix:
    print(*row)

sum_first_two_rows = sum(map(sum, matrix[:2]))

print("Сумма элементов первых двух строк:", sum_first_two_rows)