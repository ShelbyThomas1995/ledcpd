import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.40.16', 10000)
print >>sys.stderr, 'Connecting to %s port %s' % server_address
sock.connect(server_address)


    # Send data
skt = raw_input("PANDORA: Introduce socket: ")
print >>sys.stderr, 'Enviando a Raspberry: "%s"' % skt
sock.sendall(skt)
sock.close()



"""
    # Look for the response
amount_received = 0
amount_expected = len(skt)

while amount_received < amount_expected:
  data = sock.recv(16)
  amount_received += len(data)
  print >>sys.stderr, 'Recibido: "%s"' % data
"""
