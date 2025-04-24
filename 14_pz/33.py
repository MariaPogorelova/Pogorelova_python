# Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.//
### Вариант 33
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Формирование массива из положительных четных элементов
positive_even = [num for row in matrix for num in row if num > 0 and num % 2 == 0]
sum_even = sum(positive_even)
avg_even = sum_even / len(positive_even) if positive_even else 0

print(f"Массив положительных четных элементов: {positive_even}")
print(f"Сумма: {sum_even}, Среднее арифметическое: {avg_even}")