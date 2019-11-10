print("Сидорова Олександра Сергіївна\nЛабораторна робота №1 \nВаріант 18 \nОбчислення функції в залежності від значення введеної змінної \n")
from math import sin
import re
def is_float(numb):
    return bool(re.match(r"^[+-]{0,1}\d+\.{0,1}\d*$", numb))
def cycled_input(text):
    numb = input(text)
    while not is_float(numb):
        numb = input(text)
    return float(numb)


x = cycled_input("Введіть х ")
if x<=3:
    print( x**2 +3*x+9)
else:
     print(sin(x)/(x**2-9))

