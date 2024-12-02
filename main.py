from image_recognition import process_image_and_send_signal
from camerafeed import CameraFeed
from threading import Thread
import serial
import time
import logging



def main():
    # Initialize CameraFeed instance
    camera_feed = CameraFeed()

    # Start camera in a separate thread
    camera_thread = Thread(target=camera_feed.start_camera)
    camera_thread.start()

    # Process images in a separate thread
    process_thread = Thread(target=process_image_and_send_signal, args=(camera_feed,))
    process_thread.start()

    # Wait for threads to finish
    camera_thread.join()
    camera_feed.running = False
    process_thread.join()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error in script execution: {e}")
    finally:
        if 'arduino' in locals():
            arduino.close()
            print("Serial connection closed.")
