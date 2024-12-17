# Дан целочисленный список размера N.
# Найти максимальное количество его одинаковых элементов.
import random
random_list = []
N = 10
for i in range(N):
    random_list.append(random.randint(0, 100))
print(f"Список создан:", random_list)

def max_similar_elements(random_list):
    random_list.sort()
    max_count = 1
    current_count = 1

    for i in range(1, len(random_list)):
        if random_list[i] == random_list[i - 1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1

    max_count = max(max_count, current_count)

    return max_count


result = max_similar_elements(random_list)
print("Максимальное количество одинаковых элементов:", result)


