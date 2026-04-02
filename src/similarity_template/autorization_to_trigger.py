import cv2 as cv


def template_scanner(frame):
    template = cv.imread('template1.jpg')
    threshold = 0.85


    resultado = cv.matchTemplate(frame, template, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(resultado)

    if max_val >= threshold:
        cv.imshow('IA DISPARO', frame)
        
        return True

    