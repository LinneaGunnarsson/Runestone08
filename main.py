from flask import Flask, render_template, request, Response
from flask_socketio import SocketIO, send
from cameraLaptop import Camera

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
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
	talkToRobot(msg)

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


@app.route('/')
def index():
	return render_template('index.html')

#TUTORIAL BÖRJAR HÄR

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
	return Response(gen(Camera()),
		mimetype='multipart/x-mixed-replace; boundary=frame')
#TUTORIAL SLUTAR HÄR


if __name__ == '__main__':
	socketio.run(app, host = "192.168.1.39")


