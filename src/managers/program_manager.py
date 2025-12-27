import requests

class ProgramManager:
    # i guess no need for init etc. just functions? -> need to holding db connection
    def __init__(self, user, db_connection):
        self.user = user
        self.db_connection = db_connection


    def get_all_exercises(self):
        # call to the api and return
        return