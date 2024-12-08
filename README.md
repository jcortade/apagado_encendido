# Apagado y encendido de forma limpia

Programa y circuito que permiten apagar y encender una Raspberry Pi anterior a la versión 4. 

Un pulsador enciende la Rasberry actuando sobre pin de "RUN", siempre y cuando se lo permita la salida digital GPIO21.

Otro pulsado apaga la Raspberry. Cuando se pulsa se activa la entrada digital GPIO20, que ejecuta un "sudo shutdown now".

Código adaptado de este otro [repositorio](https://github.com/halofx/rpi-shutdown).

Circuito implementado:

![Circuito de encendido](https://github.com/jcortade/apagado_encendido/blob/b46286e7a8baad71da665b34c098365657bb6215/Encendido%20RPi.png)

