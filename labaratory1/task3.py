print("Сидорова Олександра Сергіївна\nЛабораторна робота №1 \nВаріант 18 \nВизначення введеного символу \n")
import re
from validators.validators_library import validator
from validators.validators_library import re_symbol

x = validator(re_symbol,"Введіть символ ")
if x.isdigit():
    print("Ви ввели цифру")
elif x.isalpha():
     print("Ви ввели букву")
else:
     print("Ви ввели не букву або не цифру")

