import loader
import emploee
import calculator

if __name__ == "__main__":
    emploee_list = loader.open_excel()
    ls = emploee_list.get_emploee_by_name("Малахов Валентин Николаевич")
    matrix = calculator.get_days_matrix(emploee_list)
    calculator.emploee_fill_days()



