#menu stuff

menu_no_user = [
    "1. Login",
    "2. Register",
    "3. Browse exercise library",
    "4. Try a random workout program",
    "0. Exit"]

menu_user = [
    "1. Start a new workout session.py",
    "2. My workout programs",
    "3. My progress & history",
    "4. Exercise Library",
    "5. My account settings",
    "6. Log Out",
    "0. Exit"]

menu_settings = [
    "1. Change My Nickname",
    "2. Change My Email",
    "3. Change My Password",
    "4. Delete My Account",
    "0. Exit"
    # etc
]




incorrect_credentials = [
    "1. Try again",
    "2. Forgot password",
    "0. Back to the menu"
]


# db stuff
db_user_tuple = {
    "id": 0,
    "nickname": 1,
    "email": 2,
    "password_hash": 3,
    "created_at": 4,
}

api_exercise_data = {
    "exerciseId": 0,
    "name": 1,
    "gif_url": 2,
    "target_muscles": 3,
    "body_parts": 4,
    "equipments": 5,
    "secondary_muscles": 6,
    "instructions": 7,
}