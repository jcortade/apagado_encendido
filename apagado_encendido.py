import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep              # lets us have a delay
import os 							# Ejecuta comando de SO
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(21, GPIO.OUT)           # set GPIO21 as an output   
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Configuración GPIO20 como entrada

# Our function on what to do when the button is pressed  
def Shutdown(channel):  
    os.system("sudo shutdown -h now")

# Creación de interrupción de detección de evento asociado a la GPIO 20 
GPIO.add_event_detect(20, GPIO.FALLING, callback = Shutdown, bouncetime = 2000) 



try:  
    while True:
        #GPIO 21 forzada a cero para impedir el reset
        GPIO.output(21,0)	

        sleep(1)				# wait 1s
        
     
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program  
