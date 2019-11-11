print("Сидорова Олександра Сергіївна\nЛабораторна робота №3 \nВаріант 18 \nПеревірка відповідності відкриваючих і закриваючих дужок \n")
def counting(expression):
    count1 = 0
    count2 = 0
    for elem in expression:
        if elem == '(':
            count1 += 1
        if elem == ')':
            count2 += 1
    return count1,count2

expr = input("Введіть математичне вираження ")
count1,count2 = counting(expr)
if count1 == count2:
    print("Ви ввели правильний математичний вираз")
elif count1 != count2:
   print("Ви ввели не правильний математичний вираз")


