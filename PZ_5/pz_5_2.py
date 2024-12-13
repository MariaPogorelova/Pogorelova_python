# Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
# Составить функцию, которая будет находить на сколько квадратов можно разрезать
# данный прямоугольник, если от него каждый раз отрезать квадрат наибольшей
# площади


def count_squares(a, b):
    if a == 0 or b == 0:
        return 0
    return a // b


def get_positive_integer(value):
    while True:
        try:
            res = int(input(value))
            if res > 0:
                return res
            else:
                print("Ошибка: Длина должна быть больше нуля.")
        except ValueError:
            print("Ошибка: Ввод должен быть числом.")


a = get_positive_integer("Укажите длину стороны a: ")
b = get_positive_integer("Укажите длину стороны b: ")


result = count_squares(a, b)
print(f"В прямоугольник со сторонами {a}x{b} помещяется квадратов: {result}")