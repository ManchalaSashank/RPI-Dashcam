import os
import shutil

SOURCE_DIR = "/home/pi/videos"
USB_PATH = "/media/usb"

if os.path.ismount(USB_PATH):
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".h264"):
            src = os.path.join(SOURCE_DIR, filename)
            dst = os.path.join(USB_PATH, filename)
            shutil.copy2(src, dst)
            os.remove(src)
            print(f"Moved: {filename}")
else:
    print("USB not mounted.")
