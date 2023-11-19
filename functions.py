import os
from pathlib import Path

from PIL import Image


def scale_image_up(image: Image.Image, scale: int) -> Image:
    """returns scaled image"""

    new_size = image.width * scale, image.height * scale
    new_image = image.resize(new_size)

    return new_image


if __name__ == '__main__':
    # # preparing bigger versions of images
    # source = 'resources_and_licenses/avatars/'
    # result = 'images/avatars/'
    #
    # for filename in os.listdir(source):
    #     image = Image.open(source + filename)
    #
    #     scaled_image = scale_image_up(image, 8)
    #     scaled_image.save(result + filename)

    # # crop out food icon
    # width, height = 16, 16
    # row_index, col_index = 1, 14
    #
    # box = (col_index * width, row_index * height,
    #        (col_index + 1) * width, (row_index + 1) * height)
    #
    # Image.open('resources_and_licenses/Fruit+.png').crop(box).save('images/food_icon.png')

    pass