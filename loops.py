'''
Программа отражающая функционал оператора while.
'''

i = 0

while i < 10: #условие
    i += 1

    if i == 7:
        #break - оператор прерывания цикла
        continue #continue - начинает следующий проход цикла, минуя оставшееся тело цикла

    a = 3 * i #оставшееся тело цикла
    print(i, a) #оставшееся тело цикла

else:
    print("Конец цикла") #else - выполняется в конце цикла, если нет прерываний
