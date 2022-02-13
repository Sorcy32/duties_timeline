from openpyxl import load_workbook
from datetime import datetime, timedelta
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


def open_excel(file='test2.xlsx'):
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
            column_name_number = cell.column - 1

    # Некоторые переменные, для работы далее
    header_isnt_got = True  # Для пропуска первой строки - заголовка
    first_date, last_date = None, None

    # Загружаем список искомых сотрудников
    seeked_empl_list = []
    with open('employees.txt', encoding='utf-8') as empl_file:
        for emplx in empl_file:
            seeked_empl_list.append(emplx.replace('\n', ''))

    # Начинаем перебор страницы
    # Перебираем строки таблицы и заполняем класс EploeeList (класс списка сотрудников). Добавляем в него список
    # сотрудников (Emploee) и дежурства (класс Dutie)
    for row in sheet:
        if header_isnt_got:  # Пропускаем заголовок таблицы excel
            header_isnt_got = False
            continue

        # Определяем дату начала и конца периода и записываем её в класс списка сотрудников
        rows_date = datetime.strptime(str(row[column_date_number].value), '%d.%m.%Y %H:%M:%S')
        if first_date is None:
            first_date = rows_date
        elif rows_date <= first_date:
            first_date = rows_date

        if last_date is None:
            last_date = rows_date
        elif rows_date >= last_date:
            last_date = rows_date

        # Проверяем есть ли сотрудник в списке сотрудников, которые нам необходимы для рассмотрения. Если нет -
        # пропускаем
        if row[column_name_number].value not in seeked_empl_list:
            continue

        # добавляем сотрудника в список сотрудников если его там нет
        if row[column_name_number].value not in empl_list.get_emploee_names():
            tmp_emploeer = emploee.Emploee(row[column_name_number].value)
            empl_list.add_emploee(tmp_emploeer)
        # добавляем сотруднику запись в дежурство
        tmp_emploee = empl_list.get_emploee_by_name(row[column_name_number].value)
        tmp_emploee.add_dutie(row[column_date_number].value, row[column_task_number].value,
                              row[column_state_number].value)
        empl_list.set_period_start_date(first_date)
        empl_list.set_period_finish_date(last_date)

    return empl_list


if __name__ == "__main__":
    open_excel()
