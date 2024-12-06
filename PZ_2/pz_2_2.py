#вывод трехзначного числа с измененным порядком цифр сотен и десятков
number = input("Введите трёхзначное число: ")
while True:
    try:
        number = int(number)
        if 100 <= number <= 999:
            break
        else:
            print("Ошибка: Введите трёхзначное трёхзначное число.")
            number = input("Введите трёхзначное число: ")
    except ValueError:
        print("Ошибка: Ввод должен быть числом.")
        number = input("Введите трёхзначное число: ")

a = number // 100
b = (number // 10) % 10
c = number % 10

result = b * 100 + a * 10 + c
print(f"Результат после перестановки: {result}")




