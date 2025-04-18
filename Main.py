from Library import Library

L1 = Library({},{})
while True:
    print("\nActions that can be performed:")
    print("\n1. Add Book")
    print("\n2. Display Book")
    print("\n3. Remove Book")
    print("\n4. Issue Book")
    print("\n5. Return Book")
    print("\n6. Add user")
    print("\n7. Display Users")
    print("\n8. Exit")
    num_choice = int(input("\n Please input the action you want to perform:"))
    match num_choice:
        case 1:
            L1.add_book()
        case 2:
            L1.display_all_books()
        case 3:
            L1.remove_book()
        case 4:
            L1.issue_book()
        case 5:
            L1.return_book()
        case 6:
            L1.register_user()
        case 7:
            L1.display_all_users()
        case 8:
            exit()
        case _:
            print("Invalid choice. Please select a valid option.")