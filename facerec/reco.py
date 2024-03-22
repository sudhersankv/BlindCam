import face_recognition
import cv2
import os
import glob
import numpy as np
from simple_facerec import SimpleFacerec
import sys
sys.path.append('../voice')
from voice import *
sys.path.append('../')


sfr = SimpleFacerec()
sfr.load_encoding_images("facerec/images/")
#sys.path.append('../')
#print("abcd")
def recognise(frame):
    frame = cv2.imread(frame, cv2.IMREAD_COLOR)
    face_locations, names = sfr.detect_known_faces(frame)
    for name in names:
        #print(name)
        voice(name)
