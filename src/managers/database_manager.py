from tkinter.messagebox import ERROR

from dotenv import load_dotenv
import bcrypt
import logging
import psycopg2
import os

from src.utils.constants import db_user_tuple
from src.utils.helpers import *


class DatabaseManager:
    logging.basicConfig(level=logging.ERROR)

    def __init__(self):
        load_dotenv()
        # or no need do it here
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.db = os.getenv("DB_NAME")
        self.port = os.getenv("DB_PORT")
        self.password = os.getenv("DB_PASSWORD")
        self.cursor = None
        self.db_con = self.get_connection()


    # connectino stuff
    def get_connection(self):
        try:
            self.db_con = psycopg2.connect(
                host=self.host,
                dbname=self.db,
                user=self.user,
                password=self.password,
                port=self.port)
            self.cursor = self.db_con.cursor() #use cursor to handle queries
        except Exception:
            logging.exception("Problem occurred: ")
        return self.db_con


    def close_connection(self):
        self.db_con.close() #


    # user stuff
    def is_user_exist(self, username, email):

        self.cursor.execute("SELECT * FROM users WHERE nickname = (%s) OR email = (%s)",
                                     (username, email))

        return self.cursor.fetchone()


    def create_user(self, user):
        try:
            self.cursor.execute("INSERT INTO users (nickname, email, password_hash, created_at) VALUES (%s, %s, %s, %s)",
                                     (user.nickname, user.email, user.password, user.created_at))
            self.db_con.commit()

            #get id
            user.id = self.get_info_from_db("users", "id", "email", user.email)
            return user
        except psycopg2.errors.NotNullViolation as NullError:
            print(f"Null Error happened {NullError}")
        except Exception:
            logging.exception("An error occurred: ")
        return None

    def auth_user(self, credentials, password):
        try:
            res = self.cursor.execute("SELECT * FROM users WHERE nickname = (%s) OR email = (%s)",
                                      (credentials, credentials))
            res = self.cursor.fetchone()

            if res is None:
                return None

            # res is a tuple. NO PROBLEMS
            password_from_db = res[db_user_tuple.get("password_hash")]

            if bcrypt.checkpw(password, bytes(password_from_db)):
                session = mapping_session_data(res)
                return session
        except Exception:
            logging.exception("An error occurred: ")
        return None


    #have to check
    def get_info_from_db(self, table_name, get_this, find_by, value):
        try:
            res = self.cursor.execute(f"SELECT {get_this} FROM {table_name} WHERE {find_by} = %s", (value,))
            return res
        except TypeError:
            print("the type error from the get_info_from_fb")
            logging.exception("More info: ")
        return None

    def update_data(self, user_id, new_data, column):
        try:
            self.cursor.execute("UPDATE users SET {column} = %s WHERE user_id = %s}",
                                (new_data, user_id))
            self.db_con.commit()
            return True
        except Exception:
            logging.exception("An error occurred")
            return False

    def delete_account(self, user_id):
        try:
            self.cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id))
            self.db_con.commit()
            return True
        except Exception:
            logging.exception("Some errors..")
            return None