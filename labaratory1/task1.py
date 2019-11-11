print("Сидорова Олександра Сергіївна\nЛабораторна робота №1 \nВаріант 18 \nЗнаходження суми арифметичної прогресії \n")
import re
from validators.validators_library import validator
from validators.validators_library import re_int

a = int(validator(re_int,"Введіть перший член прогресії "))
d = int(validator(re_int,"Введіть різницю прогресії "))
n = int(validator(re_int,"Введіть число членів прогресії "))
print("Сума членів прогресії")
s = ((2 * a + d * (n - 1)) / 2) * n
print(s)

