# 20. Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения.
import  random
random_num = random.randint(0,20)
class Counter:

    def __init__(self,current_value=random_num):
        self.value = current_value
        self.initial_value = current_value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.initial_value -= 1
        self.value = self.initial_value

    def get_value(self):
        return self.value

my_counter = Counter()
print("Исходное значение:", my_counter.get_value())
my_counter.increment()
print("Функция инкремента: ",my_counter.get_value())
my_counter.decrement()
print("Функция декремента: ",my_counter.get_value())