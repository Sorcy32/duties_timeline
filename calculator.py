from _datetime import datetime, timedelta, date
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


def emploee_fill_days_(emploe):
    emploe_duties = emploe.get_duties()
    for duty in emploe_duties:
        if len(emploe.get_days()) == 0 or duty.get_date().replace(hour=0, minute=0, second=0,
                                                                microsecond=0) not in emploe.get_all_days_dates():
            tmp_day = emploee.Day(duty.get_date().replace(hour=0, minute=0, second=0, microsecond=0),
                                  duty.get_date().day)
            emploe.add_day(tmp_day)
        else:
            for day in emploe.get_days():
                if day.get_day_date() == duty.get_date().replace(hour=0, minute=0, second=0, microsecond=0):
                    tmp_day = day


