import mss
import time

# Acer Nitro 5 (Full Screen) Configuration - Rey

top=80
left=130
width=710
height=710

def screen_recognition():
    with mss.mss() as sct:
        monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)


def shoot_ss():
    
    with mss.mss() as sct:
        time.sleep(3)
    # The screen part to capture
        monitor = {"top": top, "left": left, "width": width, "height": height}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)


shoot_ss()