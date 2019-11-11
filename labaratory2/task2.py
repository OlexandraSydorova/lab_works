"""Обчислити за допомогою оператора for"""
import re
from validators.validators_library import validator
from validators.validators_library import re_int
count = int(validator(re_int,"Введіть кількість ітерацій "))
x = int(validator(re_int,"Введіть x "))
result = 1
for i in range(1,count):
    result *= x/2**i
print("Результат", result)