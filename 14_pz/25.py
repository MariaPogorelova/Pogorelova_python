# В двумерном списке найти сумму элементов второй половины матрицы.//
### Вариант 25
import random
# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Нахождение суммы элементов второй половины матрицы
half = len(matrix) // 2
sum_second_half = sum(sum(row) for row in matrix[half:])
print(f"Сумма элементов второй половины матрицы: {sum_second_half}")