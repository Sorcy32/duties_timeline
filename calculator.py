from _datetime import datetime, timedelta
import emploee


def calculate_number_of_period_days(emploeelist):
    start_datetime = emploeelist.get_period_start_date().replace(hour=0, minute=0, second=0, microsecond=0)
    stop_datetime = emploeelist.get_period_finish_date().replace(hour=0, minute=0, second=0, microsecond=0)
    delta = stop_datetime - start_datetime
    delta = delta.days + 1
    return start_datetime, stop_datetime, delta


def get_days_matrix(empl_list):
    start, stop, delta = calculate_number_of_period_days(empl_list)
    matrix = []
    for day in range(delta):
        day_number = start + timedelta(days=day)
        matrix.append(day_number)
    return matrix


def emploee_fill_days(emploe):
    dut = emploe.get_duties()
    dut.sort()  # Сортируем список дежурств по датам записи
    for dduty in dut:
        if dduty.get_state() in ['Принят', 'Назначен', "Отменён", "Отложен"]:
            continue
        tmp_day = None
        if len(emploe.get_days()) == 0 or dduty.get_date().replace(hour=0, minute=0, second=0,
                                                                   microsecond=0) not in emploe.get_all_days_dates():
            tmp_day = emploee.Day(dduty.get_date().replace(hour=0, minute=0, second=0, microsecond=0),
                                  dduty.get_date().day)
            emploe.add_day(tmp_day)
        else:
            for x in emploe.get_days():
                if dduty.get_date().replace(hour=0, minute=0, second=0, microsecond=0) == x.get_day_date():
                    tmp_day = x

        if dduty.get_date().replace(hour=0, minute=0, second=0, microsecond=0) in emploe.get_all_days_dates():
            for dday in emploe.get_days():
                if dday.get_day_date() == dduty.get_date().replace(hour=0, minute=0, second=0, microsecond=0):
                    dday.add_task(dduty)
                if dduty.get_state() == "В работе" and dday.get_first_state_in_work() is None:
                    tmp_day.set_first_state_in_work(dduty.get_date())
                if dduty.get_state() == "Завершен" or dday.get_last_finish_state_time() is None:
                    tmp_day.set_last_finish_state_time(dduty.get_date())
    emploe.sort_days()


def make_global_table(emploee_list, matrix, table_type):
    goal_list = []

    empl_list = emploee_list.get_emploee_list()
    for man in empl_list:
        tmp_emlpoeer = []

        dct = {'Name': man.get_name()}
        for x in matrix:
            dct.update({x: ''})

        for day in man.get_days():
            try:
                if table_type == 'First':
                    dct.update({day.get_day_date(): day.get_first_state_in_work().time().isoformat(timespec='minutes')})
                elif table_type == 'Last':
                    dct.update({day.get_day_date(): str(day.get_last_finish_state_time()
                                                        .time().isoformat(timespec='minutes'))})
                elif table_type == 'Middle':
                    t = 'Er'
                    try:
                        t = str(day.get_middle_state_date()).split(":")[0] \
                            + ":" \
                            + str(day.get_middle_state_date()).split(":")[1]
                    except IndexError:
                        pass
                    dct.update({day.get_day_date(): t})
            except AttributeError:
                dct.update({day.get_day_date(): 'Er'})
        for values in dct.values():
            tmp_emlpoeer.append(values)


        goal_list.append(tmp_emlpoeer)
    return goal_list
