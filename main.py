from datetime import datetime, timedelta



"""
for x in totallist:
    print(x)
    pass
"""

#  Собираем по фамилиям
engineers = []
for row in totallist:
    if row[2] not in engineers:
        engineers.append(row[2])

# делаем диапазон необходимых дат
start_date_for_search = datetime.strptime("30.12.2021 00:00", "%d.%m.%Y %H:%M")
finish_data_for_search = datetime.strptime("09.01.2022 23:59", "%d.%m.%Y %H:%M")
days = finish_data_for_search - start_date_for_search
days = days.days

# Разбиваем работы на дни для простоты подсчета
days_list = []  # Список дней, которые рассматриваем
for x in range(days+1):
    day = start_date_for_search + timedelta(days=x)
    days_list.append(day)

cool_total_list = days_list.copy() # список дней, в которых уже строки из списка общего заявок

for row in totallist:
    for searched_day in days_list:
        if row[0].day == searched_day.day and row[0].month == searched_day.month and row[0].year == searched_day.year:
            #print(row[0], searched_day)
            index = days_list.index(searched_day)
            tmp = []
            tmp = [cool_total_list[index], row]
            cool_total_list[index] = tmp
    # Проверка не осталось ли незаполненных ячеек в списке (если не было ничего на дату - значит не добавилась вторая
    # ячейка
for x in cool_total_list:
    if type(x) == datetime:
        index = cool_total_list.index(x)
        cool_total_list[index] = [cool_total_list[index], None]

print(cool_total_list[2][1])




