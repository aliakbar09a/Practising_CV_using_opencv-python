import numpy as np
import cv2

cap = cv2.VideoCapture(0)

four = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',four,15.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
out.release()
cap.release()
cv2.destroyAllWindows()


