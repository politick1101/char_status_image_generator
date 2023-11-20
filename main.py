from PIL import Image, ImageDraw

from fonts import *


def draw_image_tag(image: Image.Image, tag: str) -> Image.Image:
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), tag, font=CS_MS_PIXEL_font, fill=(0, 0, 0))
    return image

avatar = Image.open("images/avatars/avito_link.png")
tag = 'AvitoLink2014'
status_image = draw_image_tag(avatar, tag)
status_image.show()