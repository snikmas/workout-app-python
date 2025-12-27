import json
import requests
import re

def output_menu(menu):
    for menuItem in menu:
        print(menuItem)

def get_int_input(min, max):
    user = input(">> ")
    while user.isdigit() == False or int(user) < min or int(user) > max:
        print("Invalid input, try again...")
        user = input(">> ")
    return int(user)

def get_str_input(limit, feature):
    user = input(">> ")
    match(feature):
        case None:
            while user == None or len(user.strip()) < 3 or len(user.strip()) > limit or " " in user or not any(ch.isalpha() for ch in user):
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


def output_exercises(exercises, total_exercises, total_pages):
    print(f"Result: {total_exercises} exercises.")
    for page in range(0, total_pages):
        print(f"{page}/{total_pages} page:")
        # 10 exercises per page
        for exercise in range (page * 10, page * 10 + 10):
            print(exercise)
        print("just checking")
        return

