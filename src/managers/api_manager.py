import logging
import os
from sqlite3.dbapi2 import apilevel
import requests
from dotenv import load_dotenv


class ApiManager:
    logging.basicConfig(level=logging.ERROR)
    load_dotenv()
    def __init__(self):
        self.api_url = os.getenv('API_URL')

    def get_all_exercise_data(self):
        link = '/api/v1/exercises'  # later can put to the constns
        res = requests.get(self.api_url + link)
        print(res.status_code)
        if res.status_code == 200:
            res = res.json()
            # totalExercises = res.get("data")
            # parse ? no here
            return res
        else:
            print("Can't get data from the api...")
            print(res.status_code)
            return
