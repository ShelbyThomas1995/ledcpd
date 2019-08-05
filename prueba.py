import time
from neopixel import *
import argparse
import sys
import os

# LED strip configuration:
LED_COUNT      = 3      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def printLed(idRack, mode, led):
	if mode == "on":
	  led.setPixelColor(int(idRack[4:]), Color(0,0,255))
	elif mode == "off":
	  led.setPixelColor(int(idRack[4:]), Color(0,0,0))
	elif mode == "error":
	  led.setPixelColor(int(idRack[4:]), Color(0,255,0))
	elif mode == "tecnico":
	  led.setPixelColor(int(idRack[4:]), Color(255,255,255))

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
    strip = Adafruit_NeoPixel(3, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    print "INFO: Consultando log de estados..."
    list = [line.rstrip('\n') for line in open("/var/www/html/logLedEstados.txt")]
    print list

    print "Iniciando leds..."
    for i in list:
	if i != "end":
	  aux = i.split(' ')
	  printLed(aux[0], aux[1], strip)


    #idrack, mode, fecha, hora, rest = sys.argv.split(maxsplit=4)
    idrack = sys.argv[1]
    mode = sys.argv[2]
    fecha = sys.argv[3]
    hora = sys.argv[4]
    infoaux = sys.argv[5]
    info = infoaux.replace('*',' ')

    logHistorico = idrack + "," + mode + "," + fecha + "," + hora + "," + info + "\n"

    print logHistorico
    printLed(idrack, mode, strip)
    print "INFO: Actualizando log de estados..."
    updateLogEstados("/var/www/html/logLedEstados.txt",idrack,len(idrack),idrack+" "+mode)
    updateLogHistorico("/var/www/html/logLedHistorico.txt",logHistorico)
    f = open("/var/www/html/logLedEstados.txt")
    list = [line.rstrip('\n') for line in open("/var/www/html/logLedEstados.txt")]
    print list
    #os.system("sudo cp /home/pi/logLed.txt /var/www/html/")
