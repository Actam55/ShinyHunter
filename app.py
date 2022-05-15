import pyautogui
import time

imageFolder = "Route 29"
route29Mons = ['D:\Code\Python\ShinyHunt\Route 29\HoothootIG.png', 'D:\Code\Python\ShinyHunt\Route 29\PidgeyIG.png',
               'D:\Code\Python\ShinyHunt\Route 29\RattataDayIG.png', 'D:\Code\Python\ShinyHunt\Route 29\RattataNightIG.png', 'D:\Code\Python\ShinyHunt\Route 29\SentretIG.png']
route29Monsv2 = ['D:\Code\Python\ShinyHunt\Route 29 v2\HoothootIG.png', 'D:\Code\Python\ShinyHunt\Route 29 v2\PidgeyIG.png',
                 'D:\Code\Python\ShinyHunt\Route 29 v2\RattataDayIG.png', 'D:\Code\Python\ShinyHunt\Route 29 v2\SentretIG.png']

# for image in os.listdir(imageFolder):
#     filename = os.path.basename(image)
#     if filename[0] == 'S' and filename[1] == '-':
#         shiny.append(image)
#     elif filename != "NotInBattle.png" and filename != "InBattle.png":
#         nonShiny.append(image)


def RunArround():
    time.sleep(2)
    RunLeft()
    time.sleep(0.2)
    RunRight()

def RunLeft():
    pyautogui.keyDown('left')
    time.sleep(2)
    pyautogui.keyUp('left')

def RunRight():
    pyautogui.keyDown('right')
    time.sleep(2)
    pyautogui.keyUp('right')

def CheckIfInBattle():
    if not pyautogui.locateOnScreen("NotInBattle.png", confidence=0.8):
        print("In battle")
        #postEvent("Battle detected", True)
        return True
    else:
        print("Not in battle")
        return False

def CheckIfShiny():
    for image in route29Monsv2:
        if pyautogui.locateOnScreen(image):
            print("No shiny found")
            #postEvent("Shiny found", True)
            return False
    print("Shiny found")
    return True

def RunAway():
    time.sleep(2)
    pyautogui.keyDown('down')
    time.sleep(0.2)
    pyautogui.keyUp('down')
    pyautogui.keyDown('down')
    time.sleep(0.2)
    pyautogui.keyUp('down')
    time.sleep(0.2)
    pyautogui.keyDown('right')
    time.sleep(0.2)
    pyautogui.keyUp('right')
    pyautogui.keyDown('z')
    time.sleep(0.2)
    pyautogui.keyUp('z')
    time.sleep(2)

def RALoop():
    time.sleep(2)
    shinyFound = False
    counter = 0
    while shinyFound == False:
        pyautogui.keyDown('space')
        time.sleep(2)
        if CheckIfInBattle():
            if CheckIfShiny():
                pyautogui.keyUp('space')
                shinyFound = True
            else:
                counter = counter + 1
                RunAway()
                print(counter)
        else:
            RunArround()


RALoop()


#Create new base case for each startup to fix pixel size shit