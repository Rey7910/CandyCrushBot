import pyautogui
import time
from PIL import Image, ImageDraw
import boardSolver
import fastActuator

restartSensor=0
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
    global restartSensor
    if (r in range(220,256) and g in range(70,100) and b in range(70,100)):
        print("my: ",r,g,b)
        return 22 # red packed candy
    elif (r in range(80,150) and g in range(120,220) and b in range(50,130)):
        print("my: ",r,g,b)
        return 25 # green packed candy
    
    elif(r in range(100,250) and g in range(70,150) and b in range(210,260)):
        print("my: ",r,g,b)
        return 23 # violet packed candy
    
    elif(r in range(230,280) and g in range(150,250) and b in range(90,130)):
        print("my: ",r,g,b)
        return 24 # yellow packed candy
    elif(r in range(160,350) and g in range(100,250) and b in range(0,150)):
        print("my: ",r,g,b)
        return 20 # orange packed candy

    elif(r in range(20,120) and g in range(100,270) and b in range(150,300)):
        print("my: ",r,g,b)
        return 21 # blue packed candy

    else:
        restartSensor+=1
        return 100
agent = boardSolver.BoardSolver()
def identifyCandy(pixels):
    for i in pixels:
        if(i[0] in range(30,66) and i[1] in range(159,196) and i[2] in range(0,20)):
            return 5 # green
        elif(i[0] in range(240,256) and i[1] in range(110,160) and i[2] in range(0,20)):
            return 0 # orange
        
        elif(i[0] in range(5,50) and i[1] in range(120,270) and i[2] in range(220,256)):
            
            return 1 #blue
        
        elif(i[0] in range(200,256) and i[1] in range(200,255) and i[2] in range(0,20)):
            return 4 # yellow
        
        elif(i[0] in range(240,256) and i[1] in range(0,20) and i[2] in range(0,20)):
            return 2 # red
        
        elif(i[0] in range(160,230) and i[1] in range(15,80) and i[2] in range(230,256)):
            return 3 # violet
        
        
    
    return 8
def sensorLoop():
    counter=0
    counter_rep=0
    last_movement_x = 0
    last_movement_y = 0
    while(counter<=10):
        counter+=1
        pic = pyautogui.screenshot(region = (125,60,790,690))

        pic.save('game1.png')
        image = Image.open('game1.png')
        width, height = image.size
        global restartSensor
        new_color = (255, 255, 255)
        draw = ImageDraw.Draw(image)
        counter_x=0
        counter_y=0
        
        flag = False
        for x in range(45,width,88):
            
            for y in range(25,height,80):
                
                flag = False
                pixels = []
                #print("Pixel: ({},{},{})".format(r,g,b))
                r,g,b = image.getpixel((x-30,y-24))
                draw.point((x-30, y-24), fill=new_color)
                #print("r g b -> ({},{},{})".format(r,g,b))
                '''
                if(not(r in range(35,105) and g in range(60,130) and b in range(65,140)) and r+g+b>=220):
                    candy = identifyPackedCandy(r,g,b)
                    print("packed candy")
                    board_matrix[counter_y][counter_x]=candy
                    counter_y+=1
                    continue '''
                
                #print("{},{}".format(counter_y,counter_x))
                r,g,b = image.getpixel((x,y))
                #print("Pixel center: ({},{},{})".format(r,g,b))
                draw.point((x, y), fill=new_color)
                pixels.append((r,g,b))
                ############################################ EDGE
                r,g,b = image.getpixel((x+10,y+10))
                draw.point((x+10, y+10), fill=new_color)
                pixels.append((r,g,b))
                r,g,b = image.getpixel((x-10,y-10))
                draw.point((x-10, y-10), fill=new_color)
                pixels.append((r,g,b))
                r,g,b = image.getpixel((x+10,y-10))
                draw.point((x+10, y-10), fill=new_color)
                pixels.append((r,g,b))
                r,g,b = image.getpixel((x-10,y+10))
                draw.point((x-10, y+10), fill=new_color)
                pixels.append((r,g,b))
                ############################################ EDGE
                
                r,g,b = image.getpixel((x,y+10))
                #print("Pixel down: ({},{},{})".format(r,g,b))
                draw.point((x, y+10), fill=new_color)
                pixels.append((r,g,b))
                
                r,g,b = image.getpixel((x,y-10))
                #print("Pixel up: ({},{},{})".format(r,g,b))
                draw.point((x, y-10), fill=new_color)
                pixels.append((r,g,b))
                r,g,b = image.getpixel((x+10,y))
                #print("Pixel right: ({},{},{})".format(r,g,b))
                draw.point((x+10, y), fill=new_color)
                pixels.append((r,g,b))
                
                r,g,b = image.getpixel((x-10,y))
                draw.point((x-10, y), fill=new_color)
                pixels.append((r,g,b))

                candy = identifyCandy(pixels)

                '''
                if(candy==8):
                    candy=3
                    flag=True
                    print("ERROR: ",end="")
                    print("{},{}: ".format(counter_y,counter_x),end="")
                    print(pixels)
                    continue '''

                board_matrix[counter_y][counter_x]=candy


                counter_y+=1
            counter_y=0
            counter_x+=1
        image.save('game1 modified.png')
        printMatrix(board_matrix)
        print("-----------------------")    
        
        agente = boardSolver.BoardSolver()
        
        tupla = agente.solve(board_matrix)
        x=tupla[0][1]
        y = tupla[0][0]

        '''
        if(last_movement_x==x and last_movement_y==y):
            counter_rep+=1
        else:
            counter_rep=0
        print(tupla)
        if(counter_rep>5):
            break
            continue 
        
        else: '''

        last_movement_y=y
        last_movement_x=x

        if(tupla[1] == (0,1)):
            fastActuator.crash_candy(x,y,'right')

        elif(tupla[1] == (0,-1)):
            fastActuator.crash_candy(x,y,'left')

        elif(tupla[1] == (-1,0)):
            fastActuator.crash_candy(x,y,'up')

        elif(tupla[1] == (1,0)):
            fastActuator.crash_candy(x,y,'down') 

        time.sleep(0.13)



