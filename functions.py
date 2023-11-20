import os
from math import sin, cos
from pathlib import Path

from PIL import Image, ImageDraw

from fonts import *


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


def draw_text_with_shadow(image: Image.Image, text: str, x: int, y: int,
                          width: int = 1, font=CS_MS_PIXEL, font_size=25,
                          away_steps=6, radial_steps=60) -> Image.Image:
    """
    away_steps and radial_steps are accuracy of shadow,
    the bigger the numbers,
    the better result,
    the less - the faster
    """

    draw = ImageDraw.Draw(image)
    font = tt_font(font, font_size)

    for j in range(away_steps):
        for i in range(radial_steps):
            dx = cos(i * 360 / radial_steps) * (width / away_steps * j)
            dy = sin(i * 360 / radial_steps) * (width / away_steps * j)
            draw.text((x + dx, y + dy), text, font=font, fill=(255, 255, 255))

    draw.text((x, y), text, font=font, fill=(0, 0, 0))
    return image
