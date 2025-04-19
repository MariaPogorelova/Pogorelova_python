# Если в двумерном списке имеются положительные элементы, то вывести TRUE,
# иначе FALSE.
### Вариант 32
import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]

# Проверка наличия положительных элементов
has_positive = any(num > 0 for row in matrix for num in row)

print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"\nНаличие положительных элементов: {'TRUE' if has_positive else 'FALSE'}")