class UserManager:
    def __init__(self, user, db_manager):
        self.user = user
        self.db_manager = db_manager

    def register_user(self, username, email, password_hash):
        print("u got register user") #no problems
        #steps: 1. connect to the db 2. put there? no nee
        # 1. is user exists
        # 2. if not -> create
        if self.db_manager.is_user_exist(username, email) == 1:
            return 1 # 1 - the user exists

        pass
