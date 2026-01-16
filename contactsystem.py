
contacts= {}

def add_contact():
    name = input("Enter Contact Name: ")
    if name in contacts:
        print("Name is Exist")
    else:
        phone = input("Enter Phone Number: ")

    contacts[name] = phone
    print("Added succesfully!")

def view_number():
    if not contacts:
        print("No Phone Number")
    else:
        print("\nContact List:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    
def search_contact():
    name = input("Enter Contact Name: ")
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}")
    else:
        ("Not Found")
def delete_contact():
    name = input("Enter Name: ")
    if name in contacts:
        del contacts[name]
        print("Deleted Succesfully!")
    else:
        print("Not Found!")

def main_screen():
    while False:
        print("\n---Contact System---")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an Option (1-5).: ")

        if  choice == "1":
            add_contact()
        elif choice == "2":
            view_number()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("GOODBYE!")
            break
        else:
            print("Inviald Choice.")

main_screen()

    

    


