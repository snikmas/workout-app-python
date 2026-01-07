import secrets
import os
import datetime
import jwt

import bcrypt
import requests
from dotenv import load_dotenv

from src.classes.session import Session
from src.utils.constants import *


# menu things
# output
def output_menu(menu):
    for menuItem in menu:
        print(menuItem)

def output_exercises(exercises, total_exercises, total_pages):
    print(f"Result: {total_exercises} exercises.")
    for page in range(0, total_pages):
        print(f"{page}/{total_pages} page:")
        # 10 exercises per page
        for exercise in range (page * 10, page * 10 + 10):
            print(exercise)
        print("just checking")
        return


#input
def get_int_input(min, max):
    user = input(">> ")
    while user.isdigit() == False or int(user) < min or int(user) > max:
        print("Invalid input, try again...")
        user = input(">> ")
    return int(user)

def get_str_input(limit, feature):
    user = input(">> ")
    match feature:
        case None:
            while user is None or len(user.strip()) < 3 or len(user.strip()) > limit or " " in user or not any(ch.isalpha() for ch in user):
                print("Invalid input, try again...")
                user = input(">> ")
        case "password": #requirements: has numbers/special symbosl
            while (user == None or len(user.strip()) < 8
                   or len(user.strip()) > limit
                   or not any(ch.isdigit() for ch in user)
                   or not any(ch.isalnum() for ch in user)):
                print("Invalid input, try agian...")
                user = input(">> ")
    return user.strip()

def get_yes_no():
    user = input(">> ")
    while user.upper() != 'Y' and user.upper() != 'N':
        print("invalid input, try again...")
        user = input(">> ")
    return user.strip()

def generate_secret():
    #try intialize or add text to the env -> save ti there
    new_secret = secrets.token_hex(32)

    # print(os.path.exists(".env"))
    if os.path.exists(".env"):
        with open(".env", "a") as f:
            # later have to check if its already exists DONT chagne
            f.write(f"JWT_SECRET_KEY={new_secret}\n")
            print("wroted")

#works
def get_secret():
    load_dotenv()
    key = os.getenv("JWT_SECRET_KEY")
    if key:
        return key
    else:
        print("SOme error... cant gind the secret (helpers")


# works
def create_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    secret_key = get_secret()
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token


# other small helper functions
#database
def get_password_hash(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)

def check_connection(api_url):
    return requests.get(api_url).status_code

# mappers
def mapping_session_data(res):
    nickname = res[db_user_tuple.get("nickname")]
    user_id = res[db_user_tuple.get("id")]
    # email = res[db_user_tuple.get("email")]
    # created_at = res[db_user_tuple.get("created_at")]
    # password_hash = res[db_user_tuple.get("password_hash")] # *** CHECK NOTES THIS THING
    return Session(nickname=nickname, user_id=user_id)