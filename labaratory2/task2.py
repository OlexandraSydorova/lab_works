import re
def is_int(numb):
    return bool(re.match(r"^\d+$", numb))
def cycled_input(text):
    numb = input(text)
    while not is_int(numb):
        numb = input(text)
    return int(numb)
count = cycled_input("Введіть кількість ітерацій ")
x = cycled_input("Введіть x ")
result = 1
for i in range(1,count):
    result *= x/2**i
print("Результат", result)