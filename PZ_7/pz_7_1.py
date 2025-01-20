#Дано целое положительное число. Вывести символы, изображающие цифры этого
#числа (в порядке слева направо).

def check_number(value):
    while True:
        try:
            num = int(input(value))
            if num > 0:
                return num
            else:
                print("Ошибка: Длина должна быть больше нуля.")
        except ValueError:
            print("Ошибка: Ввод должен быть числом.")

number = check_number("Введите число: ")
result = []
for i in str(number):
    result.append(int(i))
print(result)

