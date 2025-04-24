# Если в двумерном списке имеются положительные элементы, то вывести TRUE,
# иначе FALSE.//
### Вариант 32
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Проверка наличия положительных элементов
has_positive = any(num > 0 for row in matrix for num in row)
print(f"Наличие положительных элементов: {'TRUE' if has_positive else 'FALSE'}")