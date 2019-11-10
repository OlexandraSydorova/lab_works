print("Сидорова Олександра Сергіївна\nЛабораторна робота №1 \nВаріант 18 \nВизначення введеного символу \n")
import re
def is_symbol(symbol):
    return bool(re.match(r"^.{1}$", symbol))
def cycled_input(text):
    symbol = input(text)
    while not is_symbol(symbol):
        symbol = input(text)
    return symbol

x = cycled_input("Введіть символ ")
if x.isdigit():
    print("Ви ввели цифру")
elif x.isalpha():
     print("Ви ввели букву")
else:
     print("Ви ввели не букву або не цифру")

