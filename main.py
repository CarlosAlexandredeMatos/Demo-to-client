# import cv2 as cv

# from src.open_camera.opening_camera import open_camera
# from src.trigger_camera.template_scan import template_scanner


# cap = open_camera()

# while True:
#     key = cv.waitKey(1)
#     ret, frame = cap.read()
#     cv.imshow('Camera E3X', frame)

#     scanner_1 = template_scanner(frame)

#     if key == ord('q'):
#         break
        

import cv2 as cv
import time

from src.open_camera.opening_camera import open_camera
from src.trigger_camera.template_scan import template_scanner

cap = open_camera()

cooldown = 3  # segundos
last_detection_time = 0

while True:
    key = cv.waitKey(1)
    ret, frame = cap.read()

    if not ret:
        break

    current_time = time.time()

    # Só roda o scanner se já passou o cooldown
    if current_time - last_detection_time > cooldown:
        detected = template_scanner(frame)

        if detected:
            print("Template detectado!")
            cv.imshow('Inspeção', frame)

            # atualiza o tempo do último disparo
            last_detection_time = current_time

    cv.imshow('Camera E3X', frame)

    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()