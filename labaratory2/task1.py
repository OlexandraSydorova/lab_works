""" Дано ціле число N(>1). Знайти найменше ціле число K, при якому виконується нерівність 3K>N."""
K = 1
import re
from validators.validators_library import validator
from validators.validators_library import re_int

N = int(validator(re_int,"Введіть ціле число N більше за 1 "))
while 3*K<=N:
    K+=1
print("Найменше значення К при якому 3К>N ",K)
