from pathlib import Path
from pygame import image, transform

from Project.Globals import RESOURCES_DIRECTORY


class ImageLoader:
    @staticmethod
    def loadImage(file: str):
        file = Path(RESOURCES_DIRECTORY, file)
        try:
            surface = image.load(file)
        except FileNotFoundError:
            raise SystemExit(f'Could not load image "{file}".')
        return surface


    @staticmethod
    def rotateImage(img: image, degrees) -> image:
        try:
            res = transform.rotate(img, degrees)
        except Exception:
            raise SystemExit(f'Could not rotate image "{img}".')
        return res
