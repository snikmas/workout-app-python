from utils.constants import *
from utils.helpers import *
from managers.program_manager import *

class App:
    def __init__(self):
        self.currentUser = None
        self.db = None #later connect to the db

    def run(self):
        programManager = ProgramManager(self.currentUser, self.db)

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
                    all_exercises = programManager.get_all_exercises()
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
                case 3:
                    print("library exersice")
                    print("=== Library Exercises ===")
                    #get list of it
                    exercises, total_exercises, total_pages = programManager.get_all_exercises()
                    if exercises is None:
                        print("No data in the library")
                        return


                    # output using helpers.
                    output_exercises(exercises, total_exercises, total_pages)


                case 4:
                    print("try a random workout")
                case 0:
                    print("See you next time!")
                    return

