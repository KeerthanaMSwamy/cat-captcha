#Author: Keerthana 
#Date: 2021-07-28
#reach out: keerthanamswamy@Gmail.com

#before you begin, install "pip install captcha"

from captcha.image import ImageCaptcha
import random

rand = random.randint(1000,9999)
cap = ImageCaptcha(width=100, height=100) # giving dimensions for the image
# cap = cap.generate_image('Keerthana') 
# cap = cap.create_captcha_image('Keerthana', color='white', background='black')#the words or numbers or alphanum you give inside the brackets will be converted to captcha

cap = cap.create_captcha_image(str(rand), color='white', background='black')
cap.show() #you will get a new file on your folder by .pyc extension