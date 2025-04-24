# В двумерном списке элементы третьей строки заменить элементами из одномерного
# динамического массива соответствующей размерности.//
### Вариант 10
import random
# Создание случайной матрицы
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Замена элементов третьей строки на элементы из одномерного массива
new_row = [random.randint(1, 10) for _ in range(len(matrix[0]))]
print('Одномерный массив: ', new_row)
matrix[2] = new_row

print("Матрица после преобразования:")
for row in matrix:
    print(row)