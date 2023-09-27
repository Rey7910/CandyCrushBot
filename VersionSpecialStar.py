import pyautogui
import time
from PIL import Image, ImageDraw
import boardSolver
import actuators
import solver2

restartSensor=0
special_canides =[]
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

    if(r in range(80,130) and g in range(35,65) and b in range(-1,20)):
        return 66

    elif (r in range(220,256) and g in range(70,100) and b in range(70,100)):
        return 22 # red packed candy
    elif (r in range(80,150) and g in range(120,220) and b in range(50,130)):
        return 25 # green packed candy
    
    elif(r in range(100,250) and g in range(70,150) and b in range(210,260)):
        return 23 # violet packed candy
    
    elif(r in range(230,280) and g in range(150,250) and b in range(90,130)):
        return 24 # yellow packed candy
    elif(r in range(160,350) and g in range(100,250) and b in range(0,150)):
        return 20 # orange packed candy

    elif(r in range(20,120) and g in range(100,270) and b in range(150,300)):
        return 21 # blue packed candy

    else:
        return 66
agent = boardSolver.BoardSolver()
def identifyCandy(pixels):
    special=False
    counter=0
    for i in pixels:
        
        if(i[0] in range(30,130) and i[1] in range(20,70) and i[2] in (0,25)):
            return 66

        elif(i[0] in range(30,66) and i[1] in range(159,196) and i[2] in range(0,20)):
            b=0
            for i in pixels:
                b+=i[2]

            print(b)

            if b>600:
                return 15
            return 5
        elif(i[0] in range(240,256) and i[1] in range(110,160) and i[2] in range(0,20)):
            r=0
            for i in pixels:
                r+=i[0]

            if r<2270:
                return 10

            return 0
        
        elif(i[0] in range(5,50) and i[1] in range(120,270) and i[2] in range(220,256)):
            b=0
            for i in pixels:
                b+=i[2]
            
            if(b<=2000):
                return 11
            else:
                return 1
        
        elif(i[0] in range(200,256) and i[1] in range(200,255) and i[2] in range(0,20)):
            b=0
            for i in pixels:
                b+=i[2]
            
            if(b>300):
                return 14
            return 4
        
        elif(i[0] in range(240,256) and i[1] in range(0,20) and i[2] in range(0,20)):
            
            b=0
            for i in pixels:
                b+=i[2]

            print(b)

            if b>150:
                return 12
            
            
            
            return 2
        
        elif(i[0] in range(160,230) and i[1] in range(15,80) and i[2] in range(230,256)):
            
            
            if(i[2]!=255):
                return 13
            else:

                return 3
        
        
    #print(pixels)
    return 8
def sensorLoop():

    
    while(True):
        special_candies=[]
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
                
                if(not(r in range(35,105) and g in range(60,130) and b in range(65,140)) and r+g+b>=220):
                    candy = identifyPackedCandy(r,g,b)
                    special_candies.append((counter_y,counter_x))
                    board_matrix[counter_y][counter_x]=candy
                    counter_y+=1
                    continue 
                
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

                if(candy>=10):
                    special_candies.append((counter_y,counter_x))

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
        #image.save('game1 modified.png')
        #printMatrix(board_matrix)
        #print("-----------------------")    
        
        agente = solver2.BoardSolver()
        
        if(len(special_candies)!=1):
            special_candies=tuple(special_candies)

        tupla = agente.solve(board_matrix,special_candies)
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
            actuators.crash_candy(x,y,'right')

        elif(tupla[1] == (0,-1)):
            actuators.crash_candy(x,y,'left')

        elif(tupla[1] == (-1,0)):
            actuators.crash_candy(x,y,'up')

        elif(tupla[1] == (1,0)):
            actuators.crash_candy(x,y,'down') 

        st_2 = time.time()
        time.sleep(0.13)



def sensor():
    special_candies=[]
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
            
            if(not(r in range(35,105) and g in range(60,130) and b in range(65,140)) and r+g+b>=220):
                candy = identifyPackedCandy(r,g,b)
                special_candies.append((counter_y,counter_x))
                board_matrix[counter_y][counter_x]=candy
                counter_y+=1
                continue 
            
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

            if(candy>=10):
                special_candies.append((counter_y,counter_x))

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
    
    agente = solver2.BoardSolver()
    
    if(len(special_candies)!=1):
        special_candies = sorted(special_candies,reverse=True)
        special_candies=tuple(special_candies)

    tupla = agente.solve(board_matrix,special_candies)
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
        actuators.crash_candy(x,y,'right')

    elif(tupla[1] == (0,-1)):
        actuators.crash_candy(x,y,'left')

    elif(tupla[1] == (-1,0)):
        actuators.crash_candy(x,y,'up')

    elif(tupla[1] == (1,0)):
        actuators.crash_candy(x,y,'down') 

    st_2 = time.time()
    time.sleep(0.13)


#sensorLoop()
sensor()