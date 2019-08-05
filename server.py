import socket
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost',10000)
#print >> sys.stderr, ' on %s in port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
  print >> sys.stderr, 'Esperando socket de Pandora....'
  connection, client_address = sock.accept()
  # Receive the data
  try:
	print >> sys.stderr, 'Conexion de: ', client_address
	while True:

          data = connection.recv(150)
	  print >> sys.stderr, 'Socket recibido: "%s"' % data
	  print data

	  if data:
	    aux = data.split(',')
            info = aux[4].replace(' ','*')
	    comando = "sudo python /var/www/html/prueba.py" + " " + aux[0] + " " + aux[1] + " " + aux[2] + " " + aux[3] + " " + info
	    os.system(comando)
            print >> sys.stderr, 'Enviando confirmacion de socket...'
            connection.sendall("Socket recibido!")
	  else:
	    print >> sys.stderr, 'No hay mas datos que mostrar...'
	    break
  finally:
	connection.close()
