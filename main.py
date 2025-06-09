import user_interface

def print_menu():
    print('*********************************')
    print("** Evidence of Insured Persons **")
    print('*********************************')
    print("\nOptions:")
    print("1 - Add a new insured person")
    print("2 - Show all insured persons")
    print("3 - Search for an insured person")
    print("4 - Quit the program")

def main():
    while True:
        try:
            print_menu()
            choice = int(input("Your choice: "))
            match choice:
                case 1:
                    user_interface.add_new()
                    input("Press Enter to continue...")
                case 2:
                    user_interface.show_all()
                    input("Press Enter to continue...")
                case 3:
                    user_interface.search_by_name(input("Enter person like 'Name Surname:'\n"))
                    input("Press Enter to continue...")
                case 4:
                    print("App is closing ...")
                    break
                case _:
                    print("Enter a valid choice.")
                    input("Press Enter to continue...")
        except ValueError:
            print("Enter a valid number (1–4).")
            input("Press Enter to continue...")

main()