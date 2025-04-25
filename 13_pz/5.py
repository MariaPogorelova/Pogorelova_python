# В двумерном списке элементы второго столбца возвести в квадрат./
### Вариант 5
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Возведение элементов второго столбца в квадрат
for row in matrix:
    row[1] = row[1] ** 2

print("Исходная матрица после преобразования:")
for row in matrix:
    print(row)