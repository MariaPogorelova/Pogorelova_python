# Используя словарь посчитать количество уникальных слов в заданном
# предложении «Изучаем язык Питон». Вывести на экран каждую пару
# «ключ:значение»

sentence = "Изучаем язык Питон Изучаем язык Питон"
words = sentence.split() #list
words_dict = {}
for word in words:
    words_dict[word] = words.count(word)
for word, count in words_dict.items():
    print(f"{word}: {count}")


