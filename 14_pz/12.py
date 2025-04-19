# В двумерном списке найти сумму и произведение элементов столбца N (N задать с
# клавиатуры).
### Вариант 12
import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
N = int(input("Введите номер столбца N: "))

# Нахождение суммы и произведения элементов столбца N
column = [row[N] for row in matrix]
sum_col = sum(column)
product_col = 1
for num in column:
    product_col *= num

print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"\nСумма элементов столбца {N}: {sum_col}")
print(f"Произведение элементов столбца {N}: {product_col}")