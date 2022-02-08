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
    name = "None"
    duties = []

    def __init__(self, name):
        self.name = name

    def add_dutie(self, date, task, state):
        """
        Adds a dutie tu a duties list
        :param date: date of a record
        :param task: task number (iccedent or task)
        :param state: state of iccident of task
        :return:
        """
        temp_task = Dutie(date, task, state)
        self.duties.append(temp_task)

    def get_duties(self):
        return self.duties

    def get_first_date_of_dutie(self):
        pass

    def get_name(self):
        return self.name

    def __repr__(self):
        return f"Сотрудник {self.name} сделал {len(self.duties)} изменений."
        # return f"Emploee {self.name}"


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

"""gusakov = Emploee('Gusakov')
for x in range(10):
    gusakov.add_dutie("06.02.2022", 'testtusknumber' + str(x), 'в работе')

print(gusakov)
test2 = gusakov.get_duties()
for x in test2:
    print(x)

kleshev = Emploee('Gusakov')
for x in range(15):
    kleshev.add_dutie("06.02.2022", 'testtusknumber' + str(x), 'в работе')

print(kleshev)
test2 = kleshev.get_duties()
for x in test2:
    print(x)
"""