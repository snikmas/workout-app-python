def output_menu(menu):
    for menuItem in menu:
        print(menuItem)

def get_int_input(min, max):
    user = input()
    while user.isdigit() == False or int(user) < min or int(user) > max:
        print("Invalid input, try again...")
        user = input()
    return user