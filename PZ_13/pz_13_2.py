# В двумерном списке найти минимальный и максимальные элементы.
size = int(input("Введите размер массива: "))
matrix = [[i + j * size for i in range(size)] for j in range(size)]

print("Исходная матрица:")
for row in matrix:
    print(*row)

min_num = min((min(_) for _ in matrix))
print('Минимальное число: ', min_num)

max_num = max((max(_) for _ in matrix))
print('Максимальное число: ', max_num)