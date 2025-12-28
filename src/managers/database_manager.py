import traceback
import psycopg2
from dotenv import load_dotenv
import os

from src.classes.user import User


class DatabaseManager:

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
        except:
            print("problem with conneciton")
        return self.db_con


    def close_connection(self):
        pass #here later have to close connecitno


    # user stuff
    def is_user_exist(self, username, email):
        # no need, it runs first
        #if self.db_con is None:
        #    self.db_con = self.get_connection()
        #    if self.db_con is None:
        #        print("Can't connect to the db. Back to the menu...")
        #        return

        result = self.cursor.execute("SELECT * FROM users WHERE nickname = (%s) OR email = (%s)",
                                     (username, email))
        return result

    # retunrs
    def create_user(self, user):
        # print(User.print_info(user)) just check data
        try:
            self.cursor.execute("INSERT INTO users (nickname, email, password_hash, created_at) VALUES (%s, %s, %s, %s)",
                                     (user.nickname, user.email, user.password, user.created_at))
            self.db_con.commit()
            #user.created_at = self.get_data("users", "email", user.email, "created_at")
            return 0
        except psycopg2.errors.NotNullViolation as NullError:
            print(f"Null Error happened {NullError}")
        except Exception:
            print(f"the error during creating a user {Exception}")
        return 1
