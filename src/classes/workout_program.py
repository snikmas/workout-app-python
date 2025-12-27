class workout_program:
    # name; msucles ? description; is favorite? authors?
    def __init__(self, title, description, target_muscles, author, created_at, difficulty, exercises_set):
        self.title = title
        self.description = description
        self.target_muscles = target_muscles
        self.author = author
        self.created_at = created_at
        self.difficulty = difficulty
        self.exercises_set = exercises_set # exersice set.. a dictionary withs sets reps
        # in database: workout title description target uscles created and difficulty. other stuff can.. links?