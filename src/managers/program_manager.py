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

        all_api_exercises_data = self.api_manager.get_all_exercise_data()
        all_db_exercises = self.db_manager.get_all_exercise_data()

        amount_api_exercises = all_api_exercises_data.get("metadata").get("totalExercises")
        amount_db_exercises = len(all_db_exercises)

        if amount_db_exercises is None or amount_api_exercises > amount_db_exercises:
            all_exercises = all_api_exercises_data.get("data") #list
            if all_exercises is None:
                # didnt sycned but can run
                logging.exception("all_exercises from the program manager in None")
                print("Some errors occurred. The data hasn't been synchronized. Please try again later.")
                return

            list_data = [exercise for data in all_exercises if (exercise := mapping_exercise_data(data))
                         is True or not logging.exception(f"Some error during adding {exercise.id}...")]

            exercise_data = [(exercise.id, exercise.name, exercise.target_muscles,
                              exercise.body_parts, exercise.secondary_muscles,
                              exercise.instructions, exercise.gif_url) for exercise in list_data]

            self.db_manager.add_exercise_data(exercise_data)

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