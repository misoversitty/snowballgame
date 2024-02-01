class Control:
    def __init__(self, *args, **kwargs):
        self.assignment = {}

    def set(self, key: str, action: str):
        self.assignment[key.lower()] = action