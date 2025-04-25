# В двумерном списке найти сумму и произведение элементов строки N (N задать с
# клавиатуры).//
### Вариант 11

import random
# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
N = int(input("Введите номер строки N(1-4): "))
# Нахождение суммы и произведения элементов строки N
row = matrix[N-1]
sum_row = sum(row)
product_row = 1
for num in row:
    product_row *= num

print(f"Сумма элементов строки {N}: {sum_row}")
print(f"Произведение элементов строки {N}: {product_row}")