def sensor():
    pic = pyautogui.screenshot(region = (125,60,790,690))
    pic.save('game1.png')
    image = Image.open('game1.png')
    width, height = image.size
    global restartSensor
    new_color = (255, 255, 255)
    draw = ImageDraw.Draw(image)
    counter_x=0
    counter_y=0
    
    flag = False
    for x in range(45,width,88):
        
        for y in range(25,height,80):
            
            flag = False
            pixels = []
            #print("Pixel: ({},{},{})".format(r,g,b))
            r,g,b = image.getpixel((x-30,y-24))
            draw.point((x-30, y-24), fill=new_color)
            #print("r g b -> ({},{},{})".format(r,g,b))
            '''
            if(not(r in range(35,105) and g in range(60,130) and b in range(65,140)) and r+g+b>=220):
                candy = identifyPackedCandy(r,g,b)
                print("packed candy")
                board_matrix[counter_y][counter_x]=candy
                counter_y+=1
                continue '''
            
            #print("{},{}".format(counter_y,counter_x))
            r,g,b = image.getpixel((x,y))
            #print("Pixel center: ({},{},{})".format(r,g,b))
            draw.point((x, y), fill=new_color)
            pixels.append((r,g,b))
            ############################################ EDGE
            r,g,b = image.getpixel((x+10,y+10))
            draw.point((x+10, y+10), fill=new_color)
            pixels.append((r,g,b))
            r,g,b = image.getpixel((x-10,y-10))
            draw.point((x-10, y-10), fill=new_color)
            pixels.append((r,g,b))
            r,g,b = image.getpixel((x+10,y-10))
            draw.point((x+10, y-10), fill=new_color)
            pixels.append((r,g,b))
            r,g,b = image.getpixel((x-10,y+10))
            draw.point((x-10, y+10), fill=new_color)
            pixels.append((r,g,b))
            ############################################ EDGE
            
            r,g,b = image.getpixel((x,y+10))
            #print("Pixel down: ({},{},{})".format(r,g,b))
            draw.point((x, y+10), fill=new_color)
            pixels.append((r,g,b))
            
            r,g,b = image.getpixel((x,y-10))
            #print("Pixel up: ({},{},{})".format(r,g,b))
            draw.point((x, y-10), fill=new_color)
            pixels.append((r,g,b))
            r,g,b = image.getpixel((x+10,y))
            #print("Pixel right: ({},{},{})".format(r,g,b))
            draw.point((x+10, y), fill=new_color)
            pixels.append((r,g,b))
            
            r,g,b = image.getpixel((x-10,y))
            draw.point((x-10, y), fill=new_color)
            pixels.append((r,g,b))
            candy = identifyCandy(pixels)

            if(candy==8):
                candy=3
                print("ERROR: ",end="")
                print("{},{}: ".format(counter_y,counter_x),end="")
                print(pixels)
                continue
            
            board_matrix[counter_y][counter_x]=candy
            counter_y+=1
        counter_y=0
        counter_x+=1
    image.save('game1 modified.png')
    printMatrix(board_matrix)
    print("-----------------------")    
    '''
    agente = boardSolver.BoardSolver()
    
	@@ -386,25 +385,26 @@
    x=tupla[0][1]
    y = tupla[0][0]
    print(tupla)
    if(tupla[1] == (0,1)):
        actuators.crash_candy(x,y,'right')
    elif(tupla[1] == (0,-1)):
        actuators.crash_candy(x,y,'left')
    elif(tupla[1] == (-1,0)):
        actuators.crash_candy(x,y,'up')
    elif(tupla[1] == (1,0)):
        actuators.crash_candy(x,y,'down') 
    time.sleep(1)  '''


sensorLoop()
#sensor()