import functions

program_finished = False
main_menu_op = (('Enter 1 to display all Items',),
                ('Enter 2 to search Item details',),
                ('Enter 3 to add Items',),
                ('Enter 4 to modify Items',),
                ('Enter 5 to remove Items',),
                ('Enter 6 to manage users',),
                ('Enter 7 to exit',))

user_op = (('Enter 1 to display all users',),
           ('Enter 2 to search users',),
           ('Enter 3 to change username',),
           ('Enter 4 to delete Items',),
           ('Enter 5 to go back to main menu',))


username = functions.log_in()

while not program_finished:
    print(functions.table_display(main_menu_op, ['Main Menu']))
    choice = input('-> ')
    while type(choice) is str:
        if choice.isdigit():
            if int(choice) in range(1, 8):
                choice = int(choice)
            else:
                print('Enter a valid choice')
                choice = input()
        else:
            print('Enter a valid choice')
            choice = input()

    if choice == 1:
        print(functions.display_items())
        input('Press Enter to go to Main Menu')

    elif choice == 2:
        print(functions.search())
        input('Press Enter to go to Main Menu')

    elif choice == 3:
        functions.add_items()
        input('Press Enter to go to Main Menu')

    elif choice == 4:
        functions.modify()
        input('Press Enter to go to Main Menu')

    elif choice == 5:
        functions.remove()
        input('Press Enter to go to Main Menu')

    elif choice == 6:
        managing_users = True
        while managing_users:
            print(functions.table_display(user_op, ['Manage Users']))
            user_choice = input('-> ')
            if user_choice == '1':
                print(functions.see_users())
                input('Enter to go back')
            elif user_choice == '2':
                print(functions.search_user())
                input('Enter to go back')
            elif user_choice == '3':
                functions.change_username()
                input('Enter to go back')
            elif user_choice == '4':
                functions.delete_users()
                input('Enter to go back')
            elif user_choice == '5':
                managing_users = False

    elif choice == 7:
        program_finished = True
        print('Program exited...')


functions.close(username)
