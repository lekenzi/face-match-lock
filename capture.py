import cv2
import time
def cap():
    name=str(time.time())
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        #cv2.imshow(name,image)
        cv2.imwrite(name+".png", image)
        # cv2.waitKey(0)
        #cv2.destroyWindow(name)
    return name
# this is for mac support
