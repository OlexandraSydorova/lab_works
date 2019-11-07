print("Сидорова Олександра Сергіївна\nЛабораторна робота №1 \nВаріант 18 \nЗнаходження суми арифметичної прогресії \n")
import re

def is_int(numb):
    return bool(re.match(r"^\d+$", numb))
def cycled_input(text):
    numb = input(text)
    while not is_int(numb):
        numb = input(text)
    return int(numb)


a = cycled_input("Введіть перший член прогресії ")
d = cycled_input("Введіть різницю прогресії ")
n = cycled_input("Введіть число членів прогресії ")
print("Сума членів прогресії")
s = ((2 * a + d * (n - 1)) / 2) * n
print(s)

