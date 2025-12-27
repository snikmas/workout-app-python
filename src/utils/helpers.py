import json
import requests

def output_menu(menu):
    for menuItem in menu:
        print(menuItem)

def get_int_input(min, max):
    user = input()
    while user.isdigit() == False or int(user) < min or int(user) > max:
        print("Invalid input, try again...")
        user = input()
    return int(user)

def check_connection(api_url):
    return requests.get(api_url).status_code

def handle_json(json_result):
    return json.loads(json_result)