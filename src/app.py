from utils.constants import *
from utils.helpers import *
class App:
    def __init__(self):
        self.currentUser = None
        #self.db = Database()  conneciton

    def run(self):
        print("hi")
        is_user = False
        if self.currentUser:
            is_user = self.currentUser

        if is_user:
            output_menu(menu_user)
            input = get_int_input(0, 4)
        else:
            output_menu(menu_no_user)
            input = get_int_input(0, 6)
