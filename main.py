from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
from datetime import datetime
import os

# Directory to store the video
VIDEO_DIR = "/home/pi/videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

# Filename with timestamp
timestamp = datetime.now().strftime("vid_%Y-%m-%d_%H-%M.h264")
output_path = os.path.join(VIDEO_DIR, timestamp)

# Setup camera
picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (1280, 720), "format": "YUV420"}, controls={"FrameRate": 30})
picam2.configure(video_config)

# Start recording
encoder = H264Encoder(bitrate=3000000)
output = FileOutput(output_path)
picam2.start_recording(encoder, output)
print(f"🎬 Continuous recording started: {output_path}")

# Keep running forever until manually stopped
try:
    while True:
        pass  # idle loop — the camera keeps recording
except KeyboardInterrupt:
    pass
finally:
    picam2.stop_recording()
    print(f"Recording stopped and saved: {output_path}")
