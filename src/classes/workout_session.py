class Workout_session:
    def __init__(self, workout_id, date, feeling, notes):
        self.workout_id = workout_id #links
        self.date = date
        self.feeling = feeling
        self.notes = notes
        # in the db: date feeling notes and id workout session. create