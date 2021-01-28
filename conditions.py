'''
Программа сравнения 2-х чисел.
'''

from random import randint #из модуля random импортируем функцию randint

a = randint(0, 100) #0 - 100 - промежуток формирования значений
b = randint(0, 100)

print('a=%s, b=%s' % (a, b)) #%s - подстановка значений из % (a,b)

if a > b:
    print("a больше b")
elif a < b:
    print("b больше a")
else:
    print("a = b")
