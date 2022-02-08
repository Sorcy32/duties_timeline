from openpyxl import load_workbook
from datetime import datetime
import emploee
totallist = []

with open('data.txt', encoding='UTF-8') as f:
    ctr = 0
    for x in f:
        if ctr == 0:
            ctr += 1
        else:
            da = (x.split('	'))
            tmp = [datetime.strptime(da[0], "%d.%m.%Y %H:%M"), da[1], da[2].replace("\n", "")]
            totallist.append(tmp)


def openexcel():
    book = load_workbook('test.xlsx')
    sheet = book.active
    # emploee_list = []  # Список работников
    # Ищем столбцы с необходимой информацией
    column_date_number, column_task_number, column_state_number, column_name_number = 0, 0, 0, 0
    empl_list = emploee.EploeeList()
    for cell in sheet["1"]:
        if cell.value == 'Состояние':
            column_state_number = cell.column - 1
        elif cell.value == 'Период':
            column_date_number = cell.column - 1
        elif cell.value == 'Документ':
            column_task_number = cell.column - 1
        elif cell.value == 'Установил' and column_name_number == 0:
            column_name_number = cell.column - 1  # TODO разобраться почему -1

    for row in sheet:
        if row[column_name_number].value not in empl_list.get_emploee_names():
            tmp_emploeer = emploee.Emploee(row[column_name_number].value)
            tmp_emploeer.add_dutie(row[column_date_number].value, row[column_task_number].value, row[column_state_number].value)
            empl_list.add_emploee(tmp_emploeer)
        # print(row[column_task_number].value)
        # empl = emploee.Emploee()
    test = empl_list.get_emploee_list()
    for x in test:
        for z in x.get_duties():
            print(z.state())
            pass




openexcel()


