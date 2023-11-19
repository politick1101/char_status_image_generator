from PIL import Image, ImageDraw

from fonts import *

image = Image.open("images/avatars/avito_link.png")

draw = ImageDraw.Draw(image)

draw.text((10, 10), "AvitoLink2015", font=CS_MS_PIXEL_font, fill=(0, 0, 0))

image.show()
