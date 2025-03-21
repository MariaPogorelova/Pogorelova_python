try:
    f1 = open('file.txt', encoding='utf-8')
    lines = f1.readlines()
    count = 0
    for i in lines:
        count += 1
    print(f"Количество строк в файле", count)
    f1.close
except FileNotFoundError:
    print("Ошибка, файла не существует")
