import pydirectinput as pdi
import time
# import win32gui as wg
sec = 3
#presses the W key to move character forwords 
def forward():
        pdi.keyDown('w')
        time.sleep(sec)
        pdi.keyUp('w')
#presses the S key to move character backwords
def back():
    pdi.keyDown('s')
    time.sleep(sec)
    pdi.keyUp('s')
    