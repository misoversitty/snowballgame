from pygame.sprite import Group


class PlayerGroup(Group):
    def __init__(self, *args):
        super().__init__(*args)