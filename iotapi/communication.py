import socket

def forward_action(device):
	op = device.currentOp()

	try:
		send(device.ipAddress, op)
		device.passOp()
	except Exception as e:
		print('DEU RUIM', e)

def send(dest, msg):
	print('Sending', msg, 'to', dest)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect(('' + dest, 80))
		s.sendall(msg.encode('utf-8'))
		_ = s.recv(1024)
