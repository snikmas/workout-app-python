from http.client import responses
from src.utils.helpers import *
import requests
import json
from dotenv import load_dotenv
import os

class ProgramManager:
    # i guess no need for init etc. just functions? -> need to holding db connection
    def __init__(self, user, db_manager):
        load_dotenv() #it works forever?
        self.user = user
        self.db_manager = db_manager



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
            print(api_url + param)
            print(res.status_code)
            if res.status_code == 403:
                print(f"Oops, we can't open the library now.. Please, try later");
                return 403, None, None
            if res.status_code != 200:
                print(f"something is wrong, status code: {res.status_code}... back to the menu")

            res_data = res.json()
            #print(type(res_data))
            # OK ITS A DICT
            res_exercises = res_data.get("data")
            res_info = res_data.get("metadata")
            total_pages = res_info.get("totalPages")
            total_exercises = res_info.get("totalExercises")
            print(res_exercises)
            print(total_exercises)
            print(total_pages)
            # 3 returns.. is ok.
            return res_exercises, total_exercises, total_pages
        except TypeError:
            print("oops, TypeError")
        finally:
            return None, None, None