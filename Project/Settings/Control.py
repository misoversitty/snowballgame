class Control:
    def __init__(self, k_up: str, k_down: str, k_left: str, k_right: str):
        self.assignment = {
            k_up: "Up",
            k_down: "Down",
            k_left: "Left",
            k_right: "Right"
        }