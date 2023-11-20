import os

from PIL import Image

from functions import scale_image_up

# Preparing bigger versions of images.
source = 'avatars/'
result = '../images/avatars/'

for filename in os.listdir(source):
    image = Image.open(source + filename)

    scaled_image = scale_image_up(image, 8)
    scaled_image.save(result + filename)

# # crop out food icon
# width, height = 16, 16
# row_index, col_index = 1, 14
#
# box = (col_index * width, row_index * height,
# (col_index + 1) * width, (row_index + 1) * height)
#
# scale_image_up(Image.open('resources_and_licenses/Fruit+.png').crop(box), 8).save('images/food_icon.png')