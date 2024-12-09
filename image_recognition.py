import os
import time
import logging
from PIL import Image
import pytesseract
from threading import Thread
from camerafeed import CameraFeed
import serial


# Replace 'COM5' with the port your Arduino is connected to
arduino_port = 'COM5'
baud_rate = 9600

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize Arduino
try:
    logging.info("Initializing serial connection...")
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    logging.info("Serial connection established.")
    time.sleep(2)
except Exception as e:
    logging.error(f"Error initializing serial connection: {e}")
    exit()


def send_to_arduino(letter):
    """
    Send a letter to the Arduino via serial communication.
    :param letter: Single alphabetic character to send.
    """
    try:
            arduino.write(letter.upper().encode('utf-8'))
            logging.info(f"Sent letter '{letter}' to Arduino.")
            time.sleep(0.5)  # Delay to allow Arduino to process
    except Exception as e:
            logging.error(f"Error sending letter '{letter}' to Arduino: {e}")


def process_image_and_send_signal(camera_feed):
    """ Continuously process the latest frame and send signals to Arduino. """
    while camera_feed.running:
        latest_frame = None
        with camera_feed.frame_lock:
            latest_frame = camera_feed.latest_frame

        if latest_frame:
            try:
                logging.info(f"Processing latest frame: {latest_frame}")

                # Open the image, convert to grayscale, and perform OCR
                image = Image.open(latest_frame).convert("L")
                recognized_text = pytesseract.image_to_string(image)

                print("Recognized Text:", recognized_text)

                # Send each recognized alphabetic character to Arduino
                for letter in recognized_text:
                    send_to_arduino(letter)

            except Exception as e:
                logging.error(f"Error processing frame {latest_frame}: {e}")

        time.sleep(1)  # Avoid excessive CPU usage
