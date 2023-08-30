import pyautogui
import time

top=80
left=130

def Move_candy(start_x, start_y,end_x,end_y):

    time.sleep(5)

    # Move the mouse to the starting position
    pyautogui.moveTo(start_x, start_y)

    # Begin the drag action
    pyautogui.mouseDown()

    # Move the mouse to the ending position (simulating dragging)
    pyautogui.moveTo(end_x, end_y)  

    # Release the mouse button to complete the drag action
    pyautogui.mouseUp()


while(True):
    Move_candy(150,90,250,90)
    Move_candy(150,90,170,190)