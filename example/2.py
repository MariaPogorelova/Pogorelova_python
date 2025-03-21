
def find_string_in_file(filename, search_string):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if search_string in line:
                    print(f"Строка найдена в строке № {line_number}: '{line.strip()}'")
                    return
                    print(f"Ошибка: Строка '{search_string}' не найдена в файле.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")


filename='text.txt'
search_string='Звучал булат, картечь визжала,'
find_string_in_file(filename, search_string)