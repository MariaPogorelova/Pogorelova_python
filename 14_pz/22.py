# В двумерном списке найти минимальный элемент в предпоследнем столбце.//
### Вариант 22
import random
# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
# Нахождение минимального элемента в предпоследнем столбце
min_elem = min(row[-2] for row in matrix)
print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"Минимальный элемент в предпоследнем столбце: {min_elem}")