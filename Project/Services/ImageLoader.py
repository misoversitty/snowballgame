import pathlib
import pygame

GAME_DIRECTORY = pathlib.Path.cwd()  # "D:\my shit\ProgProjects\snowballgame\Project"


class ImageLoader:
    @staticmethod
    def LoadImage(file: str):
        file = pathlib.Path(GAME_DIRECTORY, file)
        try:
            surface = pygame.image.load(file)
        except FileNotFoundError:
            raise SystemExit(f'Could not load image "{file}".')
        return surface


    @staticmethod
    def RotateImage(img: pygame.image, degrees) -> pygame.image:
        try:
            res = pygame.transform.rotate(img, degrees)
        except pygame.error:
            raise SystemExit(f'Could not rotate image "{img}".')
        return res