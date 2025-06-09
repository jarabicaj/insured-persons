from insured_person import InsuredPerson

def add_new():
    print("\nAdd new insured person:")

    while True:
        name = input("Enter name: ").strip()
        if name:
            break
        else:
            print("Enter the name!")

    while True:
        surname = input("Enter surname: ").strip()
        if surname:
            break
        else:
            print("Enter the surname!")

    phone = input("Enter phone number: ").strip()

    while True:
        age = input("Enter age: ").strip()
        if age.isdigit() and int(age) > 0:
            break
        else:
            print("Enter the valid age!")

    person = InsuredPerson(name, surname, phone, age)
    InsuredPerson.add_person(person)
    print("Person added!")

def search_by_name(whole_name):
    whole_name_ls=whole_name.split()
    p = InsuredPerson.get_one(whole_name_ls)
    if p:
        print("")
        print(f"{'Name':<10} {'Surname':<10} {'Phone-Nr.':<12} {'Age'}")
        print(p)
        print("")
    else:
        print("No insured person found.")

def show_all():
    persons = InsuredPerson.get_all()
    if not persons:
        print("No insured persons found.")
        return

    print("\nAll insured persons:")
    print(f"{'Name':<10} {'Surname':<10} {'Phone-Nr.':<12} {'Age'}")
    for p in persons:
        print(p)
    print("")