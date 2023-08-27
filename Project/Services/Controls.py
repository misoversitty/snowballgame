class Controls:
    def __init__(self, k_up: str, k_down: str, k_left: str, k_right: str):
        self.assignment = {
            k_up: "MoveUp",
            k_down: "MoveDown",
            k_left: "MoveLeft",
            k_right: "MoveRight"
        }