# В двумерном списке найти максимальный положительный элемент, кратный 4.
### Вариант 23
import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]

# Нахождение максимального положительного элемента, кратного 4
max_elem = max(max(row) for row in matrix)
max_elem = max(num for row in matrix for num in row if num > 0 and num % 4 == 0)

print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"\nМаксимальный положительный элемент, кратный 4: {max_elem}")