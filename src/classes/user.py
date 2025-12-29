class User:
    def __init__(self, nickname, password, email, created_at, id):
        self.nickname = nickname #username is login
        self.password = password
        self.email = email
        self.created_at = created_at
        self.id = id

    @staticmethod
    def print_info(user):
        return (f"Username: {user.nickname}\n"
                f"Password: {user.password}\n"
                f"Email: {user.email}"
                f"Created_at: {user.created_at}")