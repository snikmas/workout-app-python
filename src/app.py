from src.managers.user_manager import UserManager
from utils.constants import *
from utils.helpers import *
from managers.program_manager import *
from managers.database_manager import *
from managers.session_manager import *

class App:
    def __init__(self):
        # self.currentUser = None no need
        self.session = None
        self.db = None
        self.user_manager = None
        self.database_manager = None
        self.program_manager = None
        self.session_manager = None
        # actually, no need for db.connection. this is db layer logic

    def run(self):
        self.database_manager = DatabaseManager()
        self.session_manager = SessionManager()
        self.program_manager = ProgramManager(self.session, self.database_manager)
        self.user_manager = UserManager(self.session, self.database_manager)

        print("hi")
        running = 1
        while running:
            if self.session:
                print(f"Welcome back, {self.session.nickname}!")
                output_menu(menu_user)
                input = get_int_input(0, 6)

                match input:
                    case 1:
                        print("start a new work session.py")
                    case 2:
                        print("my work programs")

                    case 3:
                        print("my progress history")
                    case 4:
                        print("=== Library Exercises ===")
                        all_exercises = self.program_manager.get_all_exercises()
                    case 5:
                        print("my accou settings")
                        print("=== Settings ===")
                        output_menu(menu_settings)
                        input = get_int_input(0, 4)

                        match(input):
                            case 1:
                                print("change a nickname")
                                print("Input your new nickname:")
                                nickname = get_str_input(50, None)
                                checkSession = self.session_manager.check_session(self.session)#?
                                print("Input ypur password again to update your nickname:")
                                password = get_str_input(100, "password")
                                # check_session() no need
                                # if everything is okay: "the nickckanem has been updated!" ?
                                # to change -> input your password again?
                            case 2:
                                print("change a email")
                            case 3:
                                print("change a password")
                            case 4:
                                print("change a delete a password")
                            case 0:
                                return
                    case 6:
                        self.session = None
                        print("You have been logged out.")
                    case 0:
                        self.database_manager.close_connection()
                        running = False

            else:
                output_menu(menu_no_user)
                input = get_int_input(0, 4)
                match input:
                    case 1:
                        logging_run = True
                        while logging_run:
                            print("Input your username/email: ")
                            credentials = get_str_input(50, None)
                            print("Input your password: ")
                            password = get_str_input(50, None)
                            res = self.user_manager.login_user(credentials, password)
                            if res:
                                self.session = res
                                print("Welcome back!")
                            else:
                                print("Incorrect username/email or password.")
                                # ask for a trying again or forgot password
                                output_menu(incorrect_credentials)
                                input = get_int_input(0, 2)

                                match(input):
                                    case 1:
                                        pass;
                                    case 2:
                                        self.forgot_password()
                                        print("Please, input your credentials again.")
                                        pass
                                    case 0:
                                        logging_run = False

                    case 2:
                        print("Nice to meet you!\nInput your username:")
                        username = get_str_input(30, None)
                        print("Input your email:")
                        email = get_str_input(50, None)
                        print("Input your password (8+ symbols; contains digits and special symbols):")
                        password = get_str_input(50, "password")


                        res = self.user_manager.register_user(username, email, password)
                        if res is None:
                            print("something wrong in create_user..")
                        else:
                            self.session = res

                        print("The Account Has Been Created!")

                    case 3:
                        print("library exersice")
                        print("=== Library Exercises ===")
                        #get list of it
                        exercises, total_exercises, total_pages = self.program_manager.get_all_exercises()
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
                        self.database_manager.close_connection()
                        running = 0

        print("See you next time!")
        return

    def forgot_password(self):
        #print("we got forgot apssword")
        print("Input your email:")
        user_email = get_str_input(None, None)

        pass