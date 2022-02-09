from _datetime import datetime, timedelta, date


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


def emploee_fill_days(emploee, template_matrix):
    dut = emploee.get_duties()
    # TODO сделать сортировку по времени и датам и наполнять класс сотрудника днями на основании шаблона матрицы.
    for duty in dut:
        pass


def get_fitst_in_wokrk_time(day):
    pass
