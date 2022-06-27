import time
import pyautogui as pg
from main import get_color, InType, scc_screen

try:
    print("Enter <Ctrl>+C to exit:")
    width, height = pg.size()
    print(f"Display resolution: {width} * {height}")
    time.sleep(1)
    pre_pos = None
    pre_rgb = None
    while True:
        time.sleep(0.5)
        x, y = pg.position()
        pos = str(x) + "," + str(y)
        rgb = str(pg.screenshot().getpixel((x, y)))[1:-1]

        # is move
        if pos == pre_pos and rgb == pre_rgb:
            time.sleep(0.5)
            continue
        pre_pos = pos
        pre_rgb = rgb

        # get color
        color = (scc_screen(rgb))

        # output
        print("Mouse position: ", end='')
        print(pos)
        print("RGB: ", end='')
        print(rgb)
        print("Color: ", end='')
        print(color)

except KeyboardInterrupt:
    exit('\n Bye.\n')