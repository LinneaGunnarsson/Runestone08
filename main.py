from flask import Flask, render_template, request, Response
from flask_socketio import SocketIO, send
from cameraLaptop import Camera
import socket
import threading

app = Flask(__name__)

socketio = SocketIO(app)
button = 0

def talkToRobot(command):
	if (command == 'Up'):
		send('up pressed', broadcast=True)
	if (command == 'down'):
		send('down pressed', broadcast=True)
	if (command == 'right'):
		send('right pressed', bradcast=True)
	if (command == 'left'):
		send('left pressed', broadcast=True)



@socketio.on('message')
def handleMessage(msg):
	print('session id: ' + request.sid)
	print('Message: ' + msg)
	send(msg, broadcast=True)

@socketio.on('manual request')
def handleManualReq():
	global button
	if(button == 0):
		msg = " take control"
		button = request.sid
		send(msg, broadcast=True)
   
	elif (request.sid != button):
		send("Ocupied")
   
	else:
		send("released")
		button = 0


@socketio.on('up')
def handleUp():
	if (button == 0):
		msg = "need to take control first"
		send(msg, broadcast=True)
	else:
		send("up", broadcast=True)

@socketio.on('down')
def handleDown():
	if (button == 0):
		msg = "need to take control first"
		send(msg, broadcast=True)
	else:
		send("down", broadcast=True)

@socketio.on('left')
def handleLeft():
	if (button == 0):
		msg = "need to take control first"
		send(msg, broadcast=True)
	else:
		send("left", broadcast=True)

@socketio.on('right')
def handleRight():
	if (button == 0):
		msg = "need to take control first"
		send(msg, broadcast=True)
	else:
		send("right", broadcast=True)

@app.route('/')
def index():
	return render_template('index.html')

#TUTORIAL BORJAR HAR

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
	return Response(gen(Camera()),
		mimetype='multipart/x-mixed-replace; boundary=frame')
#TUTORIAL SLUTAR HAR

def hostSocket():
	#TESTAR MED SOCKET HÄR
	HOST = '192.168.1.106'
	PORT = 65432

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST,PORT))
		s.listen()
		conn, addr = s.accept()
		with conn:
			print('Connected by', addr)
			while True:
				data = conn.recv(1024)
				if not data:
					break
				conn.sendall(data)
#SLUTAR TESTA MED SOCKET HÄR

def hostFlask(arbitrary):
	socketio.run(app, host = "192.168.1.106")

if __name__ == '__main__':
	socketio.run(app, host = "130.243.212.217")



