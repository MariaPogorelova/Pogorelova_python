#Дан список размера N и целые числа K и L (1 < K < L < N ). Найти среднее
#арифметическое элементов список с номерами от K до L включительно.

import random
list = []
N = 10
for i in range(N):
    list.append(random.randint(0, 100))
print(f"Список создан:", list)

while True:
    try:
        K = int(input("Введите значение K (1 <= K < L): "))
        if K >= 1 and K < N:
            break
        else:
            print("Неправильно ввели! (1 <= K < N)")
    except ValueError:
        print("Ошибка: Ввод должен быть числом.")

while True:
    try:
        L = int(input("Введите значение L (K < L < N): "))
        if L > K and L <= N:
            break
        else:
            print("Неправильно ввели! (K < L <=  N)")
    except ValueError:
        print("Ошибка: Ввод должен быть числом.")




def average_of_list(list, K, L):
    elements_of_list = list[K-1:L]
    total_sum = sum(elements_of_list)
    count = len(elements_of_list)
    average = total_sum / count

    return average

result = average_of_list(list, K, L)
print(f"Среднее арифметическое элементов с номерами от {K} до {L} включительно: {result}")