import torch
import cv2
import time
import numpy as np
import serial
from ultralytics import YOLO

ArduinoSerial = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1)
time.sleep(1)

model = YOLO("best.pt")

torch.cuda.set_device(0)

def resize_frame(frame):
    resized_frame = cv2.resize(frame, (128, 96))
    return resized_frame

def apply_deepisp(frame):
    image_np = np.array(frame)
    brightness = 20
    contrast = 1.5
    enhanced_image = cv2.convertScaleAbs(image_np, alpha=contrast, beta=brightness)
    return np.array(enhanced_image)

cap = cv2.VideoCapture(0)

# for detection
first_class_id = None
second_class_id = None

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    resized = resize_frame(frame)

    flip = cv2.flip(resized, 1) #Flip horizontal

    deepisp_frame = apply_deepisp(flip)

    results = model.predict(deepisp_frame, conf=0.7, show=True)

    for result in results:
        for class_id in result.boxes.cls:
            if first_class_id is None:
                first_class_id = class_id
            else:
                second_class_id = class_id
                if first_class_id == second_class_id:
                        ArduinoSerial.write(chr(int(class_id)).encode())
                first_class_id = None
                second_class_id = None

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
