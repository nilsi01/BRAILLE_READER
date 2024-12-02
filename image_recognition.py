import os
import serial
import time
from PIL import Image
import pytesseract
from threading import Thread
from camerafeed import CameraFeed

# Replace 'COM5' with the port your Arduino is connected to
arduino_port = 'COM5'
baud_rate = 9600

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize Arduino
try:
    print("Initializing serial connection...")
    arduino = serial.Serial(arduino_port, baud_rate)
    print("Serial connection established.")
    time.sleep(2)
except Exception as e:
    print(f"Error initializing serial connection: {e}")
    exit()


def process_image_and_send_signal(camera_feed):
    """ Continuously process the latest frame and send signals to Arduino. """
    while camera_feed.running:
        latest_frame = None
        with camera_feed.frame_lock:
            latest_frame = camera_feed.latest_frame

        if latest_frame:
            try:
                print(f"Processing latest frame: {latest_frame}")
                image = Image.open(latest_frame).convert("L")
                recognized_text = pytesseract.image_to_string(image)
                print("OCR output:", recognized_text)

                # Send signals to Arduino
                for letter in recognized_text:
                    if letter.isalpha():
                        print(f"Sending '1' to Arduino for letter: {letter}")
                        arduino.write(b'1')
                        time.sleep(0.5)
            except Exception as e:
                print(f"Error processing frame {latest_frame}: {e}")

        time.sleep(1)  # Avoid excessive CPU usage

