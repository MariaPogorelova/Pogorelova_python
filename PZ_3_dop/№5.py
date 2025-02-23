a, b = float(input("Введите первое число: ")), float(input("Введите второе число: "))
num_sum = a + b
if num_sum % 5 == 0:
    result = num_sum + 1
else:
    result = num_sum - 1
print("Результат:", result)