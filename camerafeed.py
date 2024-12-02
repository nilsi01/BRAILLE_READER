import os
import cv2
import time
from pathlib import Path

def use_webcam(save_directory="captured_frames", save_interval=1, max_frames=100):
    """
    Continuously captures frames from the webcam and saves them automatically.
    Automatically deletes older frames when the limit is exceeded.

    Parameters:
        save_directory (str): Directory to save captured frames.
        save_interval (int): Interval in seconds between saving frames.
        max_frames (int): Maximum number of frames to keep in the directory.
    """
    # Ensure the save directory exists
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Initialize the webcam (default is usually 0, but can vary)
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # Change the port if you have problems recognizing the camera

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        return

    print("Press 'q' to stop capturing and exit.")

    frame_count = 0
    last_save_time = time.time()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame reading is unsuccessful, break the loop
        if not ret:
            print("Error: Unable to read frame from webcam.")
            break

        # Display the captured frame
        cv2.imshow("Webcam Feed", frame)

        # Save frame automatically at specified intervals
        current_time = time.time()
        if current_time - last_save_time >= save_interval:
            frame_filename = os.path.join(save_directory, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Automatically saved frame as: {frame_filename}")
            frame_count += 1
            last_save_time = current_time

            # Perform cleanup if the number of files exceeds the maximum allowed
            cleanup_old_files(save_directory, max_frames)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


def cleanup_old_files(directory, max_files):
    """
    Deletes the oldest files in a directory if the number exceeds max_files.

    Parameters:
        directory (str): Directory to monitor for cleanup.
        max_files (int): Maximum number of files to keep in the directory.
    """
    files = list(Path(directory).glob("*.jpg"))  # Get all .jpg files in the directory
    if len(files) > max_files:
        # Sort files by modification time (oldest first)
        files.sort(key=lambda f: f.stat().st_mtime)
        # Delete the oldest files to keep the count within the limit
        files_to_delete = files[:len(files) - max_files]
        for file in files_to_delete:
            try:
                file.unlink()  # Delete the file
                print(f"Deleted old file: {file}")
            except Exception as e:
                print(f"Error deleting file {file}: {e}")


if __name__ == "__main__":
    use_webcam()
