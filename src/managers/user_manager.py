from dataclasses import dataclass
from src.classes.user import User
from datetime import datetime

class UserManager:
    def __init__(self, user, db_manager):
        self.user = user
        self.db_manager = db_manager

    def register_user(self, nickname, email, password_hash):
        print("u got register user") #no problems
        #steps: 1. connect to the db 2. put there? no nee
        # 1. is user exists
        # 2. if not -> create
        if self.db_manager.is_user_exist(nickname, email) is not None:
            print("The user has already exist!")
            return  # 1 - the user exists

        # it should return.. full user with created_at? or maybe just create another one
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        new_user = User(nickname=nickname, password=password_hash, email=email, created_at=date)
        res = self.db_manager.create_user(new_user)
        return res
