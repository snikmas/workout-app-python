import logging
from dataclasses import dataclass

from src.classes.session import Session
from src.utils.helpers import *
from src.classes.user import User
from datetime import datetime


class UserManager:
    logging.basicConfig(level=logging.ERROR)

    def __init__(self, session, db_manager):
        self.session = session
        self.db_manager = db_manager

    def register_user(self, nickname, email, password):
        if self.db_manager.is_user_exist(nickname, email) is not None:
            print("The user has already exist!")
            return

        password_hash = get_password_hash(password)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_user = User(nickname=nickname, password=password_hash, email=email, created_at=date, id=None)

        new_user = self.db_manager.create_user(new_user)
        #create a session and return it ! ! !

        # later maybe have to put to the another manager

        # call it after login or registr
        self.auth_user(new_user.id, new_user.nickname)
        print(self.session)

        return self.session

    def login_user(self, credentials, password):
        password = password.encode('utf-8')
        # get response and handle it to the user class
        res = self.db_manager.auth_user(credentials, password)
        return res # this is a session

    def auth_user(self, user_id, user_nickname):
        token = create_token(user_id)
        session = Session(user_id, user_nickname, token, True)
        self.session = session