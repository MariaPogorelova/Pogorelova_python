import re
p = re.compile(r"\bpython\b")
print ("Найдено" if p.search ("python") else "Нет")
# выдаст Найдено
print ("Найдено" if p.search("pythonware") else "Нет")
# выдаст Нет
p = re.compile(r"\Bth\B")
print ("Найдено" if p.search("python") else "Нет")
# выдаст Найдено
print ("Найдено" if p.search("this") else "Нет")
# выдаст Нет