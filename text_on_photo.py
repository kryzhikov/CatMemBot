
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import random, os
def get_mem(text):
    path = "./downloads/ kitten/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    try:
        img = Image.open(path+ random_filename)
    except:
        get_mem(text)
    draw = ImageDraw.Draw(img)
    fz = 90
    font = ImageFont.truetype("arial_bold_italic.ttf", fz)

    text_w, text_h = draw.textsize(text, font)
    w, h = img.size
    while (text_w > w - 40):
        fz -= 1
        font = ImageFont.truetype("arial_bold_italic.ttf", fz)
        text_w, text_h = draw.textsize(text, font)
    draw.text(((w - text_w) // 2, h - text_h - 30),text,(255,255,255),font=font)
    print(fz)
    try:
        img.save('sample-out.jpg')
    except:
        get_mem(text)
