"""Обчислення конкретної функції, в залежності від введеного значення х"""
from math import sin
import re
from validators.validators_library import validator
from validators.validators_library import re_float

x = float(validator(re_float,"Введіть х "))
if x<=3:
    print( x**2 +3*x+9)
else:
     print(sin(x)/(x**2-9))

