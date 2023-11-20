import os
from pathlib import Path

from PIL import Image


def scale_image_up(image: Image.Image, scale: int) -> Image:
    """returns scaled image"""

    new_size = image.width * scale, image.height * scale

    # todo: resize function is blurry now, rewrite for pixel-by-pixel crisp scaling
    new_image = image.resize(new_size, 5)

    return new_image
