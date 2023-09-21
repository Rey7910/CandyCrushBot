import pyautogui
import time
from PIL import Image, ImageDraw


board_matrix = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

def reportUnknownCandy(y,x,r,g,b):
    print("Candy[{}][{}] with({},{},{})".format(y,x,r,g,b))

def reportCandy(y,x,candy):
    print("Candy[{}][{}]: {}".format(y,x,candy))


def printMatrix(matrix):

    for i in range(9):
        for j in range(9):
            print(matrix[i][j],end=" ")
        print()



def identifyPackedCandy(r,g,b):
    if (r in range(80,150) and g in range(120,220) and b in range(50,130)):
        return 24 # green packed candy
    
    elif(r in range(100,250) and g in range(70,150) and b in range(210,260)):
        return 23 # violet packed candy
    
    elif(r in range(230,280) and g in range(150,250) and b in range(0,130)):
        print("my: ",r,g,b)
        return 25 # orange packed candy

    elif(r in range(160,350) and g in range(100,250) and b in range(0,150)):
        print("my: ",r,g,b)
        return 20 # orange packed candy
    
    else:
        print(r,g,b)
        return 100


def identifyCandy(r,g,b):

    '''elif( r in range(1100,1276) and g in range(1000,1200) and b in range(700,1000)):
        return 10 # "special orange" '''


    if(r in range(300,1000) and g in range(100,700) and b in range(30,400)):
        return 66 # "chocolate"

    elif( (r in range(1200,1276) and g in range(1000,1090) and b in range(130,200)) or (r in range(1200,1276) and g in range(1000,1200) and b in range(380,500))):
        return 15 # "special yellow"
    
    elif( (r in range(780,850) and g in range(1100,1276) and b in range(550,650)) or (r in range(380,500) and g in range(1100,1276) and b in range(180,280))):
        return 14 # "special green"
    
    elif( (r in range(1200,1276) and g in range(650,750) and b in range(600,710)) or (r in range(1100,1250) and g in range(200,420) and b in range(160,420))):
        return 12 # "special red"

    elif( r in range(400,830) and g in range(940,1200) and b in range(1130,1260)):

        return 11 # "special blue"   
    
    elif( (r in range(400,700) and g in range(800,1100) and b in range(1000,1276)) or (r in range(1200,1270) and g in range(800,1140) and b in range(200,860))):
        print(r,g,b)
        return 10 #"special orange"
    
    elif( r in range(900,1200) and g in range(90,290) and b in range(1270,1276)):
        return 3 #"violet"

    elif( r in range(900,1100) and g in range(250,400) and b in range(1200,1276)):
        return 13 #"special violet"
    
    elif( r in range(1220,1276) and g in range(900,1270) and b in range(0,270)):
        return 5 # "yellow"
    
    elif( r in range(1000,1276) and g in range(0,30) and b in range(0,10)):
        return 2 #"red"
    
    elif( r in range(200,280) and g in range(770,920) and b in range(0,10)):
        return 4 #"green"
    
    elif( r in range(1270,1276) and g in range(700,910) and b in range(50,400)):
        return 0 #"orange"
    
    elif( r in range(100,255) and g in range(540,800) and b in range(1200,1276)):
        return 1 #"blue"
    
    else:
        return 100 #"no match"



def testSensor():
        
    pic = pyautogui.screenshot(region = (125,60,790,690))

    pic.save('game1.png')

    image = Image.open('game1.png')

    width, height = image.size


    new_color = (255, 255, 255)

    draw = ImageDraw.Draw(image)

    counter_x=0
    counter_y=0
    total_r=0
    total_g=0
    total_b=0

    for x in range(45,width,88):
        
        for y in range(25,height,80):
            
            if((counter_y==6 and counter_x==2)):
                new_color=(0,0,0)

            else:
                new_color=(255,255,255)

            #print("Pixel: ({},{},{})".format(r,g,b))
            r,g,b = image.getpixel((x-30,y-24))
            draw.point((x-30, y-24), fill=new_color)

            #print("r g b -> ({},{},{})".format(r,g,b))

            if(not(r in range(35,105) and g in range(60,130) and b in range(65,140)) and r+g+b>=200):
                candy = identifyPackedCandy(r,g,b)
                print("packed candy")
                board_matrix[counter_y][counter_x]=candy
                counter_y+=1
                total_r=0
                total_g=0
                total_b=0
                continue


            r,g,b = image.getpixel((x,y))
            total_b+=b
            total_r+=r
            total_g+=g
            #print("Pixel: ({},{},{})".format(r,g,b))
            draw.point((x, y), fill=new_color)

            
            r,g,b = image.getpixel((x,y+5))
            total_b+=b
            total_r+=r
            total_g+=g
            #print("Pixel: ({},{},{})".format(r,g,b))
            draw.point((x, y+5), fill=new_color)

            
            r,g,b = image.getpixel((x,y-5))
            total_b+=b
            total_r+=r
            total_g+=g
            #print("Pixel: ({},{},{})".format(r,g,b))
            draw.point((x, y-5), fill=new_color)
            
            r,g,b = image.getpixel((x+5,y))
            total_b+=b
            total_r+=r
            total_g+=g
            #print("Pixel: ({},{},{})".format(r,g,b))
            draw.point((x+5, y), fill=new_color)
            
            r,g,b = image.getpixel((x-5,y))
            draw.point((x-5, y), fill=new_color)
            total_b+=b
            total_r+=r
            total_g+=g
            #print("Pixel: ({},{},{})".format(r,g,b))

            
            candy = identifyCandy(total_r,total_g,total_b)

            
            #print("Candy[{}][{}] with({},{},{})".format(counter_y,counter_x,total_r,total_g,total_b))
            
            if(candy==100):
                reportUnknownCandy(counter_y,counter_x,total_r,total_g,total_b)
            
            else:
                reportCandy(counter_y,counter_x,candy) 


            board_matrix[counter_y][counter_x]=candy


            counter_y+=1
            total_r=0
            total_g=0
            total_b=0


        counter_y=0
        counter_x+=1
        


    image.save('game1 modified.png')
    
    printMatrix(board_matrix)
    print("-----------------------")





testSensor()
#Sensor()

