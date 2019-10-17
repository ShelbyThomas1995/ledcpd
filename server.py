import socket
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('192.168.40.16',10000)
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
	  if data:
	    aux = data.split(',')
	    aux2 = aux[2].split(" ")
	    fecha = aux2[0]

	    hora = aux2[1]
	    lenhora = len(aux2[1])

	    comando = "sudo python /var/www/html/prueba.py" + " " + aux[0] + " " + aux[1] + " " + fecha  + " " + hora[:lenhora-3] + " " + aux[3]
	    print comando
	    os.system(comando)
            print >> sys.stderr, 'Enviando confirmacion de socket...'
            connection.sendall("Socket recibido!")
	  else:
	    print >> sys.stderr, 'No hay mas datos que mostrar...'
	    break
  finally:
	connection.close()
