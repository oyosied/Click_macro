from pynput.keyboard import Listener
import pyautogui
from pynput import mouse
import time

both_pos = []
pressed_key  = None

def on_click(x, y, button, pressed):
    if pressed:
        #print ("{0} {1}".format(x,y))
        print(pressed_key)
        if pressed_key == "1":
            both_pos.append("{0}".format(x,y))
            both_pos.append("{1}".format(x,y))
            #print("test" + x_pos + y_pos)
            print (x_pos + y_pos)
        else:
            pass
        if pressed_key == 'q':
            return False

def on_press(key):
    print("To replay press 'q' , to stop recording press '1' , to record again press '1' .")
    global pressed_key
    if 'Key.esc' in str(key):
        return False
    if '1' in str(key):
        pressed_key= None if pressed_key == '1' else '1'
    if 'q' in str(key):
        print("Replaying actions")
        print(str(len(both_pos)))
        for point in range(0,len(both_pos),2):
            time.sleep(3)
            print("clicking")
            pyautogui.click(x=int(both_pos[point]),y=int(both_pos[point+1]))
        print("done...")
        return False
        


mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()
with Listener(on_press=on_press) as listener:  # Create an instance of Listener
    listener.join()
    #print(mouse_listener.mouse_positions)
