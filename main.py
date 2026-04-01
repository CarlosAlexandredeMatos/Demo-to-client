import cv2 as cv
from src.open_camera.opening_camera import open_camera


cap = open_camera()

while True:
    key = cv.waitKey(1)
    ret, frame = cap.read()
    cv.imshow('Camera E3X', frame)

    if key == ord('s'):
        cv.imshow('Inspeção', frame)
        

    elif key == ord('q'):
        break
        
    