import socketio

s = socketio.Client()

@s.on('connect')
def handleConnect():
    print('connection established')

@s.on('move', namespace = '/robot')
def handleMove(msg):
    print("hej ")

s.connect('http://192.168.1.106:5000/robot')
s.wait()