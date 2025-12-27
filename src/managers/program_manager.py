from http.client import responses
from src.utils.helpers import *
import requests
import json
from dotenv import load_dotenv
import os

class ProgramManager:
    # i guess no need for init etc. just functions? -> need to holding db connection
    def __init__(self, user, db_connection):
        load_dotenv() #it works forever?
        self.user = user
        self.db_connection = db_connection



    def get_all_exercises(self):

        api_url = os.getenv("API_URL") #maybe put to the up? like we use only this url

        #actually, for a server part we can put to the another functions
        try:
            #check connection with the server (does it okay?) or no need, just call thing
            if check_connection(api_url) == 500:
                print("no response from the server... back to the menu\n")
                return

            param = "/api/v1/exercises"
            # print(api_url + param)
            res = requests.get(api_url + param)
            if res.status_code == 500:
                print("something is wrong... back to the menu")
                return

            res_data = res.json()
            #print(type(res_data))
            # OK ITS A DICT
            exercises = res_data.get("data")
            return exercises

            # we also can return it, but idk, i think
            # res_info = res_data.get("metadata")
            # total_pages = res_info.get("totalPages")
            # total_exercises = res_info.get("totalExercises")

        except:
            print("oops, something wrong")



        # call to the api and return
        #
        return
