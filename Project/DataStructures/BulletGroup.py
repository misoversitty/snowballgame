from pygame.sprite import Group


class BulletGroup(Group):
    def __init__(self, *args):
        super().__init__(*args)