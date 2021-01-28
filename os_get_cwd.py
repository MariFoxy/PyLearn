'''
Программа, выводящая место запуска программы (конкретную директорию).
'''

from os import getcwd
where_i_am = getcwd()
print(where_i_am)
