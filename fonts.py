from PIL import ImageFont


def tt_font(name: str, size: int)->ImageFont:
    """Wrapper over ImageFont.truetype"""
    return ImageFont.truetype(name, size)


# Initialising fonts
BETTER_VCR = "fonts/better-vcr5.1.ttf"
CS_MS_PIXEL = "fonts/Comic Sans MS Pixel.ttf"
PSY_FORCE_MONOSPACED = "fonts/PsychicForce2012Monospaced.otf"
