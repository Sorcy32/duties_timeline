from openpyxl import Workbook
from datetime import datetime
import pandas as pd

wb = Workbook()
ws = wb.create_sheet("Output", 0)
dt_now = (str(datetime.strftime(datetime.now(), "%d.%m.%y %H.%M.%S")) + '.xlsx')


def save_long_list(data_set, header, sheet_name='Sorcy32'):
    data = [header]
    for x in data_set:
        data.append(x)
    time_now = str(datetime.now())[0:19].replace(":", ".")
    filename = time_now + ".xlsx"
    df = pd.DataFrame(data)
    with pd.ExcelWriter(filename, index=False, header=False) as wr:
        df.to_excel(wr, sheet_name=sheet_name, index=False, header=False)
    print('Сохранение успешно завершено.')


class Saver:
    datasets = {}

    def __init__(self):
        time_now = str(datetime.now())[0:19].replace(":", ".")
        filename = time_now + ".xlsx"
        self.writer = pd.ExcelWriter(filename, engine='openpyxl', index=False, header=False)
        self.datasets = {}

    def add_sheet(self, data_set, header, sheet_name='Sorcy32'):
        data = [header]
        for x in data_set:
            data.append(x)
        df = pd.DataFrame(data)
        self.datasets.update({sheet_name: df})

    def save(self):
        for k, v in self.datasets.items():
            v.to_excel(self.writer, sheet_name=k, index=False, header=False)
        self.writer.save()
        self.writer.close()
