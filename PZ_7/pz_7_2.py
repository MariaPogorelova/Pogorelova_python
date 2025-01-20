#Дана строка, состоящая из русских слов, набранных заглавными буквами и
#разделенных пробелами (одним или несколькими). Преобразовать каждое слово в
#строке, заменив в нем все последующие вхождения его первой буквы на символ «.»
#(точка). Например, слово «МИНИМУМ» надо преобразовать в «МИНИ.У».
#Количество пробелов между словами не изменять.

string = "ОЛОВО ОЛОВО"
words = string.split(' ')

def change_string(word):
    if not word:
        return word
    first_letter = word[0]
    check = first_letter
    for char in word[1:]:
        if char == first_letter:
            check += '.'
        else:
            check += char
    return check

change_words = [change_string(word) for word in words]

result = ' '.join(change_words)

print(result)

