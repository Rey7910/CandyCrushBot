import pyautogui
import time
from PIL import Image, ImageDraw
import boardSolver
import actuators

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
        return 8




agent = boardSolver.BoardSolver()

def identifyCandy(pixels,acumulator_r,acumulator_b):


    for i in pixels:
        if(i[0] in range(30,66) and i[1] in range(159,255) and i[2] in range(-1,21)):
            
            if(acumulator_b>=200):
                #print("special green")
                return 15 # green
            else:
                #print("green")
                return 5

        elif(i[0] in range(240,256) and i[1] in range(110,160) and i[2] in range(-1,20)):
            
            if(acumulator_b>=500):
                #print("special orange")
                return 10
            else:
                #print("orange")
                return 0 # orange

        
        elif(i[0] in range(5,50) and i[1] in range(120,270) and i[2] in range(220,256)):
            if(acumulator_b<=3100 or acumulator_r>=1000):
                #print("special blue")
                return 11
            else:
                #print("blue")
                print(acumulator_b)
                print(acumulator_r)
                return 1 #blue
        
        elif(i[0] in range(200,256) and i[1] in range(200,255) and i[2] in range(-1,20)):
            
            if(acumulator_b>=300):
                #print("special yellow")
                return 14
            else:

                #print("yellow")
                return 4

        
        elif(i[0] in range(240,256) and i[1] in range(0,20) and i[2] in range(-1,20)):
            
            if(acumulator_b>=100):
                #print("special red")
                return 12
            else:

                #print("red")
                return 2 # red
        
        elif(i[0] in range(160,230) and i[1] in range(15,80) and i[2] in range(230,256)):
            
            if(acumulator_b!=3315):
                #print("special violet")
                return 13
            else:
                #print("violet")
                return 3 # violet
        
        
    
    return 8



