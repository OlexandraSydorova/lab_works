"""Написати програму-фільтр, яка при натисканні будь-яких клавіш виводить на екран тільки букви і цифри, при цьому вказуючи, що виводиться: буква або цифра."""
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

