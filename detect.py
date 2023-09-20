import pyautogui
import time
from PIL import Image, ImageDraw


def testSensor():
    #time.sleep(3)
        
    #pic = pyautogui.screenshot(region = (125,60,710,690))

    #pic.save('game.png')

    image = Image.open('game.png')

    width, height = image.size

    new_color = (255, 255, 255)

    for x in range(45,width,88):
        for y in range(25,height,80):
            r,g,b = image.getpixel((x,y))
            print("Pixel: ({},{},{})".format(r,g,b))
            draw = ImageDraw.Draw(image)
            draw.point((x, y), fill=new_color)

    image.save('game modified.png')



testSensor()