import serial

try:
    ser = serial.Serial('COM5', 9600, timeout=1)
    print("Serial port opened successfully.")
    ser.close()
except Exception as e:
    print(f"Error: {e}")