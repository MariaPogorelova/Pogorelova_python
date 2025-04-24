# Сгенерировать двумерный список на произвольное количество элементов, в которой
# задается преобразование от предыдущего элемента к следующему на произвольное
# значение.//
### Вариант 17
import random
# Создание случайной матрицы с преобразованием
n = random.randint(3, 5)
matrix = [[random.randint(1, 5) for _ in range(n)]]
for _ in range(1, n):
    new_row = [x + random.randint(1, 3) for x in matrix[-1]]
    matrix.append(new_row)
print("Сгенерированная матрица:")
for row in matrix:
    print(row)