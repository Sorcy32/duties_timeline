from openpyxl import load_workbook
from datetime import datetime
import emploee


def open_txt():
    """
    doesn't work
    :return:
    """
    with open('data.txt', encoding='UTF-8') as f:
        totallist = []
        ctr = 0
        for x in f:
            if ctr == 0:
                ctr += 1
            else:
                da = (x.split('	'))
                tmp = [datetime.strptime(da[0], "%d.%m.%Y %H:%M"), da[1], da[2].replace("\n", "")]
                totallist.append(tmp)


def open_excel(file='test.xlsx'):
    """
    Loads File by name and convert data to a EmploeeList
    :param file: name of the input-data file
    :return: EmploeeList
    """
    book = load_workbook(file)
    sheet = book.active
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
    # Перебираем строки таблицы и заполняем класс EploeeList (класс списка сотрудников). Добавляем в него список
    # сотрудников (Emploee) и дежурства (класс Dutie)
    for row in sheet:
        # добавляем сотрудника в список сотрудников если его там нет
        if row[column_name_number].value not in empl_list.get_emploee_names():
            tmp_emploeer = emploee.Emploee(row[column_name_number].value)
            empl_list.add_emploee(tmp_emploeer)
        # добавляем сотруднику запись в дежурство
        tmp_emploee = empl_list.get_emploee_by_name(row[column_name_number].value)
        tmp_emploee.add_dutie(row[column_date_number].value, row[column_task_number].value,
                              row[column_state_number].value)

    return empl_list


if __name__ == "__main__":
    open_excel()


