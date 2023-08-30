import mss



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
    monitor = {"top": 160, "left": 19, "width": 180, "height": 900}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)