import socketio

s = socketio.Client()

@s.on('connect', namespace='/robot')
def handleConnect():
    print('robot connection established')

@s.on('move', namespace = '/robot')
def handleMove(msg):
    print(msg['command'])
    success = 0
    if(success == 1):
        s.emit('result', {'re-id': '5678', 'status': 'successful'})
    else:
        s.emit('result', {'re-id': '5678', 'status': 'fail'})


s.connect('http://192.168.1.106:5000/robot', namespaces=['/robot'])
#s.wait()
