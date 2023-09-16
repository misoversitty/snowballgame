from Project.Dependencies import *
import pygame



class ImageLoader:
    @staticmethod
    def LoadImage(file: str):
        file = Path(RESOURCES_DIRECTORY, file)
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