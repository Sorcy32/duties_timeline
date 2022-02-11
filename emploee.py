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
    __day_name = None
    __day_number = None
    __tasks_list = []
    __fitst_in_progress_state_time = None
    __last_finish_state_time = None

    def __init__(self):
        pass


class Emploee:
    __name = "None"
    __duties = []
    __days = []

    def __init__(self, name):
        self.__name = name
        self.__duties = []

    def add_dutie(self, date, task, state):
        """
        Adds a dutie tu a duties list
        :param date: date of a record
        :param task: task number (iccedent or task)
        :param state: state of iccident of task
        """
        temp_task = Dutie(date, task, state)
        self.__duties.append(temp_task)

    def get_duties(self):
        return self.__duties

    def get_first_date_of_dutie(self):
        pass

    def get_name(self):
        return self.__name

    def __repr__(self):
        return f"Сотрудник {self.__name} сделал {len(self.__duties)} изменений."


class EploeeList:
    emloeelist = []
    emploee_names_list = []
    period_start_date, period_finish_date = None, None

    def __init__(self):
        pass

    def add_emploee(self, empl):
        self.emloeelist.append(empl)
        self.emploee_names_list.append(empl.get_name())

    def get_emploee_names(self):
        return self.emploee_names_list

    def get_emploee_by_name(self, name):
        for eml in self.emloeelist:
            if eml.get_name() == name:
                return eml

    def get_emploee_list(self):
        return self.emloeelist

    def set_period_start_date(self, date):
        self.period_start_date = date

    def set_period_finish_date(self, date):
        self.period_finish_date = date

    def get_period_finish_date(self):
        return self.period_finish_date

    def get_period_start_date(self):
        return self.period_start_date

    def __repr__(self):
        return f"Список сотрудников содержит имён: {len(self.emploee_names_list)}"
