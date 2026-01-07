from secrets import token_bytes


class Session:
    def __init__(self, user_id, nickname):
        self.user_id = user_id
        self.nickname = nickname
        self.token = None
        self.is_authorized = None
    pass