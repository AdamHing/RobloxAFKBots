import win32gui
import win32process
import argparse

#this code cycles through all the roblox instances by their pid and focuses on the window.

ap=argparse.ArgumentParser()
ap.add_argument("-p", "--pid", type=int, required=True,help="the pid")

args=vars(ap.parse_args())
pids = args["pid"]
print(pids)


def enum_window_callback(hwnd, pid):

    a,current_pid = win32process.GetWindowThreadProcessId(hwnd)
    # print(pid)
    print(current_pid)
    # print(current_pid)
    if pid == current_pid and win32gui.IsWindowVisible(hwnd):
        win32gui.SetForegroundWindow(hwnd)
        print("window activated") 
    

win32gui.EnumWindows(enum_window_callback,pids)
