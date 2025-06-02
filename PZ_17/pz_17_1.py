from tkinter import *

root = Tk()
root.title('Форма регистрации')
root.geometry('700x400')



user_info = LabelFrame(root, text='Данные для входа пользователя')
user_info.pack(fill='both', padx=10, pady=10)
user_info_name = Label(user_info, text='Имя пользователя:').grid(row=0, column=0, sticky='w', padx=5, pady=5)
input_name = Entry(user_info).grid(row=0, column=1, padx=5, pady=5)
user_info_email = Label(user_info, text='Электронная почта:').grid(row=1, column=0, sticky='w', padx=5, pady=5)
input_email = Entry(user_info).grid(row=1, column=1, padx=5, pady=5)
user_info_psw = Label(user_info, text='Пароль:').grid(row=2, column=0, sticky='w', padx=5, pady=5)
input_psw = Entry(user_info).grid(row=2, column=1, padx=5, pady=5)

personal_data = LabelFrame(root, text='Персональные данные')
personal_data.pack(fill='both', padx=10, pady=10)
pers_data_addr = Label(personal_data, text='Домашний адрес:').grid(row=0, column=0, sticky='w', padx=5, pady=5)
input_addr = Entry(personal_data).grid(row=0, column=1, padx=5, pady=5)
pers_data_addr = Label(personal_data, text='Дата рождения:').grid(row=1, column=0, sticky='w', padx=5, pady=5)
input_addr = Entry(personal_data).grid(row=1, column=1, padx=5, pady=5)
pers_data_addr = Label(personal_data, text='Ваш возраст:').grid(row=2, column=0, sticky='w', padx=5, pady=5)
input_addr = Entry(personal_data).grid(row=2, column=1, padx=5, pady=5)



root.mainloop()
