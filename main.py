from PIL import Image, ImageDraw

from fonts import *

from functions import draw_text_with_shadow


def draw_image_tag(image: Image.Image, tag: str) -> Image.Image:
    draw_text_with_shadow(image, tag, 20, 40, width=10, font_size=50)
    # draw = ImageDraw.Draw(image)

    return image


avatar = Image.open("images/avatars/avito_link.png")
tag = 'AvitoLink2014'
status_image = draw_image_tag(avatar, tag)
status_image.show()
