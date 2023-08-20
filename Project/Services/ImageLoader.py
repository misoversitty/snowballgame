import pathlib
import pygame

GAME_DIRECTORY = "D:\my shit\ProgProjects\snowballgame\Project"

def LoadImage(file: str):
    file = pathlib.Path(GAME_DIRECTORY, file)
    try:
        surface = pygame.image.load(file)
    except FileNotFoundError:
        raise SystemExit(f'Could not load image "{file}".')
    return surface


def RotateImage(img: pygame.image, degrees) -> pygame.image:
    try:
        res = pygame.transform.rotate(img, degrees)
    except pygame.error:
        raise SystemExit(f'Could not rotate image "{img}".')
    return res