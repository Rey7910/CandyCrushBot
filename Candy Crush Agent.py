import pyautogui
import time
import mss


def Click():
    # Wait a period of time before continue with the rest of code
    time.sleep(5)

    # Click cordenates
    x_coord = 500
    y_coord = 500

    # Move the mouse and click
    pyautogui.moveTo(x_coord, y_coord)
    pyautogui.click()


def pyautogui_ss():
        # Tomar una captura de pantalla completa
    screenshot = pyautogui.screenshot()

    # Guardar la captura de pantalla en un archivo
    screenshot.save("captura_de_pantalla.png")



'''
pyautogui_ss()
Click()'''


with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)