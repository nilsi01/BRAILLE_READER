import serial
import time

from PIL import Image
import pytesseract

# Replace 'COM3' with the port your Arduino is connected to (e.g., '/dev/ttyUSB0' on Linux or macOS)
arduino_port = 'COM5'
baud_rate = 9600

# Establish the connection
arduino = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Wait for the connection to initialize

# Send data
try:
    while True:
        user_input = input("Enter '1' to turn on, '0' to turn off: ")
        if user_input in ['0', '1']:
            arduino.write(user_input.encode())  # Send data to Arduino
        else:
            print("Invalid input. Please enter '0' or '1'.")
except KeyboardInterrupt:
    print("Exiting...")

# Close the connection
arduino.close()
