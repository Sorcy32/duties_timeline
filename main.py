import loader
import emploee
import calculator
import time

if __name__ == "__main__":
    emploee_list = loader.open_excel()
    # matrix = calculator.get_days_matrix(emploee_list)
    for man in emploee_list.get_emploee_list():
        calculator.emploee_fill_days(man)
    for x in emploee_list.get_emploee_list():
        print(x)
        x.get_average_work_time()
        for z in x.get_days():
            print(z)
            pass





