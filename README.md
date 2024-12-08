# Apagado y encendido de forma limpia

Programa y circuito que permiten apagar y encender una Raspberry Pi anterior a la versión 4. 

Un pulsador enciende la Rasberry actuando sobre pin de "RUN", siempre y cuando se lo permita la salida digital GPIO21.

Otro pulsado apaga la Raspberry. Cuando se pulsa se activa la entrada digital GPIO20, que ejecuta un "sudo shutdown now".


