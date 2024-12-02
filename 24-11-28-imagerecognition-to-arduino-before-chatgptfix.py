import serial
import time
from PIL import Image
import pytesseract
import os

# Replace 'COM5' with the port your Arduino is connected to
arduino_port = 'COM5'
baud_rate = 9600


class BraileConverter:
    def __init__ (self, character):
        self.character = character
        


# Braile Patterns

braille_patterns = {
    'A': 0b100000,  'B': 0b101000,  'C': 0b110000,  'D': 0b110100,  'E': 0b100100,
    'F': 0b111000,  'G': 0b111100,  'H': 0b101100,  'I': 0b011000,  'J': 0b011100,
    'K': 0b100010,  'L': 0b101010,  'M': 0b110010,  'N': 0b110110,  'O': 0b100110,
    'P': 0b111010,  'Q': 0b111110,  'R': 0b101110,  'S': 0b011010,  'T': 0b011110,
    'U': 0b100011,  'V': 0b101011,  'W': 0b011101,  'X': 0b110011,  'Y': 0b110111,
    'Z': 0b100111,
    '0': 0b011100,  '1': 0b100000,  '2': 0b101000,  '3': 0b110000,  '4': 0b110100,
    '5': 0b100100,  '6': 0b111000,  '7': 0b111100,  '8': 0b101100,  '9': 0b011000,
    ',': 0b010000,  ';': 0b011000,  ':': 0b011100,  '.': 0b001000,  '?': 0b011010,
    '!': 0b011001,  '\'': 0b001001, '\"': 0b001011, '(': 0b001111,  ')': 0b001110,
    '/': 0b001010
}

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
        for character in recognized_text_list:
            character = character.upper()
            print(character)
        if character in braille_patterns:
            braille_code = braille_patterns[character] # braille_code stores an individual character that is being sent to arduino

            print("Recognized letter:", character)
            print(f"Sending character {character} to Arduino:")
            arduino.write(bytes([braille_code]))  
            time.sleep(1)  # Wait for Arduino to process each letter (adjust if needed)

        else:
            print(f"Character '{character}' not recognized as Braille.")

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
