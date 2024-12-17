# Дан список размера N, все элементы которого, кроме одного, упорядочены по
# убыванию. Сделать список упорядоченным, переместив элемент, нарушающий
# упорядоченность, на новую позицию.
def fix_decreasing_list(random_list):
    if len(random_list) < 2:
        return random_list

    index_out_of_order = -1
    for i in range(1, len(random_list)):
        if random_list[i] > random_list[i - 1]:
            index_out_of_order = i
            break

    if index_out_of_order == -1:
        return random_list

    el_out_of_order = random_list[index_out_of_order]
    random_list.pop(index_out_of_order)

    for i in range(len(random_list)):
        if el_out_of_order > random_list[i]:
            random_list.insert(i, el_out_of_order)
            return random_list

    random_list.append(el_out_of_order)
    return random_list


random_list = [5, 4, 3, 2, 6, 1]
print("Исходный список:", random_list)
sorted_list = fix_decreasing_list(random_list)
print("Упорядоченный список:", sorted_list)

