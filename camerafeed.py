import os
import cv2
from PIL import ImageEnhance
import time
import log_config
from pathlib import Path
from threading import Thread, Lock
import logging
import serial



class CameraFeed:
    def __init__(self, save_directory="captured_frames", max_frames=100, contrast=0, greyscale=True, serial_port="COM5", baud_rate=9600):
        self.save_directory = save_directory
        self.max_frames = max_frames
        self.contrast = 1.5
        self.greyscale = True
        self.running = True

        # # Set up serial communication
        # self.serial_port = serial.Serial(serial_port, baud_rate, timeout=1)

        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

    def start_camera(self):
        # Initialize webcam
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Change the port if needed

        if not cap.isOpened():
            logging.error("Error: Unable to access the webcam.")
            return

        logging.info("Press 'q' to stop capturing and exit.")
        
        while self.running:
            # Read a frame from the webcam
            ret, frame = cap.read()
            if not ret:
                logging.error("Error: Unable to read frame from webcam.")
                break

            # Convert frame to grayscale if enabled
            if self.greyscale:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the frame
            cv2.imshow("Webcam Feed", frame)

            # Check serial input for "Pressed"
            if self.serial_port.in_waiting > 0:
                line = self.serial_port.readline().decode('utf-8').strip()
                if line == "Pressed":
                    # Save the frame when the button is pressed
                    timestamp = int(time.time())
                    frame_filename = os.path.join(self.save_directory, f"frame_{timestamp}.jpg")
                    cv2.imwrite(frame_filename, frame)
                    logging.info(f"Saved frame: {frame_filename}")

                    # Clean up old files
                    self.cleanup_old_files()

            # Exit loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.running = False

        cap.release()
        cv2.destroyAllWindows()

    def cleanup_old_files(self):
        files = list(Path(self.save_directory).glob("*.jpg"))
        if len(files) > self.max_frames:
            files.sort(key=lambda f: f.stat().st_mtime)
            for file in files[:len(files) - self.max_frames]:
                try:
                    file.unlink()
                    logging.info(f"Deleted old file: {file}")
                except Exception as e:
                    logging.error(f"Error deleting file {file}: {e}")