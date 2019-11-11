print("Сидорова Олександра Сергіївна\nЛабораторна робота №1 \nВаріант 18 \nОбчислення функції в залежності від значення введеної змінної \n")
from math import sin
import re
from validators.validators_library import validator
from validators.validators_library import re_float

x = float(validator(re_float,"Введіть х "))
if x<=3:
    print( x**2 +3*x+9)
else:
     print(sin(x)/(x**2-9))

