#!/usr/bin/python

#
# 2013/11/26 21:02:42 @FoRTU
#
# Como cambiar de color la retro iluminacion del LCD. Al ser RGB es
# posible generar varios colores aparte de los primarios. Los utilizados
# en los siguentes ejemplos son los creados en la clase importada. Pero
# deduzco que modificando la clase se podrian generar mas colores.
#

# Importamos el comando "sleep" para pausar la ejecucion. Tambien 
# la Clase para crear un objeto que no sayude a interactur con el LCD.
from time import sleep
from Modulos.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Inicializamos un objeto llamado 'lcd' mediante la Clase importada.
# La clase autodetecta el Bus I2C pero en caso de no hacerlo poner
# 'busnum = 0' entre los parentesis en caso de la version A de 256MB
# de la Raspberry, o 'busnum = 1' en el caso de la version B con 512MB
# de Ram.
lcd = Adafruit_CharLCDPlate()

# Limpia el tecto de LCD.
lcd.clear()

# Cambia el Color de la retroiluminacion del LCD.
lcd.backlight(lcd.ON)

# Escribe un Mensaje en el LCD.
lcd.message("El fondo es de\ncolor Blanco")

#Pausa la ejecucion del codigo
sleep(1)

lcd.clear()
lcd.backlight(lcd.WHITE)
lcd.message("El fondo es de\ncolor Blanco")
sleep(1)

lcd.clear()
lcd.backlight(lcd.BLUE)
lcd.message("El fondo es de\ncolor Azul")
sleep(1)

lcd.clear()
lcd.backlight(lcd.GREEN)
lcd.message("El fondo es de\ncolor Verde")
sleep(1)

lcd.clear()
lcd.backlight(lcd.VIOLET)
lcd.message("El fondo es de\ncolor Violeta")
sleep(1)

lcd.clear()
lcd.backlight(lcd.TEAL)
lcd.message("El fondo es de\ncolor Cerceta")
sleep(1)

lcd.clear()
lcd.backlight(lcd.YELLOW)
lcd.message("El fondo es de\ncolor Amarillo")
sleep(1)

lcd.clear()
lcd.backlight(lcd.OFF)
lcd.message("La iluminacion\nesta desactivada")
sleep(1)

lcd.clear()
lcd.backlight(lcd.ON)
lcd.message("La iluminacion\nesta activada")
sleep(1)

