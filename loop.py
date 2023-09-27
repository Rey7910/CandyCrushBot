import cv2
import numpy as np
import time
import pyautogui
import boardSolver
import actuators



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



blue_img = cv2.imread('img/blue candy.png',cv2.IMREAD_UNCHANGED)
red_img = cv2.imread('img/red candy.png',cv2.IMREAD_UNCHANGED)
violet_img = cv2.imread('img/violet candy.png',cv2.IMREAD_UNCHANGED)
green_img = cv2.imread('img/green candy.png',cv2.IMREAD_UNCHANGED)
yellow_img = cv2.imread('img/yellow candy.png',cv2.IMREAD_UNCHANGED)
orange_img = cv2.imread('img/orange candy.png',cv2.IMREAD_UNCHANGED)
srv_img = cv2.imread('img/special red vertical candy.png',cv2.IMREAD_UNCHANGED)
svv_img = cv2.imread('img/special violet vertical candy.png',cv2.IMREAD_UNCHANGED)
syv_img = cv2.imread('img/special yellow vertical candy.png',cv2.IMREAD_UNCHANGED)
syh_img = cv2.imread('img/special yellow horizontal candy.png',cv2.IMREAD_UNCHANGED)
soh_img = cv2.imread('img/special orange horizontal candy.png',cv2.IMREAD_UNCHANGED)
sbv_img = cv2.imread('img/special blue vertical candy.png',cv2.IMREAD_UNCHANGED)
sbh_img = cv2.imread('img/special blue horizontal candy.png',cv2.IMREAD_UNCHANGED)
sov_img = cv2.imread('img/special orange vertical candy.png',cv2.IMREAD_UNCHANGED)
py_img = cv2.imread('img/packed yellow candy.png',cv2.IMREAD_UNCHANGED)
pv_img = cv2.imread('img/packed violet candy.png',cv2.IMREAD_UNCHANGED)
pg_img = cv2.imread('img/packed violet candy.png',cv2.IMREAD_UNCHANGED)
choco_img = cv2.imread('img/chocolate.png',cv2.IMREAD_UNCHANGED)

templates = [(blue_img,1,0.75),(red_img,2,0.75),(violet_img,3,0.75),(green_img,5,0.67),(yellow_img,4,0.9),(orange_img,0,0.88),(srv_img,12,0.85),(svv_img,13,0.85),
             (syv_img,14,0.9) , (syh_img,11,0.9) ,(pv_img,23,0.82) , (py_img,24,0.85), (pg_img,25,0.7) ,(sbh_img,11,0.8) , (sbv_img,11,0.85) ,(soh_img,10,0.85),(choco_img,66,0.8)]

def calculatePositionX(num):

    ranges = [(35,65,0),(120,155,1),(215,240,2),(310,350,3),(390,420,4),(480,515,5),(570,600,6),(650,680,7),(740,770,8)]

    for start, end, value in ranges:
        if start <= num < end:
            return value
    return 8



def calculatePositionY(num):
    ranges = [(35, 65, 0), (110, 135, 1), (190, 220, 2), (265, 295, 3),
              (340, 370, 4), (420, 450, 5), (500, 530, 6), (570, 600, 7),
              (650, 680, 8)]

    for start, end, value in ranges:
        if start <= num < end:
            return value
    return 8


def printMatrix(matrix):
    for i in range(9):
        for j in range(9):
            print(matrix[i][j],end=" ")
        print()

def Action(board_matrix):
        agente = boardSolver.BoardSolver()
        
        tupla = agente.solve(board_matrix)
        x=tupla[0][1]
        y = tupla[0][0]

        if(tupla[1] == (0,1)):
            actuators.crash_candy(x,y,'right')

        elif(tupla[1] == (0,-1)):
            actuators.crash_candy(x,y,'left')

        elif(tupla[1] == (-1,0)):
            actuators.crash_candy(x,y,'up')

        elif(tupla[1] == (1,0)):
            actuators.crash_candy(x,y,'down') 
        
        time.sleep(0.13)


def fillMatrix(rectangles,candy):
    #print(candy)
    for i in rectangles:
        #print(int(i[0]+(i[2]/2)),int(i[1]+(i[3]/2)))

        center_x = int(i[0]+(i[2]/2))
        center_y = int(i[1]+(i[3]/2))

        position_x = calculatePositionX(center_x)
        position_y = calculatePositionY(center_y)
        #print("Position x: ",position_x)
        #print("Position y: ",position_y)
        if(position_x == 'none' or position_y=='none'):
            continue
        else:
            board_matrix[position_y][position_x]=candy


def sense():
    pic = pyautogui.screenshot(region = (125,45,800,710))
    pic.save('dashboard.png')
    board_img = cv2.imread('dashboard.png',cv2.IMREAD_UNCHANGED)

    for template,candy,treshold in templates:
        rectangles=[]
        w=template.shape[1]
        h=template.shape[0]
        result = cv2.matchTemplate(board_img, template, cv2.TM_CCOEFF_NORMED)
        yloc,xloc = np.where(result>=treshold)
        for(x,y) in zip(xloc,yloc):
            rectangles.append([int(x),int(y),int(w),int(h)])

        rectangles, weights = cv2.groupRectangles(rectangles,1,0.2)
        fillMatrix(rectangles,candy)

        for (x,y,w,h) in rectangles:
            cv2.rectangle(board_img, (x,y) ,(x+w,y+h),(0,255,255),2)  

        cv2.imshow('candy '+str(candy),board_img)
        cv2.waitKey()
        cv2.destroyAllWindows()
        board_img = cv2.imread('dashboard.png',cv2.IMREAD_UNCHANGED)
    
    printMatrix(board_matrix)
    #print("---------------")
    #Action(board_matrix)




st = time.time()
#sense()
st_2 = time.time()

#printMatrix(board_matrix)
#print(st_2-st)
def proof():
    while(True):
        
        pic1 = pyautogui.screenshot(region = (125,45,800,710))
        pic1.save('dashboard.png')

        #time.sleep(0.1)

        pic2=pyautogui.screenshot(region = (125,45,800,710))
        pic2.save('dashboard2.png')
        
        if open("dashboard.png","rb").read() == open("dashboard2.png","rb").read():
            st = time.time()
            sense()
            st_2 = time.time()
            print(st_2-st)
        else:
            print("moving")
    
#st_2 = time.time()

def NoMove():
    while(True):
        sense()

NoMove()






'''
for (x,y,w,h) in rectangles:
        cv2.rectangle(board_img, (x,y) ,(x+w,y+h),(0,255,255),2)  

cv2.imshow('Board',board_img)
cv2.waitKey()
cv2.destroyAllWindows() '''

