Python Script for Face Tracking with Arduino

This Python script enables real-time face detection using OpenCV and sends angle data to an Arduino to control servo motors for a face-tracking gimbal.

Features

Real-time Face Detection: Uses OpenCV to locate faces in the video feed.
Servo Angle Control: Calculates pan and tilt angles and sends them to the Arduino via serial communication.
Customizable: Adjust detection sensitivity, camera input, and communication settings.
Requirements

Hardware
Arduino Uno (preloaded with servo control code)
MG996R Servos (for pan and tilt)
Camera (USB or Laptop Webcam)
Software
Python 3.x


Installation

Clone the repository:
git clone https://github.com/your-username/face-tracking-gimbal.git
cd face-tracking-gimbal/Python


pip install opencv-python pyserial

Connect the Arduino to your computer and upload the Arduino/face_tracking_gimbal.ino code from this repository.



Usage

Ensure all hardware is connected as described in the main README.
Run the Python script:

python face_detection.py

Observe the servo movements as the camera tracks detected faces.

Configuration Options

Serial Port:
Update the following line in face_detection.py with the appropriate port:

arduino = serial.Serial('COM3', 9600)

Replace COM3 with the correct port (e.g., /dev/ttyUSB0 for Linux/Mac).

Camera Input:
Change the camera source if necessary:
cap = cv2.VideoCapture(0)

Replace 0 with 1 or higher for an external camera.

Code Overview

Face Detection: Uses OpenCV's Haarcascade to detect faces in the video feed.
Angle Mapping: Converts face coordinates into servo angles (0°–180°) based on the camera's resolution.
Serial Communication: Sends angles to the Arduino as a comma-separated string (pan_angle,tilt_angle\n).


Troubleshooting

No Face Detected:
Ensure proper lighting and camera focus.
Confirm the Haarcascade XML file path is correct.
Servo Motors Not Moving:
Verify the Arduino COM port.
Test servos with standalone Arduino sketches.
Camera Not Detected:
Ensure the camera is connected and accessible.
Try changing the camera index.

