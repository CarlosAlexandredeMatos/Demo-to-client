import cv2 as cv

cap = cv.VideoCapture(0)
while True:
    key = cv.waitKey(1)
    ret, frame = cap.read()
    cv.imshow('CAMERA E3X', frame)

    if key == ord('q'):
        break
    elif key == ord('s'):
        roi = cv.selectROI('SELECIONAR TEMPLATE', frame)
        x, y, w, h = roi
        img = frame[y:y+h, x:x+w]
        cv.imwrite('template1.jpg', img)
        break

cap.release()
cv.destroyAllWindows()

    