import logging
from dataclasses import dataclass

from PyQt5.QtSql import password

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

        session = self.db_manager.auth_user(credentials, password)
        token = create_token(session.user_id)
        session.token = token
        session.is_authorized = True
        # have to add token and is_auth

        return session # this is a session

    def auth_user(self, user_id, user_nickname):
        token = create_token(user_id)
        session = Session(user_id, user_nickname)
        session.token = token
        session.is_authorized = True
        self.session = session

    def verify_password(self, user_id, password):
        password = password.encode('utf-8')
        res = self.db_manager.auth_user(user_id, password)
        # will be none if nothing
        return res

    def change_user_data(self, user_id, new_data, data_type):
        # check is its data exists
        if data_type is not "password":
            res = self.db_manager.is_user_exist(new_data, new_data)
            if res:
                return f"This {data_type} exists"
        else:
            new_data = new_data.encode('utf-8')

        res = self.db_manager.update_data(user_id, new_data, data_type)
        if res is False:
            return "Error from the db"
        return True


    def delete_account(self, user_id):
        try:
            res = self.db_manager.delete_account(user_id)
        except Exception:
            logging.exception("Unexpected error...")
            return None
        return res
