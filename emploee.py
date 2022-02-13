import datetime


class Dutie:
    _date = None
    _task = None
    _state = None

    def __init__(self, date, task, state):
        """
        Dutie date.
        :param date: date of a record
        :param task: task number (iccedent or task)
        :param state: state of iccident of task
        """
        self._date = datetime.datetime.strptime(str(date), '%d.%m.%Y %H:%M:%S')
        self._task = task
        self._state = state

    def get_date(self):
        return self._date

    def get_task(self):
        return self._task

    def get_state(self):
        return self._state

    def __lt__(self, other):
        return self._date < other.get_date()

    def __repr__(self):
        return f'Дата:  {self.get_date()}  Документ: {self.get_task()} Состояние: {self.get_state()}'


class Day:
    __day_date = None
    __day_number = None
    __tasks_list = []
    __fitst_in_progress_state_time = None
    __last_finish_state_time = None

    def __init__(self, date, number):
        self.__day_date = date
        self.__day_number = number

    def add_task(self, task):
        self.__tasks_list.append(task)

    def set_first_state_in_work(self, date):
        self.__fitst_in_progress_state_time = date

    def set_last_finish_state_time(self, date):
        self.__last_finish_state_time = date

    def get_first_state_in_work(self):
        return self.__fitst_in_progress_state_time

    def get_last_finish_state_time(self):
        return self.__last_finish_state_time

    def get_day_date(self):
        return self.__day_date

    def __lt__(self, other):
        return self.__day_date < other.get_day_date()

    def __repr__(self):
        try:
            in_work = self.get_last_finish_state_time() - self.get_first_state_in_work()
        except TypeError:
            in_work = None
        return f'Число: {self.get_day_date()}, первое "в работе" {self.get_first_state_in_work()}' \
               f', последнее "завершен" {self.get_last_finish_state_time()}, ' \
               f'Отработал {in_work} '


class Emploee:
    __name = "None"
    __duties = None
    __days = None
    __days_dates_list = []

    def __init__(self, name):
        self.__name = name
        self.__duties = []
        self.__days = []
        self.__days_dates_list = []

    def add_dutie(self, date, task, state):
        """
        Adds a dutie tu a duties list
        :param date: date of a record
        :param task: task number (iccedent or task)
        :param state: state of iccident of task
        """
        temp_task = Dutie(date, task, state)
        self.__duties.append(temp_task)

    def add_day(self, day):
        self.__days.append(day)
        self.__days_dates_list.append(day.get_day_date())

    def get_duties(self):
        return self.__duties

    def get_first_date_of_dutie(self):
        pass

    def get_name(self):
        return self.__name

    def get_days(self):
        return self.__days

    def get_all_days_dates(self):
        tmpor = []
        for x in self.__days:
            tmpor.append(x.get_day_date())
        return tmpor

    def sort_days(self):
        self.__days.sort()

    def get_average_work_time(self):
        time = []
        try:
            for day in self.get_days():
                t = day.get_last_finish_state_time() - day.get_first_state_in_work()
                t = t.seconds
                time.append(t)
            t2 = sum(time)/len(time)
            z = datetime.timedelta(seconds=t2)
            return str(z).split(".")[0]
        except TypeError:
            return False

    def __repr__(self):
        return f"Сотрудник {self.__name} среднее время работы {self.get_average_work_time()}."


class EploeeList:
    __emloeelist = []
    period_start_date, period_finish_date = None, None

    def __init__(self):
        pass

    def add_emploee(self, empl):
        self.__emloeelist.append(empl)

    def get_emploee_names(self):
        t = []
        for x in self.__emloeelist:
            t.append(x.get_name())
        return t

    def get_emploee_by_name(self, name):
        for eml in self.__emloeelist:
            if eml.get_name() == name:
                return eml

    def get_emploee_list(self):
        return self.__emloeelist

    def set_period_start_date(self, date):
        self.period_start_date = date

    def set_period_finish_date(self, date):
        self.period_finish_date = date

    def get_period_finish_date(self):
        return self.period_finish_date

    def get_period_start_date(self):
        return self.period_start_date

    def __repr__(self):
        return f"Список сотрудников содержит имён: {len(self.__emloeelist)}"
