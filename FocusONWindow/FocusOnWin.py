import psutil 
import time
#imports module for moveing the character
import movePlayer as mp

def check_process_status(process_name):
    process_status = [ proc for proc in psutil.process_iter() if proc.name() == process_name ]
    if process_status:
        print(process_status)

    else:
        print("Process name not valid", process_name)

    return process_status
process_status = check_process_status("RobloxPlayerBeta.exe")
while 1:

    for current_process in process_status:
        print(current_process.pid)


        pidforlib = str(current_process.pid)

        openlib = "python focuslib.py -p " + pidforlib 
        psutil.Popen(openlib)
        time.sleep(2)
        mp.forward()
        time.sleep(0.1)
        mp.back()
        time.sleep(2)
        # time.sleep(900)
        

