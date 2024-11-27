import cv2
import serial

# Initialize serial communication
arduino = serial.Serial('COM3', 9600)

# Initialize camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use Haarcascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cx, cy = x + w // 2, y + h // 2
        frame_height, frame_width = frame.shape[:2]

        pan_angle = int((cx / frame_width) * 180)
        tilt_angle = int((cy / frame_height) * 180)

        # Send angles to Arduino
        arduino.write(f"{pan_angle},{tilt_angle}\n".encode())

        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Face Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

