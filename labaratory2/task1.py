print("Сидорова Олександра Сергіївна\nЛабораторна робота №2 \nВаріант 18 \nЗнаходження найменшого числа K при 3K>N \n")
K = 1
import re
from validators.validators_library import validator
from validators.validators_library import re_int

N = int(validator(re_int,"Введіть ціле число N більше за 1 "))
while 3*K<=N:
    K+=1
print("Найменше значення К при якому 3К>N ",K)
