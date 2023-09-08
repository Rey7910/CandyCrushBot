import mss
import time
from PIL import Image

# Acer Nitro 5 (Full Screen) Configuration - Rey

top=80
left=130
width=710
height=710

def screen_recognition():
    with mss.mss() as sct:
        monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)


def shoot_ss():
    
    with mss.mss() as sct:
        time.sleep(3)
        # The screen part to capture
        monitor = {"top": top, "left": left, "width": width, "height": height}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output='game image.png')
        print(output)


def identify_special_candy(r,g,b):

    
    print("({},{},{})".format(r,g,b))

    print("Special candy")


def identify_candy(r,g,b):
        #print("({},{},{})".format(r,g,b))

        if((r>=1450 and r<=2300) and (g>=5300 and g<=6700) and (b>=0 and b<=150)):
            print("Green found")
            #print("({},{},{})".format(r,g,b))
        elif(r>=6800 and g<=150 and b<=150):
            print("Red found")
            #print("({},{},{})".format(r,g,b))
        elif(r<=2300 and g>=4000 and g<=6000 and b>=8900):
            print("Blue found")
            #print("({},{},{})".format(r,g,b))
        elif(r>=8500 and r<9150 and g>=6300 and b<=3500):
            print("Yellow found")
            #print("({},{},{})".format(r,g,b))
        elif(r>=9000 and g>=4500 and b<=5500):
            print("Orange found")
            #print("({},{},{})".format(r,g,b))
        elif(r>=6000 and g<=3500 and b>=9170):
            print("Violet found")
            #print("({},{},{})".format(r,g,b))
        else:
            identify_special_candy(r,g,b)


def recognize_image():
    image = Image.open("game image.png")
    i=0
    j=0
    width, height = image.size
    print("this is the width: ",width)
    print("this is the height: ",height)

    modified_image = Image.new("RGB", (width, height))

    # walk throughout the matrix
    for y in range(35,height,80):
        for x in range(30,width,90):
            print("Matrix path [{}][{}]: ".format(i,j),end="")

            #pixels_array=[]
            r=0
            g=0
            b=0
            # catch the 6x6 area of pixels
            for k in range(-3,3,1):
                for l in range(-3,3,1):
                    pixel_color = image.getpixel((x+k, y+l))
                    r+=pixel_color[0]
                    g+=pixel_color[1]
                    b+=pixel_color[2]

                    image.putpixel((x + k, y + l), (255, 255, 255))
                    '''
                    
                    pixels_array.append(pixels_array)      '''  

            identify_candy(r,g,b)

        
            
            #identify_candy(pixels_array)            

            j+=1
        j=0
        i+=1

    image.save("modified_image.png")
    
    image.close()


recognize_image()
#shoot_ss()