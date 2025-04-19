# В двумерном списке найти минимальный элемент в предпоследней строке
### Вариант 21
import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]

# Нахождение минимального элемента в предпоследней строке
min_elem = min(matrix[-2])

print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"\nМинимальный элемент в предпоследней строке: {min_elem}")
