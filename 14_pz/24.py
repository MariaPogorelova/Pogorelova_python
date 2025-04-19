# В двумерном списке найти отрицательные элементы, сформировать из них новый
# массив. Вывести размер полученного массива.
### Вариант 24
import random

# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]

# Формирование массива из отрицательных элементов
negative_elements = [num for row in matrix for num in row if num < 0]

print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"\nМассив отрицательных элементов: {negative_elements}")
print(f"Размер массива: {len(negative_elements)}")
