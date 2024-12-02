import serial
import time
from PIL import Image
import pytesseract
import os

# Replace 'COM3' with the port your Arduino is connected to (e.g., '/dev/ttyUSB0' on Linux or macOS)
arduino_port = 'COM5'
baud_rate = 9600

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\halon\OneDrive\KISD\5-semester\MIP\code\attachments\txtRecognition-papa.jpg"






# Establish the connection
try:
    print("Initializing serial connection...")
    arduino = serial.Serial(arduino_port, baud_rate)
    print("Serial connection established.")
    time.sleep(2)  # Wait for the connection to initialize
except Exception as e:
    print(f"Error initializing serial connection: {e}")




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
        print("OCR complete.")

        print("Recognized text:")
        print(recognized_text)


        recognized_text_list = list(recognized_text)

        for letters in recognized_text_list:
            print("Recognized letters:", letters)
            time.sleep(1)


        for letters in recognized_text_list:
            print(letters)
            if letters.isalpha():  # Only send alphabetic characters
                # Send each letter to Arduino
                arduino.write(letters.encode())  # Encode letter as byte and send it
                time.sleep(1)  # Wait a little to give Arduino time to process
        print("Finished sending letters.")
    except Exception as e:
        print(f"Error processing image: {e}")




        # letters to arduino, arduino then to pins

        # Check if any text is detected
        if recognized_text.strip():  # If text is not empty
            print("Text detected! Sending signal to Arduino...")
            arduino.write(b'1')  # Send '1' as a byte
            print("Signal sent!")
        else:
            print("No text detected.")
    except Exception as e:
        print(f"Error processing image: {e}")




try:
    process_image_and_send_signal(r"C:\Users\halon\OneDrive\KISD\5-semester\MIP\code\attachments\txtRecognition-papa.jpg")
except Exception as e:
    print(f"Error in script execution: {e}")
finally:
    if 'arduino' in locals():
        arduino.close()
        print("Serial connection closed.")
