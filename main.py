from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

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
if __name__ == '__main__':
	socketio.run(app, host = "130.243.228.9")


