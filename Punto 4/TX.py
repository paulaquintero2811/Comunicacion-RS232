from machine import Pin, UART
import time

# UART0
uart = UART(0,baudrate=9600,bits=8,parity=None,stop=1,tx=Pin(0),rx=Pin(1))
# LED interno
led = Pin("LED", Pin.OUT)

print("TRANSMISOR listo")
print("Escriba un caracter:")

while True:

    caracter = input("Caracter: ")

    if len(caracter) > 0:
        # Enviar el primer caracter escrito
        uart.write(caracter[0])

        print("Enviado:", caracter[0])
        # Esperar confirmación del receptor
        while not uart.any():
            time.sleep(0.01)

        respuesta = uart.read(1)

        if respuesta == b"K":

            print("ACK recibido")
            # Parpadear LED durante 2 segundos
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(1)