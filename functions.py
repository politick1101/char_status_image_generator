import os
from pathlib import Path

from PIL import Image


def scale_image_up(image: Image.Image, scale: int) -> Image:
    """returns scaled image"""

    new_size = image.width * scale, image.height * scale

    # todo: resize function is blurry now, rewrite for pixel-by-pixel crisp scaling
    new_image = image.resize(new_size, 5)

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

    # crop out food icon
    width, height = 16, 16
    row_index, col_index = 1, 14

    box = (col_index * width, row_index * height,
           (col_index + 1) * width, (row_index + 1) * height)

    scale_image_up(Image.open('resources_and_licenses/Fruit+.png').crop(box), 8).save('images/food_icon.png')

    pass
