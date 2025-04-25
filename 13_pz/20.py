# В двумерном списке найти сумму элементов первых двух строк.//
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
# Нахождение суммы элементов первых двух строк
sum_first_two = sum(sum(row) for row in matrix[:2])
print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"\nСумма элементов первых двух строк: {sum_first_two}")