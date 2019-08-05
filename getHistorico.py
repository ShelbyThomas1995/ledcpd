import sys

if __name__ == '__main__':

    idrack = sys.argv[1]
    list = [line.rstrip('\n') for line in open("/var/www/html/logLedHistorico.txt")]

    list2 = []

    for i in list:
	aux = i.split(',')

	if aux[0] == idrack:
	  cont = 0
	  for j in aux:
              if cont == 0:
		new = "ID Rack: " + j
		#print new
		list2.append(new)
	      elif cont == 1:
		new = "Modo: " + j
		#print new
		list2.append(new)
	      elif cont == 2:
		new = "Fecha: " + j
		#print new
		list2.append(new)
              elif cont == 3:
		new = "Hora: " + j
		#print new
		list2.append(new)
	      elif cont == 4:
		new = "Info: " + j
		#print new
		list2.append(new)
		#newLinea =  "____________________"
		#print newLinea
		#list2.append(newLinea)
              cont = cont + 1

    print list2



