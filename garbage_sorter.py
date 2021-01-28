'''
Программа сортировки мусора.
'''

container = [True, False, False, False, True, True, False] # Контейнер с алмазами и мусором

i = -1

while i < len(container)-1:
    i += 1 # при первом проходе станет нулем (индексы начинаются с 0)
    if container[i] == False:
        continue

    print(container[i])
