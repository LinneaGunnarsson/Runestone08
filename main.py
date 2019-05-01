from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

button = null

@socketio.on('message')
def handleMessage(msg):
	print('session id: ' + request.sid)
	print('Message: ' + msg)
	send(msg, broadcast=True)

@socketio.on('manual request')
def handleManualReq():
	send('take control', broadcast=True)

@app.route('/')
def index():
	return render_template('index.html')
if __name__ == '__main__':
	socketio.run(app, host = "192.168.1.106")