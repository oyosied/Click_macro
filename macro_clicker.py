from pynput.keyboard import Listener
import pyautogui
from pynput import mouse
import time

both_pos = []
pressed_key  = None
recording_flag = False
replay_flag = False 
def on_click(x, y, button, pressed):
    global recording_flag
    global replay_flag
    if pressed and recording_flag == False and replay_flag == False:
        print("Does not record , please press '1' again . ")
        print(x , y)
    elif pressed and recording_flag and replay_flag == False:
        #print ("{0} {1}".format(x,y))
        print("Click registered ! ")
        print(x , y)
        if pressed_key == "1" :
            both_pos.append("{0}".format(x,y))
            both_pos.append("{1}".format(x,y))
            #print("test" + x_pos + y_pos)
        else:
            pass
        # if pressed_key == 'q':
        #     return False
    
def on_press(key):
    global pressed_key
    global recording_flag
    global replay_flag
    if 'Key.esc' in str(key):
        return False
    if '1' in str(key):
        recording_flag = False if recording_flag else True
        replay_flag = False
        if recording_flag:
            print("To replay press 'q' , to stop recording press '1' , to record again press '1' .")
            print("Recording mouse clicks .... ")
        if recording_flag == False :
            print("Recording stopped , to add more clicks press '1' again . ")
        pressed_key= None if pressed_key == '1' else '1'
    if 'q' in str(key):
        replay_flag = True
        pressed_key = 'q'
        print("Replaying actions")
        print(str(len(both_pos)))
        for point in range(0,len(both_pos),2):
            print("clicking")
            pyautogui.click(x=int(both_pos[point]),y=int(both_pos[point+1]))
        print("done...")

        


mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()
with Listener(on_press=on_press) as listener:  # Create an instance of Listener
    listener.join()
    #print(mouse_listener.mouse_positions)
