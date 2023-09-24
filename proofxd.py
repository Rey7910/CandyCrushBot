import win32api
import win32con
import time

x_growth_factor = 60
y_growth_factor = 50
x_reference = 150
y_reference = 20

def move_candy(start_x, start_y, end_x, end_y):
    # Mueve el cursor del mouse a la posición de inicio
    win32api.SetCursorPos((start_x, start_y))
    # Presiona el botón izquierdo del mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # Mueve el cursor del mouse a la posición final (simulando el arrastre)
    win32api.SetCursorPos((end_x, end_y))
    time.sleep(0.1)
    # Libera el botón izquierdo del mouse para completar la acción de arrastre
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


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
    time.sleep(0.5)
    crash_candy(x,y,'up')
    time.sleep(0.5)
    crash_candy(x,y,'left')
    time.sleep(0.5)
    crash_candy(x,y,'right')
    time.sleep(0.5)

def test_full_movements():

    time.sleep(2)

    for x in range(9):
        for y in range(9):
            crash_candy(x,y,'down')
            crash_candy(x,y,'up')
            crash_candy(x,y,'left')
            crash_candy(x,y,'right')


test_actuators(0,1)
test_actuators(0,2)
test_actuators(0,3)
test_actuators(0,4)