import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)

green_lower = np.array([40, 40, 40])
green_upper = np.array([70, 255,255])
pink_lower = np.array([150, 150, 150])
pink_upper = np.array([170, 255, 255])
prev_y1 = 0
prev_y2 = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Scrolling down
    mask_1 = cv2.inRange(hsv, green_lower, green_upper)
    contours_1, hierarchy_1 = cv2.findContours(mask_1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Scrolling up
    mask_2 = cv2.inRange(hsv, pink_lower, pink_upper)
    contours_2, hierarchy_2 = cv2.findContours(mask_2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours_1:
        area_1 = cv2.contourArea(c)
        if area_1 > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if y < prev_y1:
                pyautogui.press('down')

            prev_y1 = y

    for c in contours_2:
        area_2 = cv2.contourArea(c)
        if area_2 > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if y < prev_y2:
                pyautogui.press('up')

            prev_y2 = y
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
