"""Перевірити у математичному вираженні, заданому рядком, відповідність відкриваючих і закриваючих дужок."""
"""Порахувати кількість відкриваючих і закриваючих дужок і перевірити чи рівні ці два числа"""
def counting(expression):
    """
Ця функція рахує кількість відкриваючих і закриваючих дужок і перевіряє на рівність цих чисел
    :param expression: str
    :return: True or False
    """
    count1 = 0
    count2 = 0
    for elem in expression:
        if elem == '(':
            count1 += 1
        if elem == ')':
            count2 += 1
    if count1 == count2:
        return True
    elif count1 != count2:
        return False

expr = input("Введіть математичне вираження ")
if counting(expr):
    print("Ви ввели правильний математичний вираз")
elif not counting(expr):
   print("Ви ввели не правильний математичний вираз")


