### Вариант 2
# В двумерном списке найти минимальный и максимальные элементы.ty
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]

# Нахождение минимального и максимального элементов
min_elem = min(min(row) for row in matrix)
max_elem = max(max(row) for row in matrix)

print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"Минимальный элемент: {min_elem}")
print(f"Максимальный элемент: {max_elem}")