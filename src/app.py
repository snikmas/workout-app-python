from src.managers.user_manager import UserManager
from utils.constants import *
from utils.helpers import *
from managers.program_manager import *
from managers.database_manager import *

class App:
    def __init__(self):
        self.currentUser = None
        self.db = None
        self.userManager = None
        self.databaseManager = None
        self.programManager = None
        # actually, no need for db.connection. this is db layer logic

    def run(self):
        self.databaseManager = DatabaseManager()
        self.programManager = ProgramManager(self.currentUser, self.databaseManager)
        self.userManager = UserManager(self.currentUser, self.databaseManager)

        print("hi")
        is_user = False
        if self.currentUser:
            is_user = self.currentUser

        if is_user:
            output_menu(menu_user)
            input = get_int_input(0, 4)

            match input:
                case 1:
                    print("start a new work session")
                case 2:
                    print("my work programs")

                case 3:
                    print("my progress history")
                case 4:
                    print("=== Library Exercises ===")
                    all_exercises = self.programManager.get_all_exercises()
                case 5:
                    print("my accou settings")
                case 6:
                    print("log out")
                case 0:
                    print("See you next time!")
                    return

        else:
            output_menu(menu_no_user)
            input = get_int_input(0, 6)
            match input:
                case 1:
                    print("login")
                case 2:
                    print("register")
                    print("Nice to meet you!\nInput your username:")
                    username = get_str_input(30, None)
                    print("Input your email:")
                    email = get_str_input(50, None)
                    print("Input your password (8+ symbols; contains digits and special symbols):")
                    password = get_str_input(50, "password")
                    password_hash = get_password_hash(password)
                    # connect to db
                    self.userManager.register_user(username, email, password_hash)



                    print("The Account Has Been Created!")
                    return # for now

                case 3:
                    print("library exersice")
                    print("=== Library Exercises ===")
                    #get list of it
                    exercises, total_exercises, total_pages = self.programManager.get_all_exercises()
                    if exercises is None:
                        print("some issus")
                        return
                    elif exercises == 403:
                        print("403 problrm. write frmo the run")


                    # output using helpers.
                    output_exercises(exercises, total_exercises, total_pages)


                case 4:
                    print("try a random workout")
                case 0:
                    print("See you next time!")
                    return

