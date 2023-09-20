from Project.Globals import RESOURCES_DIRECTORY
from pathlib import Path
import pygame



class ImageLoader:
    @staticmethod
    def loadImage(file: str):
        file = Path(RESOURCES_DIRECTORY, file)
        try:
            surface = pygame.image.load(file)
        except FileNotFoundError:
            raise SystemExit(f'Could not load image "{file}".')
        return surface


    @staticmethod
    def rotateImage(img: pygame.image, degrees) -> pygame.image:
        try:
            res = pygame.transform.rotate(img, degrees)
        except pygame.error:
            raise SystemExit(f'Could not rotate image "{img}".')
        return res