from lib.helpers import (
    list_members,
    list_classes,
    list_bookings,
    add_member,
    add_class,
    book_member,
    delete_member,
    delete_class
)

def menu():
    print("\n--- Gym Membership System ---")
    print("1. View all members")
    print("2. View all gym classes")
    print("3. View all bookings")
    print("4. Add a new member")
    print("5. Add a new class")
    print("6. Book a member into a class")
    print("7. Delete a member")
    print("8. Delete a class")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ")
        
        if choice == "1":
            list_members()
        elif choice == "2":
            list_classes()
        elif choice == "3":
            list_bookings()
        elif choice == "4":
            add_member()
        elif choice == "5":
            add_class()
        elif choice == "6":
            book_member()
        elif choice == "7":
            delete_member()
        elif choice == "8":
            delete_class()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
