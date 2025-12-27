import psycopg2
from dotenv import load_dotenv
import os

class DatabaseManager:


    def __init__(self):
        self.db_con = None
        load_dotenv()
        # or no need do it here
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.db = os.getenv("DB_NAME")
        self.port = os.getenv("DB_PORT")
        self.password = os.getenv("DB_PASSWORD")


    def get_connection(self):
        db_con = psycopg2.connect(
            host=self.host,
            dbname=self.db,
            user=self.user,
            password=self.password,
            port=self.port)
        return db_con

    def is_user_exist(self, username, email):
        if self.db_con is None:
            self.db_con = self.get_connection()
            if self.db_con is None:
                print("Can't connect to the db. Back to the menu...")
                return

        print("connected")
