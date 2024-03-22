import cv2
import sys
sys.path.append('voice')
from objectdetection.objdetect import detect_objects
from voice import *
sys.path.append('ocr')
from OCR import *
sys.path.append('objectdetection')
from objdetect import *


sys.path.append('facerec')
from reco import *

sys.path.append('../')
mode=3
count = 0
import time

def cam():
    global mode
    global count
    # Load Camera
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if count % 5 != 0:  # This condition is unnecessary now; we'll use sleep instead
            nm = "frame" + str(count) + ".jpg"
            cv2.imwrite(nm, frame)
            if mode == 1:
                recognise(nm)
            elif mode == 2:
                ocr(nm)
            elif mode == 3:
                # Object detection
                detect_objects(frame)
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key == 50:
            mode = 2
        elif key == 49:
            mode = 1
        elif key == 51:
            mode = 3
        elif key == 27:
            break
        time.sleep(.2)  # Wait for 1 seconds before capturing the next frame
        count += 1  # Increment count here, outside the if condition
    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    cam()
