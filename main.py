import loader
import emploee
import calculator
import saver

if __name__ == "__main__":
    # TODO сделать проверку для отделения в записях нарядов и обращений. Для инженеров нужно использовать только наряды

    x = input('Регистр сведений - состояния. Файл данных - input.xlsx')
    emploee_list = loader.open_excel()
    matrix = calculator.get_days_matrix(emploee_list)
    for man in emploee_list.get_emploee_list():
        calculator.emploee_fill_days(man)

    headers = ['Ф.И.О']
    matrix.sort()
    for x in matrix:
        headers.append(str(x.day) + '.' + str(x.month))

    table = calculator.make_global_table(emploee_list, matrix, 'First')
    # saver.save_long_list(table, headers, sheet_name='Начало дня')
    telbe = calculator.make_global_table(emploee_list, matrix, 'Last')
    telbem = calculator.make_global_table(emploee_list, matrix, 'Middle')
    # saver.save_long_list(telbe, headers, sheet_name='Конец дня')
    saver = saver.Saver()
    saver.add_sheet(table, headers, 'Начало дня')
    saver.add_sheet(telbe, headers, 'Конец дня')
    saver.add_sheet(telbem, headers, 'Время работы')
    saver.save()






