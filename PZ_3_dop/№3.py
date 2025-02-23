number = input("Введите число: ")
while True:
    try:
        number = int(number)
        if 10 <= number <= 99:
            break
        else:
            print("Ошибка: Число должно быть двухзначным.")
            number = input("Введите двухзначное число: ")
    except ValueError:
        print("Ошибка: Ввод должен быть числом.")
        number = input("Введите двузначное число: ")
a = number // 10 #десятки
b = number % 10 #единицы
if (a + b) % 2 == 0:
    result = number * 2
else:
    result = number / 2
print("Результат:", result)
#gr