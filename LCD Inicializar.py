#!/usr/bin/python

#
# 20132013/11/26 21:19:07 @FoRTU
#
# Para poder interactuar con el 'lcd' es necesario crar un objeto que
# apunte 'de alguna manera' al dispositivo fisico. Para ello importamos
# una Clase que nos ayudara a crear dicho objeto.

# Importamos la clase que creara nuestro objeto que a su vez interactuara
# con el dispositivo.
from Librerias.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Inicializamos un objeto llamado 'lcd' mediante la Clase importada.
# La clase autodetecta el Bus I2C pero en caso de no hacerlo poner
# 'busnum = 0' entre los parentesis en caso de la version A de 256MB
# de la Raspberry, o 'busnum = 1' en el caso de la version B con 512MB
# de Ram.
lcd = Adafruit_CharLCDPlate()

# Una vez el objeto este creado ahora podremos interactuar con el
# dispositivo, como por ejemplo escribiendo un texto y poniendo el color
# de fondo 'verde'.
lcd.message("Hola Mundo!")
lcd.backlight(lcd.GREEN)

