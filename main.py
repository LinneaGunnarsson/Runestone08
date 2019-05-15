from flask import Flask, render_template, request, Response
from flask_socketio import SocketIO, send
from cameraLaptop import Camera

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

@socketio.on('connect', namespace='/robot')
def handleRobotConnect():
	#TODO: Add another robot to database or Robot array
	print('Another robot joins the warehouse!')

@socketio.on('disconnect', namespace='/robot')
def handleRobotDisconnect():
	#TODO: Remove robot from database or Robot array
	print('Another robot leaves the warehouse!')

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
		send("Occupied")
   
	else:
		send("released")
		button = 0


@socketio.on('command')
def handleCommand(msg):
	if(button == 0):
		msg = "need to take control first"
		send(msg, broadcast=True)
		return

	c = msg['command']
	#TODO: If move commands: Can robot move without colliding with robots or warehouse walls?
	# If pick up: It it already holding something?
	# If drop: Is it holding something?
	socketio.emit('move', {'id' : '1234', 'command' : c}, namespace= '/robot')
	send(c, broadcast=True)

	while True:
		@socketio.on('result')
		def handleResult(msg):
			send(msg['status'], broadcast=True)
		break


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

@socketio.on('down')
def handleDown():
	if (button == 0):
		msg = "need to take control first"
		send(msg, broadcast=True)
	else:
		send("down", broadcast=True)

if __name__ == '__main__':
	socketio.run(app, host = "192.168.1.69", debug = True)

'''
@socketio.on('straight')
def handleUp():
	if (button == 0):
		msg = "need to take control first"
		send(msg, broadcast=True)
	else:
		socketio.emit('move', {'id' : '1234', 'command' : 'move-straight'}, namespace= '/robot')
		send("move-straight", broadcast=True)

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
		socketio.emit('move', {'id' : '1234', 'command' : 'move-left'}, namespace= '/robot')
		send("move-left", broadcast=True)

@socketio.on('right')
def handleRight():
	if (button == 0):
		msg = "need to take control first"
		send(msg, broadcast=True)
		return
	else:
		socketio.emit('move', {'id' : '1234', 'command' : 'move-right'}, namespace= '/robot')
		send("move-right", broadcast=True)
	
@socketio.on('pick up')
def handlePickUp():
	if(button == 0):
		msg = "need to take control first"
		send(msg, broadcast=True)
	else:
		socketio.emit('move', {'id' : '1234', 'command' : 'pick-object'}, namespace= '/robot')

@socketio.on('drop')
def handleDrop():
	if(button == 0):
		msg = "need to take control first"
		send(msg, broadcast=True)
	else:
		socketio.emit('move', {'id' : '1234', 'command' : 'drop-object'}, namespace= '/robot')
'''

