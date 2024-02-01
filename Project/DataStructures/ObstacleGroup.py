from pygame.sprite import Group


class ObstacleGroup(Group):
    def __init__(self, *args):
        super().__init__(*args)