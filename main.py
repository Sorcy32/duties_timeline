import loader
import emploee

if __name__ == "__main__":
    emploee_list = loader.open_excel()
    print(emploee_list)
