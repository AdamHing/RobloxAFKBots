import pydirectinput as pdi
import time
# import win32gui as wg
sec = 3

def forward():
        pdi.keyDown('w')
        time.sleep(sec)
        pdi.keyUp('w')

def back():
    pdi.keyDown('s')
    time.sleep(sec)
    pdi.keyUp('s')



    # wg.FindWindow('Roblox')
    # wg.SetForegroundWindow()
    