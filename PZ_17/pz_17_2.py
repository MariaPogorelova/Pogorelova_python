#Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара взаимно противоположных.
from tkinter import *

def find_count(event):
    try:
        n1 = int(num1.get())
        n2 = int(num2.get())
        n3 = int(num3.get())
    except ValueError:
        result['text'] = ('Ошибка! Введите корректные значения')
        return
    check_num = (n1 == -n2) or (n1 == -n3) or (n2 == -n3)
    result['text'] = f"Среди трех данных \nцелых чисел \nесть хотя бы \nодна пара \nвзаимно противоположных? {check_num}"

root = Tk()
root.title('Поиск взаимно противоположных чисел')
root.geometry('500x200')

Label(text="Первое число").grid(row=1, column=0)
num1 = Entry()
num1.grid(row=1, column=1)


Label(text="Второе число").grid(row=2, column=0)
num2 = Entry()
num2.grid(row=2, column=1)

Label(text="Третье число").grid(row=3, column=0)
num3 = Entry()
num3.grid(row=3, column=1)

button1 = Button(text="Обработать")
button1.grid(row=4, column=1)

result = Label()
result.grid(row=5, column=1)

button1.bind('<Button-1>',find_count)

root.mainloop()
