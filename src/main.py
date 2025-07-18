import cv2
import math
import time
from ultralytics import YOLO
from utils import publish_presence
from config import MESSAGE_INTERVAL_SECONDS, YOLO_CLASS_NAMES

model = YOLO('yolo-Weights/yolov10x.pt')

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)


last_presence = False
last_publish_time = 0

while True:
    ret, img = cam.read()
    if not ret:
        print("Error: can note read camera.")
        break

    people_count = 0
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence =>", confidence)

            cls = int(box.cls[0])
            print("Class name =>", YOLO_CLASS_NAMES[cls])

            if YOLO_CLASS_NAMES[cls] == "person":
                people_count += 1

            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, YOLO_CLASS_NAMES[cls], org,
                        font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

    current_time = time.time()
    presence = people_count > 0

    should_publish = False

    if presence != last_presence:
        should_publish = True
        print("==> State change")
    elif presence and (current_time - last_publish_time) > MESSAGE_INTERVAL_SECONDS:
        should_publish = True
    else:
        should_publish = False

    if should_publish:
        publish_presence(presence, people_count)
        last_publish_time = current_time
        last_presence = presence

cam.release()
cv2.destroyAllWindows()
