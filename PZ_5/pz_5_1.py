# Составить функцию, которая напечатает сорок любых символов

import random


def print_random_characters(num_symbols=40):
    symbols = ""

    while len(symbols) < num_symbols:
        symbol = chr(random.randint(32, 126))
        symbols += symbol

    print(symbols)


print_random_characters()

