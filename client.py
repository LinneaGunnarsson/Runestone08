import socketio

s = socketio.Client()

@s.on('connect', namespace='/robot')
def handleConnect():
    print('robot connection established')

@s.on('move', namespace = '/robot')
def handleMove(msg):
    print(msg['command'])
    success = 1
    if(success == 1):
        s.emit('result', {'re-id': msg['id'], 'status': 'successful'})
    else:
        s.emit('result', {'re-id': msg['id'], 'status': 'fail'})


s.connect('http://192.168.1.106:5000/robot', namespaces=['/robot'])
s.wait()
