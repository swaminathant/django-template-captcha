from django.conf import settings
import os
from io import BytesIO
import string
from random import randint, choices
import base64
from PIL import Image, ImageDraw, ImageFont


def RandomCharacter(length):
    Char = choices(string.ascii_lowercase + string.digits, weights=None, k=length)
    return ''.join(Char)


def GenerateCaptcha(width=140, height=60, length=4):
    # generate verification code
    img = Image.new("RGB", (width, height), (250, 250, 250))
    draw = ImageDraw.Draw(img)
    FontLocation = os.path.join(settings.BASE_DIR, "telenor", "static", "fonts", "Roboto-Black.ttf")
    font = ImageFont.truetype(FontLocation, size=36)
    CaptchaText = RandomCharacter(length)
    #  captcha text
    for i in range(length):
        RGB = (randint(10, 150), randint(10, 150), randint(10, 150))
        Char = CaptchaText[i]
        rand_len = randint(-1,1)
        draw.text((width * 0.2 * (i + 0.5) + rand_len, height * 0.1 + rand_len), Char, font=font,  fill=RGB)

    # Draw line inside the image.
    for i in range(4):
        RGB = (randint(10, 150), randint(10, 150), randint(10, 150))
        x1, y1, x2, y2 = randint(0, width), randint(0, height), randint(0, width), randint(0, height)
        draw.line((x1, y1, x2, y2), fill=RGB)

    # Create byteio object to store the image.
    buffered = BytesIO()
    # This is to save the img to buffer image
    img.save(buffered, format="PNG")
    # Return the image as base64
    ImgBase64 = base64.b64encode(buffered.getvalue())
    ImgBase64 = str(ImgBase64, 'utf-8')
    return ImgBase64, CaptchaText
