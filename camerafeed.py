import numpy as np
from PIL import ImageGrab
import cv2



# Function to capture the screen
def capture_screen(bbox=(300, 300, 1500, 1000)):
    cap_scr = np.array(ImageGrab.grab(bbox))
    cap_scr = cv2.cvtColor(cap_scr, cv2.COLOR_RGB2BGR)
    return cap_scr


# Function to capture the screen
def capture_screen(bbox=(300, 300, 1500, 1000)):
    cap_scr = np.array(ImageGrab.grab(bbox))
    cap_scr = cv2.cvtColor(cap_scr, cv2.COLOR_RGB2BGR)
    return cap_scr