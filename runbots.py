from selenium import webdriver
import pandas as pd
import time
import psutil 
import pyautogui

data = pd.read_excel(r'RobloxAccountsTest.xlsx')
names = pd.DataFrame(data,columns=['names'])
passwords = pd.DataFrame(data,columns=['passwords'])

nameList = names.values.tolist()
passwordList = passwords.values.tolist()

print(nameList)
print('')
print(passwordList)

print("Wazzup my homi")


for x,y in zip(nameList, passwordList):
    
    time.sleep(1)

    print(x)
    print(y)
    driver = webdriver.Chrome('C:\webdrivers\chromedriver') 
    driver.get("https://www.roblox.com/login")
    usernameStr = x
    passwordStr = y
    username = driver.find_element_by_id('login-username')
    username.send_keys(usernameStr)
    password = driver.find_element_by_id('login-password')
    password.send_keys(passwordStr)
    signInButton = driver.find_element_by_id('login-button')
    signInButton.click()#game-details-play-button-container > button
    time.sleep(4)
    driver.get("https://www.roblox.com/games/6852386028/Warehouse-v-1?refPageId=70c151ea-dc06-4bad-a565-d5591af398a9")
    time.sleep(4)
 
#     <button type="button" class="btn-full-width btn-common-play-game-lg btn-primary-md btn-min-width"><span class="icon-common-play"></span></button>
# //*[@id="game-details-play-button-container"]/button
    try:
        playbutton = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div/button')
        playbutton.click()

        time.sleep(3)

        start = pyautogui.locateCenterOnScreen('OpenRoblox.PNG')#If the file is not a png file it will not work
        print(start)
        time.sleep(2)
        pyautogui.moveTo(start)
        pyautogui.click(start)
        time.sleep(4)


        print("Done one loop.")
        driver.close()
    except:
        break


print("All bots online.")
time.sleep(5)
#focus on window for afkness

FocusOnWin = "C:/ProgramData/Anaconda3/python.exe D:\RobloxCreations\FocusONWindow\FocusOnWin.py"
psutil.Popen(FocusOnWin)