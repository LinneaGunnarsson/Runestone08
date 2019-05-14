import socketio
from time import time
from camera import Camera

s = socketio.Client()
camera = Camera()

@s.on('connect', namespace='/camera')
def handleConnect():
    print('Camera connection established')

@s.on('send img', namespace='/camera')
def handleImg():
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
            		b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

s.connect('http://192.168.1.106:5000/robot', namespaces=['/camera'])