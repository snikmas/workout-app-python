from http.client import responses
from src.utils.helpers import *
import requests
import json
from dotenv import load_dotenv
import os
import logging

class ProgramManager:
    logging.basicConfig(level=logging.ERROR)
    # i guess no need for init etc. just functions? -> need to holding db connection
    api_url = os.getenv("API_URL")

    def __init__(self, session, db_manager, api_manager):
        load_dotenv() #it works forever?
        self.session= session
        self.db_manager = db_manager
        self.api_manager = api_manager

    # change this thing: one call to api and db
    def sync_exercises(self):

        all_api_exercises_data = self.api_manager.amount_exercises()

        amount_db_exercises = self.db_manager.get_all_exercise_data()
        amount_api_exercises = all_api_exercises_data.res.get("metadata").get("totalExercises")

        if amount_db_exercises is None or amount_api_exercises > amount_db_exercises:
            all_exercises = all_api_exercises_data.get("data") #list
            if all_exercises is None:
                print("Some problems with a server... Waiting")
                return
            for data in all_exercises:
                exercise = mapping_exercise_data(data)
                # if exercise is not None: # ADD IF DOENST EXIDST
                #     if self.db_manager.is_exercise_exist(exercise.id) is True:
                #         do nothing, its exists
                        # continue
                res = self.db_manager.add_exercise_data(exercise)
                if res is not True:
                    print(f"some error duirng adding {exercise.id}...")
        else:
            logging.exception("Unexpected result, program manager check updates")
            return False
        return "The data has been synchronized."


    def get_all_exercises(self):

        res = self.sync_exercises()
        if res is False:
            print("Some errors during sync...")
            return
        print(res)

        # connect to db and get all data
        # 1/ compare count exersices from the api and from our db