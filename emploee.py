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
        self._date = date
        self._task = task
        self._state = state

    def date(self):
        return self._date

    def task(self):
        return self._task

    def state(self):
        return self._state

    def __repr__(self):
        return f'Дата:  {self.date()}  Документ: {self.task()} Состояние: {self.state()}'


class Emploee:
    __name = "None"
    __duties = []

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

    def __repr__(self):
        return f"Список сотрудников содержит имён: {len(self.emploee_names_list)}"
