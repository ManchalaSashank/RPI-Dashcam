from picamera2 import Picamera2
from datetime import datetime
import os
import time

# Set your USB mount path
USB_PATH = "/media/usb"

# Create a new folder for today's date if it doesn't exist
def get_today_folder():
    date_folder = os.path.join(USB_PATH, datetime.now().strftime('%Y-%m-%d'))
    os.makedirs(date_folder, exist_ok=True)
    return date_folder

# Start continuous video recording
def start_continuous_recording():
    # Setup PiCamera
    picam2 = Picamera2()
    video_config = picam2.create_video_configuration(main={"size": (1280, 720)})
    picam2.configure(video_config)

    # Create video file path
    folder = get_today_folder()
    filename = datetime.now().strftime('continuous_%H-%M.h264')
    filepath = os.path.join(folder, filename)

    # Start recording
    picam2.start()
    picam2.start_recording(filepath)
    print(f"Recording started: {filepath}")

    try:
        while True:
            time.sleep(1) 
    except KeyboardInterrupt:
        print("Recording stopped by user.")
    finally:
        picam2.stop_recording()
        print(f"Video saved to: {filepath}")

if __name__ == "__main__":
    start_continuous_recording()
