# В двумерном списке найти максимальный положительный элемент, кратный 4.//
### Вариант 23
import random
# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
filtered = [num for row in matrix for num in row if num > 0 and num % 4 == 0]
if filtered:
    max_elem = max(filtered)
    print(f"Максимальный положительный элемент, кратный 4: {max_elem}")
else:
    print("Таких элементов нет.")

