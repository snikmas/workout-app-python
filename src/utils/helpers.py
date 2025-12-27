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

def output_exercises(exercises, total_exercises, total_pages):

    print(f"Result: {total_exercises} exercises.")
    for page in range(0, total_pages):
        print(f"{page}/{total_pages} page:")
        # 10 exercises per page
        for exercise in range (page * 10, page * 10 + 10):
            print(exercise)
        print("just checking")
        return
