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
        s.emit('result', {'re-id': msg['id'], 'status': 'successful'})
    else:
        s.emit('result', {'re-id': msg['id'], 'status': 'fail'})


s.connect('http://130.243.235.165:5000/robot', namespaces=['/robot'])
s.wait()
