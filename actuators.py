import pyautogui
import time

# Acer Nitro 5 (Full Screen) Configuration - Rey

x_growth_factor = 90
y_growth_factor = 80
x_reference = 170
y_reference = 80


def move_candy(start_x, start_y,end_x,end_y):

    # Move the mouse to the starting position
    pyautogui.moveTo(start_x, start_y)

    # Begin the drag action
    pyautogui.mouseDown()

    # Move the mouse to the ending position (simulating dragging)
    pyautogui.moveTo(end_x, end_y)  

    # Release the mouse button to complete the drag action
    pyautogui.mouseUp()

#90*90


def crash_candy(x,y,direction):


    # Pixel Direction of the movement to the right side
    if(direction=='right'):
        move_candy(x_reference+(x*x_growth_factor),y_reference+(y*y_growth_factor),x_reference+(x*x_growth_factor)+x_growth_factor,y_reference+(y*y_growth_factor))
    
    # Pixel Direction of the movement to the left side
    elif(direction=='left'):
        move_candy(x_reference+(x*x_growth_factor),y_reference+(y*y_growth_factor),x_reference+(x*x_growth_factor)-x_growth_factor,y_reference+(y*y_growth_factor))
    
    # Pixel Direction of the movement to the up side
    elif(direction=='up'):
        move_candy(x_reference+(x*x_growth_factor),y_reference+(y*y_growth_factor),x_reference+(x*x_growth_factor),y_reference+(y*y_growth_factor)-y_growth_factor)
    
    # Pixel Direction of the movement to the down side
    elif(direction == 'down'):
        move_candy(x_reference+(x*x_growth_factor),y_reference+(y*y_growth_factor),x_reference+(x*x_growth_factor),y_reference+(y*y_growth_factor)+y_growth_factor)



def test_actuators(x,y):

    crash_candy(x,y,'down')
    crash_candy(x,y,'up')
    crash_candy(x,y,'left')
    crash_candy(x,y,'right')


def test_full_movements():

    time.sleep(2)

    for x in range(9):
        for y in range(9):
            crash_candy(x,y,'down')
            crash_candy(x,y,'up')
            crash_candy(x,y,'left')
            crash_candy(x,y,'right')
        


test_full_movements()
