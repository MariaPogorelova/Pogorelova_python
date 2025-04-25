# В двумерном списке найти отрицательные элементы, сформировать из них новый
# массив. Вывести размер полученного массива.//
### Вариант 24
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Формирование массива из отрицательных элементов
negative_elements = [num for row in matrix for num in row if num < 0]
print(f"Массив отрицательных элементов: {negative_elements}")
print(f"Размер массива: {len(negative_elements)}")