def sensorLoop():

    counter=0
    while(True):
        counter+=1
        pic = pyautogui.screenshot(region = (125,60,790,690))
        allow=True
        pic.save('game200.png'.format(counter))

        image = Image.open('game200.png'.format(counter))

        width, height = image.size

        new_color = (255, 255, 255)

        draw = ImageDraw.Draw(image)

        counter_x=0
        counter_y=0
        #special_candies = ()
        special_candies=[]

        

        for x in range(50,width,88):
            
            for y in range(25,height,80):
                acumulator_r=0
                acumulator_b=0
                pixels = []
                #print("Pixel: ({},{},{})".format(r,g,b))
                r,g,b = image.getpixel((x-30,y-24))
                draw.point((x-30, y-24), fill=new_color)
                '''
                if(g>=180):
                    mult_g+=1
                if(b>=180):
                    mult_b+=1 '''

                #print("r g b -> ({},{},{})".format(r,g,b))
                
                '''if(not(r in range(35,105) and g in range(60,130) and b in range(65,140)) and r+g+b>=220):
                    candy = identifyPackedCandy(r,g,b)
                    print("packed candy")
                    board_matrix[counter_y][counter_x]=candy
                    special_candies.append((counter_y,counter_x))
                    counter_y+=1
                    continue '''
                
                #print("{},{}".format(counter_y,counter_x))

                r,g,b = image.getpixel((x,y))

                draw.point((x, y), fill=new_color)

                pixels.append((r,g,b))

                acumulator_r+=r
                acumulator_b+=b

                ############################################ EDGE

                # Down
                r,g,b = image.getpixel((x,y+5))
                draw.point((x, y+5), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b

                r,g,b = image.getpixel((x,y+10))
                draw.point((x, y+10), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b


                r,g,b = image.getpixel((x,y+15))
                draw.point((x, y+15), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b

                # up
                r,g,b = image.getpixel((x,y-5))
                draw.point((x, y-5), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b


                r,g,b = image.getpixel((x,y-10))
                draw.point((x, y-10), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b


                r,g,b = image.getpixel((x,y-15))
                draw.point((x, y-15), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b

                # left

                r,g,b = image.getpixel((x+5,y))
                draw.point((x+5, y), fill=new_color)
                pixels.append((r,g,b))

                acumulator_r+=r
                acumulator_b+=b

                r,g,b = image.getpixel((x+10,y))
                draw.point((x+10, y), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b

                r,g,b = image.getpixel((x+15,y))
                draw.point((x+15, y), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b

                # right

                r,g,b = image.getpixel((x-5,y))
                draw.point((x-5, y), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b


                r,g,b = image.getpixel((x-10,y))
                draw.point((x-10, y), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b


                r,g,b = image.getpixel((x-15,y))
                draw.point((x-15, y), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b
                

                #print("Path [{}][{}]".format(counter_y,counter_x))

                candy = identifyCandy(pixels, acumulator_r, acumulator_b)
    
                board_matrix[counter_y][counter_x]=candy

                if(candy>=10):
                    special_candies.append((counter_y,counter_x))


                counter_y+=1


            counter_y=0
            counter_x+=1


        #image.save('game1 modified.png')

        #printMatrix(board_matrix)
        #print("-----------------------")    
        
        agente = boardSolver.BoardSolver()
        
        if(len(special_candies)!=1):
            special_candies=tuple(special_candies)
            
        
        #print(special_candies)

        tupla = agente.solve(board_matrix)#,special_candies)
        x=tupla[0][1]
        y = tupla[0][0]

        #print(tupla)
        

        

        if(tupla[1] == (0,1)):
            actuators.crash_candy(x,y,'right')

        elif(tupla[1] == (0,-1)):
            actuators.crash_candy(x,y,'left')

        elif(tupla[1] == (-1,0)):
            actuators.crash_candy(x,y,'up')

        elif(tupla[1] == (1,0)):
            actuators.crash_candy(x,y,'down') 

        else:
            print("ERROR")
        
        time.sleep(0.2) 

        

        


def sensor():

        #pic = pyautogui.screenshot(region = (125,60,790,690))

        #pic.save('game5.png')

        image = Image.open('game27.png')

        width, height = image.size

        new_color = (255, 255, 255)

        draw = ImageDraw.Draw(image)

        counter_x=0
        counter_y=0
        #special_candies = ()
        special_candies=[]

        

        for x in range(50,width,88):
            
            for y in range(25,height,80):
                acumulator_r=0
                acumulator_b=0
                pixels = []
                #print("Pixel: ({},{},{})".format(r,g,b))
                r,g,b = image.getpixel((x-30,y-24))
                draw.point((x-30, y-24), fill=new_color)

                r,g,b = image.getpixel((x+35,y+20))
                draw.point((x+35, y+20), fill=new_color)
                print((r,g,b))
                '''
                if(g>=180):
                    mult_g+=1
                if(b>=180):
                    mult_b+=1 '''

                #print("r g b -> ({},{},{})".format(r,g,b))
                
                '''if(not(r in range(35,105) and g in range(60,130) and b in range(65,140)) and r+g+b>=220):
                    candy = identifyPackedCandy(r,g,b)
                    print("packed candy")
                    board_matrix[counter_y][counter_x]=candy
                    special_candies.append((counter_y,counter_x))
                    counter_y+=1
                    continue '''
                
                #print("{},{}".format(counter_y,counter_x))

                r,g,b = image.getpixel((x,y))

                draw.point((x, y), fill=new_color)

                pixels.append((r,g,b))

                acumulator_r+=r
                acumulator_b+=b

                ############################################ EDGE

                # Down
                r,g,b = image.getpixel((x,y+5))
                draw.point((x, y+5), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b

                r,g,b = image.getpixel((x,y+10))
                draw.point((x, y+10), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b


                r,g,b = image.getpixel((x,y+15))
                draw.point((x, y+15), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b

                # up
                r,g,b = image.getpixel((x,y-5))
                draw.point((x, y-5), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b


                r,g,b = image.getpixel((x,y-10))
                draw.point((x, y-10), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b


                r,g,b = image.getpixel((x,y-15))
                draw.point((x, y-15), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b

                # left

                r,g,b = image.getpixel((x+5,y))
                draw.point((x+5, y), fill=new_color)
                pixels.append((r,g,b))

                acumulator_r+=r
                acumulator_b+=b

                r,g,b = image.getpixel((x+10,y))
                draw.point((x+10, y), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b

                r,g,b = image.getpixel((x+15,y))
                draw.point((x+15, y), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b

                # right

                r,g,b = image.getpixel((x-5,y))
                draw.point((x-5, y), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b


                r,g,b = image.getpixel((x-10,y))
                draw.point((x-10, y), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b


                r,g,b = image.getpixel((x-15,y))
                draw.point((x-15, y), fill=new_color)
                pixels.append((r,g,b))
                acumulator_r+=r
                acumulator_b+=b

                background_counter=0
                for i in pixels:
                    
                    if(i[0] in range(40,100) and i[1] in range(0,130) and i[2] in range(0,140)):
                        background_counter+=1

                if(background_counter>=3):
                    allow=False


                print("Path [{}][{}]".format(counter_y,counter_x))

                candy = identifyCandy(pixels, acumulator_r, acumulator_b)
    
                board_matrix[counter_y][counter_x]=candy

                if(candy>=10):
                    special_candies.append((counter_y,counter_x))


                counter_y+=1


            counter_y=0
            counter_x+=1


        image.save('game1 modified.png')

        printMatrix(board_matrix)
        print("-----------------------")    
        
        agente = boardSolver.BoardSolver()
        
        if(len(special_candies)!=1):
            special_candies=tuple(special_candies)
            
        
        print(special_candies)

        tupla = agente.solve(board_matrix,special_candies)
        x=tupla[0][1]
        y = tupla[0][0]

        print(tupla)
        

        '''

        if(tupla[1] == (0,1)):
            actuators.crash_candy(x,y,'right')

        elif(tupla[1] == (0,-1)):
            actuators.crash_candy(x,y,'left')

        elif(tupla[1] == (-1,0)):
            actuators.crash_candy(x,y,'up')

        elif(tupla[1] == (1,0)):
            actuators.crash_candy(x,y,'down') 

        else:
            print("ERROR")
        
        time.sleep(0.2)  '''




sensorLoop()
#sensor()