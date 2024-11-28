import numpy as np
from PIL import ImageGrab
import cv2

import cv2

def use_webcam():
    # Initialize the webcam (default is usually 0, but can vary)
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) # change the port if you have problems recognizing the camera

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        return

    print("Press 'q' to exit the video feed.")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame reading is unsuccessful, break the loop
        if not ret:
            print("Error: Unable to read frame from webcam.")
            break

        # Display the captured frame
        cv2.imshow("Webcam Feed", frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to use the webcam
use_webcam()
