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

    def check_updates(self):
        amount_db_exercises = self.db_manager.amount_exercises()
        amount_api_exercises = self.api_manager.amount_exercises()

        # late have to check parameter IF ONLY DB DOENST HAVE or just doesnt have a few ones
        if amount_db_exercises is None:
            all_exercises = self.api_manager.get_all_exercise_data() #list
            print(all_exercises)
            for data in all_exercises:
                exercise = mapping_exercise_data(data)
                if exercise is not None:
                    #addig to the db+ check again if its exiss
                    if self.db_manager.is_exercise_exist(exercise.id) is True:
                        #do nothing, its exists
                        continue
                    else:
                        res = self.db_manager.add_exercise_data(exercise)
                        if res is not True:
                            print(f"some error duirng adding {exercise.id}...")


            # have to parse dict
            return
            # self.db_manager.update_exercise_data(all_exercises)
        elif  amount_db_exercises < amount_api_exercises:
            pass
        else:
            logging.exception("Unexpected result, program manager check updates")

        # gen amount from the api. next if amount db = none or is les..
        print(amount_db_exercises)


    def get_all_exercises(self):

        self.check_updates()
        # 1/ compare count exersices from the api and from our db