import os
import cv2
from PIL import ImageEnhance
import time
import log_config
from pathlib import Path
from threading import Thread, Lock
import logging



class CameraFeed:
    def __init__(self, save_directory="captured_frames", save_interval=3, max_frames=100, contrast = 0, greyscale = True):
        self.save_directory = save_directory
        self.save_interval = save_interval
        self.max_frames = max_frames
        self.frame_lock = Lock()
        self.latest_frame = None
        self.running = True
        self.contrast = 1.5
        self.greyscale = True

        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

    def start_camera(self):
        # Initialize webcam
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) # Change the port if needed 

        if not cap.isOpened():
            logging.error("Error: Unable to access the webcam.")
            return

        logging.info("Press 'q' to stop capturing and exit.")
        last_save_time = time.time()

        while self.running:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



            if not ret:
                logging.error("Error: Unable to read frame from webcam.")
                break

            # Display the frame
            cv2.imshow("Webcam Feed", cap_gray_contrast)

            # Save frame at specified intervals
            current_time = time.time()
            if current_time - last_save_time >= self.save_interval:
                frame_filename = os.path.join(self.save_directory, f"frame_{int(current_time)}.jpg")
                cv2.imwrite(frame_filename, frame)
                logging.info(f"Automatically saved frame: {frame_filename}")

                # Update the latest frame
                with self.frame_lock:
                    self.latest_frame = frame_filename

                last_save_time = current_time

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
