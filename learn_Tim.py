'''
Программа сортировки чисел методом пузырька за K обменов по возрастанию.
'''

n = int(input("Введите любое натуральное число N меньше 100: "))
k = int(input("Введите любое целое неотрицательное K: "))

def enter_list(num): #формирование начального списка
    num_list = []
    i = 1
    while i <= num:
        num_list.append(i)
        i += 1
    return num_list

num_list = enter_list(n)
print("Исходный массив: "+str(num_list)+".")

#num_list = [5, 4, 3, 9, 1]

def descen_sort_list(unsorted_list):
    loc = 0
    i = 0
    j = 1
    while j < len(unsorted_list):
        i = 0
        while i < len(unsorted_list) - j:
            if unsorted_list[i] < unsorted_list[i + 1]:
                loc = unsorted_list[i + 1]
                unsorted_list[i + 1] = unsorted_list[i]
                unsorted_list[i] = loc
            i += 1
        j += 1
        if j == k:
            break
    return unsorted_list
print("Отсортированный по убыванию массив: "+str(descen_sort_list(num_list))+".")

def ascen_sort_list(unsorted_list):
    loc = 0
    i = 0
    j = 1
    while j < len(unsorted_list):
        i = 0
        while i < len(unsorted_list) - j:
            if unsorted_list[i] > unsorted_list[i + 1]:
                loc = unsorted_list[i + 1]
                unsorted_list[i + 1] = unsorted_list[i]
                unsorted_list[i] = loc
            i += 1
        j += 1
    return unsorted_list
print("Отсортированный по возрастанию массив: "+str(ascen_sort_list(num_list))+".")
