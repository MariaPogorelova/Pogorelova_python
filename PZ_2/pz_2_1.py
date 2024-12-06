#Дано трехзначное число. Вывести число, полученное при перестановке цифр сотен и десятков исходного числа
number = input("Введите трёхзначное число: ")

while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print("Ошибка: Ввод должен быть числом.")
        number = input("Введите трёхзначное число: ")

if 100 <= number <= 999:
    a = number // 100  #3
    b = (number // 10) % 10    #2
    c = number % 10 #4
    result = b * 100 + a * 10 + c
    print(result)
else:
    print("Ошибка: Введите трёхзначное число. Перезапустите программу.")




