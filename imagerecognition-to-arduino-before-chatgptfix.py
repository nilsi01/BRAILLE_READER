import serial
import time
from PIL import Image
import pytesseract
import os

# Replace 'COM5' with the port your Arduino is connected to
arduino_port = 'COM5'
baud_rate = 9600

# Path to Tesseract and image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\halon\OneDrive\KISD\5-semester\MIP\code\attachments\txtRecognition-papa.jpg"

# Establish the connection to Arduino
try:
    print("Initializing serial connection...")
    arduino = serial.Serial(arduino_port, baud_rate)
    print("Serial connection established.")
    time.sleep(2)  # Wait for the connection to initialize
except Exception as e:
    print(f"Error initializing serial connection: {e}")
    exit()  # Exit the script if Arduino connection fails





def process_image_and_send_signal(image_path):
    try:
        print(f"Checking if image exists: {image_path}")
        if not os.path.exists(image_path):
            print("Image file does not exist!")
            return

        print(f"Opening image: {image_path}")
        image = Image.open(image_path)

        print("Performing OCR...")
        recognized_text = pytesseract.image_to_string(image)
        time.sleep(1)


        print("OCR complete.")

        time.sleep(2)

        print("Recognized text:", {recognized_text})

        recognized_text_list = list(recognized_text)

        # Send a signal for each recognized alphabetic character
        for letter in recognized_text_list:
            print("Recognized letter:", letter)
            if letter.isalpha():  # Only process alphabetic characters
                print(f"Sending '1' to Arduino for letter: {letter}")
                arduino.write(b'1')  # Send '1' byte to Arduino to activate pin
                time.sleep(1)  # Wait for Arduino to process each letter (adjust if needed)

        print("Finished sending letters.")
    except Exception as e:
        print(f"Error processing image: {e}")




# Run the process
try:
    process_image_and_send_signal(image_path)
except Exception as e:
    print(f"Error in script execution: {e}")
finally:
    if 'arduino' in locals():
        arduino.close()
        print("Serial connection closed.")
