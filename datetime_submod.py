'''
Программа, форматирующая текущую дату и время.
'''

import datetime
import time

date_now = datetime.date.isoformat(datetime.date.today()) #isoformat - приводит дату к строковому типу
print(date_now)

time_now = time.strftime("%A %p %I:%M") #strftime - находит день недели, PM/AM, часы:минуты
print(time_now)
