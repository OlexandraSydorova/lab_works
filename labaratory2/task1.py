print("Сидорова Олександра Сергіївна\nЛабораторна робота №2 \nВаріант 18 \nЗнаходження найменшого числа K при 3K>N \n")
K = 1
import re
def is_int(numb):
    return bool(re.match(r"^\d+$", numb))
def cycled_input(text):
    numb = input(text)
    while not is_int(numb) or int(numb)<=1:
        numb = input(text)
    return int(numb)


N = cycled_input("Введіть ціле число N більше за 1 ")
while 3*K<=N:
    K+=1
print("Найменше значення К при якому 3К>N ",K)
