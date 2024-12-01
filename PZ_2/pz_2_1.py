#Дано трехзначное число. Вывести число, полученное при перестановке цифр сотен и десятков исходного числа
try:
    number = int(input("Введите трёхзначное число: "))
    str_number = str(number)

    if len(str_number) == 3:
        new_number = str_number[1] + str_number[0] + str_number[2]
        result = int(new_number)
        print(result)
    else:
        print("Ошибка: Введите трёхзначное число.")
except Exception:
    print("Ошибка: Ввод должен быть числом.")

