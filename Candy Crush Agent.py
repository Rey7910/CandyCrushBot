import pyautogui
import time
from PIL import ImageGrab


def Click():
    # Wait a period of time before continue with the rest of code
    time.sleep(5)

    # Click cordenates
    x_coord = 500
    y_coord = 500

    # Move the mouse and click
    pyautogui.moveTo(x_coord, y_coord)
    pyautogui.click()


def shoot_ss():

    # Define limits per each side of the screen (izquierda, superior, derecha, inferior)
    bounding_box = (100, 100, 500, 500)

    # Capture the specific region throughout the screen
    screenshot = ImageGrab.grab(bbox=bounding_box)

    # Resize the image to a lower resolution
    #resized_screenshot = screenshot.resize((320, 240))

    # Save the image
    #resized_screenshot.save("captura_baja_resolucion.png")

def pyautogui_ss():
        # Tomar una captura de pantalla completa
    screenshot = pyautogui.screenshot()

    # Guardar la captura de pantalla en un archivo
    screenshot.save("captura_de_pantalla.png")



pyautogui_ss()
Click()