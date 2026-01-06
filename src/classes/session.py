from secrets import token_bytes


class Session:
    def __init__(self, user_id, nickname, token, is_authorized):
        self.user_id = user_id
        self.nickname = nickname
        self.token = token
        self.is_authorized = is_authorized
    pass