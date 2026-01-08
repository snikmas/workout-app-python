from src.managers.api_manager import ApiManager
from src.managers.user_manager import UserManager
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
        self.api_manager = None
        # actually, no need for db.connection. this is db layer logic

    def run(self):
        self.database_manager = DatabaseManager()
        self.session_manager = SessionManager()
        self.api_manager = ApiManager()
        self.program_manager = ProgramManager(self.session, self.database_manager, self.api_managerg)
        self.user_manager = UserManager(self.session, self.database_manager)
        generate_secret()

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
                        all_exercises =  self.program_manager.get_all_exercises()

                    case 5:
                        print("=== Settings ===")
                        output_menu(menu_settings)
                        input = get_int_input(0, 4)
                        print("Input your password again to make changes")
                        password = get_str_input(50, None)
                        res = self.user_manager.verify_password(self.session.user_id, password)
                        if res is None:
                            print("Wrong password. Back to menu...")

                        match input:
                            case 1:
                                print("Input your new nickname:")
                                nickname = get_str_input(50, None)
                                res = self.user_manager.change_user_data(self.session.user_id, nickname, "nickname")
                                if res is not True:
                                    print(res)
                                    print("Back to menu...")
                                    return
                                self.session.nickname = nickname
                                print("The data updated")
                            case 2:
                                print("Input your new email:")
                                email = get_str_input(50, None)
                                res = self.user_manager.change_user_data(self.session.user_id, email, "email")
                                if res is not True:
                                    print(res)
                                    print("Back to menu...")
                                    return
                                print("The data updated")
                            case 3:
                                print("Input your password (8+ symbols; contains digits and special symbols):")
                                password = get_str_input(50, "password")
                                res = self.user_manager.change_user_data(self.session.user_id, password,
                                                                         "password")
                                if res is not True:
                                    print(res)
                                    print("Back to menu...")
                                    return
                                print("The data updated")
                            case 4:
                                print("Are you really want to delete your account? [Y/N]")
                                user = get_yes_no()
                                if user.upper() == 'Y':
                                    res = self.user_manager.delete_account(self.session.user_id)
                                    if user is None:
                                        print("Sometihng wrong...")
                                        return
                                    print("Your profile has been deleted. Bye")
                                    self.session = None
                                    return

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
                                # res is a session
                                self.session = res
                                print("Welcome back!")
                                break # maybe
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


                        # create
                        res = self.user_manager.register_user(username, email, password)
                        if res is None:
                            print("something wrong in create_user..")
                        else:
                            self.session = res
                            print(self.session)
                        #no problems
                        print("The Account Has Been Created!")

                    case 3:
                        print("library exersice")
                        print("=== Library Exercises ===")
                        all_exercises =  self.program_manager.get_all_exercises()


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