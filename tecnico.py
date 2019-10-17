import time
import argparse
import sys
import os

if __name__ == '__main__':

    idrack = sys.argv[1]
    mode = sys.argv[2]
    fecha = sys.argv[3]
    hora = sys.argv[4]
    duracion = sys.argv[5]
    fechaTe = sys.argv[6]
    horaTe = sys.argv[7]

    string = "IDRack: " + idrack + " Modo: " + mode + " Fecha: " + fecha + " Hora: " + hora + " Entrada: " + fechaTe + " " + horaTe  +  " Duracion: " + duracion


    os.system("sudo echo " + string + " >> /var/www/html/a.txt")

