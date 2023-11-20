import os
from pathlib import Path

from PIL import Image


def scale_image_up(image: Image.Image, scale: int) -> Image:
    """returns scaled image"""

    new_size = image.width * scale, image.height * scale
    new_image = Image.new('RGB', new_size)

    pixels = image.load()
    new_pixels = new_image.load()

    for y in range(new_size[1]):
        for x in range(new_size[0]):
            new_pixels[x, y] = pixels[x // scale, y // scale]

    return new_image


def draw_text_with_shadow():
    pass
