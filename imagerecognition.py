import os
import serial
import time
from PIL import Image
import pytesseract
import camerafeed  # Importing the webcam module

# Replace 'COM5' with the port your Arduino is connected to
arduino_port = 'COM5'
baud_rate = 9600

# Path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize Arduino connection
try:
    print("Initializing serial connection...")
    arduino = serial.Serial(arduino_port, baud_rate)
    print("Serial connection established.")
    time.sleep(2)  # Wait for the connection to initialize
except Exception as e:
    print(f"Error initializing serial connection: {e}")
    exit()  # Exit the script if Arduino connection fails


def process_image_and_send_signal(save_directory):
    try:
        print(f"Checking if image exists: {save_directory}")
        if not os.path.exists(save_directory):
            print("Image file does not exist!")
            return

        print(f"Opening image: {save_directory}")
        image = Image.open(save_directory)

        print("Performing OCR...")
        recognized_text = pytesseract.image_to_string(image)
        print("OCR complete.")
        print("Recognized text:", recognized_text)

        recognized_text_list = list(recognized_text)

        # Send a signal for each recognized alphabetic character
        for letter in recognized_text_list:
            if letter.isalpha():  # Only process alphabetic characters
                print(f"Sending: {letter} to Arduino")
                arduino.write(b'1')  # Send '1' byte to Arduino to activate pin
                time.sleep(1)  # Wait for Arduino to process each letter (adjust if needed)

        print("Finished sending letters.")
    except Exception as e:
        print(f"Error processing image: {e}")


def main():
    # Run the webcam to capture images
    print("Starting webcam feed...")
    camerafeed.use_webcam()

    # Process saved frames
    save_directory = "captured_frames"
    if os.path.exists(save_directory):
        images = [os.path.join(save_directory, f) for f in os.listdir(save_directory) if f.endswith('.jpg')]
        if images:
            print(f"Processing {len(images)} captured images...")
            for img_path in images:
                process_image_and_send_signal(img_path)
        else:
            print("No images to process.")
    else:
        print("No captured frames found.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error in script execution: {e}")
    finally:
        if 'arduino' in locals():
            arduino.close()
            print("Serial connection closed.")
