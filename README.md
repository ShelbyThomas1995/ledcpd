# Control LED CPD

- Programas y herramientas necesarios:	
	
   Libreria WS2812 LEDs:

	sudo apt-get install gcc make build-essential python-dev git scons swig

	git clone https://github.com/jgarff/rpi_ws281x
	cd rpi_ws281x/
	sudo scons
	cd python
	sudo python setup.py build
	sudo python setup.py install

   PHP 7:
	
	apt-get install apache2 php7.0 php7.0-curl php7.0-gd php7.0-imap php7.0-json php7.0-mcrypt php7.0-mysql 
	php7.0-opcache php7.0-xmlrpc libapache2-mod-php7.0
	
	php -v	
	

- Configuración horaria:

   Utilizar el script "updateTime.sh", incluir el comando en rc.local para 
   que se ejecute al inicio de la Raspberry.

	sudo nano /etc/rc.local
	"Escribir comando de updateTime.sh"

   Añadir tarea crontab para que se ejecute cada dos horas y no se desconfigure
   la hora y fecha de la Raspberry:

	crontab -e 0 0,2,4,6,8,10,12,14,16,18,20,22 * * * /home/pi/updateTime.sh
  
	crontab -l #Para listar y comprobar la tarea
