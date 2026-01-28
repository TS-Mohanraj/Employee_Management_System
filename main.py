from database import create_table
from employee import add_employee, search_employee, view_employee, update_employee, promote_employee, delete_employee

def menu():
    print("----------Employee Management System-----------------")
    print("1.Add Employee")
    print("2.Search Employee by ID")
    print("3.View Records")
    print("4.Update Employees")
    print("5.Promote Employees")
    print("6.Delete Employee")
    print("7.Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Enter your choice:")
        match choice:
            case "1":
                add_employee()
            case "2":
                search_employee()
            case "3":
                view_employee()
            case "4":
                update_employee()
            case "5":
                promote_employee()
            case "6":
                delete_employee()
            case "7":
                print("exiting program....")
                break
            case _:
                print("invalid choice!")

if __name__ == '__main__':
    main()

