import numpy as np
import cv2
import time


class Camera(object):

    def __init__(self):
        self.camera = cv2.VideoCapture(0)


    def get_frame(self):
        while(True):
            tmp, frame = self.camera.read()

            yield cv2.imencode('.jpg', frame)[1].tobytes()
    # cv2.imshow('frame',frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break


        self.camera.release()
