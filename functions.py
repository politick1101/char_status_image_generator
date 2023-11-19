import os

from PIL import Image


def scale_image_up(image: Image.Image, scale: int) -> Image:
    """returns scaled image"""

    new_size = image.width * scale, image.height * scale
    new_image = image.resize(new_size)

    return new_image


if __name__ == '__main__':

    # preparing bigger versions of images

    source = 'resources_and_licenses/avatars/'
    result = 'images/avatars/'

    for filename in os.listdir(source):

        image = Image.open(source + filename)

        scaled_image = scale_image_up(image, 8)
        scaled_image.save(result + filename)
