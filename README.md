# django-template-captcha
Using this you can implement the captcha with django template.

Required PIL package.

# pip installation method
pip install Pillow

#Example code for calling the captcha image generator function
from . import CaptchaImageGenerator
def ():
    # Call the captcha customs module.
    Base64Data, text = CaptchaImageGenerator.GenerateCaptcha()
    Data = {"CaptchaImage": Base64Data}
    return Data, text

By adding this to session you can send that base64 image content to frontend and validate the session.
