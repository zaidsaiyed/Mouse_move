import pyautogui, keyboard, random

'''
Please note that screen resolution is 1920x1080
Please insall the following modules:
    pyautogui - pip install pyautogui
    keyboard - pip install keyboard
    
Start the program and it will move the mouse to random coordinates
To stop the program press and hold the 'ctrl+alt+shift+z' key for 1-2 seconds

Created by: @zaidsaiyed
'''

def move_mouse():
    
    x_axis = random.randint(0, 1919)
    y_axis = random.randint(0, 1079)
    
    time = random.random() # The amount of time it takes to move the mouse to the random coordinates
    
    pyautogui.moveTo(x_axis, y_axis, time)
    
while True:
    if keyboard.is_pressed('ctrl+alt+shift+z'):
        break
    else:
        move_mouse()