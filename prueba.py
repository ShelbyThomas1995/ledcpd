import time
from neopixel import *
import argparse
import sys
import os

# LED strip configuration:
LED_COUNT      = 61       # Number of LED pixels.
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Pines disponibles para LEDs
#LED_PIN       = 18
LED_PIN        = 12 #(Grupo 1: rack0, rack1, rack2, rack3)
#LED_PIN       = 21
LED_CHANNEL    = 0

#LED_PIN       = 19
#LED_PIN       = 13
#LED_CHANNEL   = 1

def printLed(idRack, mode, led):

	aux = idRack.split("rack")
	if aux[1] == '0':
          i1 = 0
          i2 = 30
        elif aux[1] == '1':
          i1 = 30
          i2 = 60
        elif aux[1] == '2':
          i1 = 60
          i2 = 90
	elif aux[1] == '3':
	  i1 = 90
	  i2 = 120

	if mode == "on":
	  for i in range(i1,i2):
	    led.setPixelColor(i, Color(0,0,255))
	elif mode == "off":
	 for i in range(i1,i2):
            led.setPixelColor(i , Color(0,0,0))
	elif mode == "error":
	 for i in range(i1,i2):
            led.setPixelColor(i , Color(0,255,0))
	elif mode == "tecnico":
	 for i in range(i1,i2):
            led.setPixelColor(i , Color(255,255,255))

        led.setBrightness(85)
	led.show()

def updateLogEstados(file, check, size, update):
	with open(file, "r") as f:
	  lines = (line.rstrip() for line in f)
	  altered_lines = [update if line[:size] == check else line for line in lines]

	with open(file, "w") as f:
	  f.write('\n'.join(altered_lines)+'\n')

def updateLogHistorico(file, update):
	f = open(file, "a")
	f.write(update)
	f.close

if __name__ == '__main__':

    strip = Adafruit_NeoPixel(600, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    list = [line.rstrip('\n') for line in open("/var/www/html/logLedEstados.txt")]

    for i in list:
	if i != "end":
	  aux = i.split(' ')
	  printLed(aux[0], aux[1], strip)

    idrack = sys.argv[1]
    mode = sys.argv[2]
    fecha = sys.argv[3]
    hora = sys.argv[4]
    infoaux = sys.argv[5]
    info = infoaux.replace('*',' ')
    duracion = sys.argv[6]
    fechaT = sys.argv[7]
    horaT = sys.argv[8]

    if mode == "tecnico":
	infoA = "Entrada de tecnico con fecha: " + fechaT + " " + horaT
        logHistorico = idrack + "," + mode + "," + fecha + "," + hora + "," + infoA + "\n"
        os.system("sudo python /var/www/html/tecnico.py " + idrack + " " + mode + " " + fecha + " " + hora  + " " + duracion + " " + fechaT + " " + horaT)
    else:
	logHistorico = idrack + "," + mode + "," + fecha + "," + hora + "," + info + "\n"
	printLed(idrack, mode, strip)


    updateLogEstados("/var/www/html/logLedEstados.txt",idrack,len(idrack),idrack+" "+mode)
    updateLogHistorico("/var/www/html/logLedHistorico.txt",logHistorico)
    f = open("/var/www/html/logLedEstados.txt")
    list = [line.rstrip('\n') for line in open("/var/www/html/logLedEstados.txt")]
