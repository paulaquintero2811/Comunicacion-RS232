from machine import Pin, UART, I2C
import time
import ssd1306

# UART0
uart = UART(0, baudrate=9600, bits=8, parity=None, stop=1, tx=Pin(0),rx=Pin(1))

# LED interno
led = Pin("LED", Pin.OUT)

# OLED
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Pantalla inicial
oled.fill(0)
oled.text("RECEPTOR", 25, 0)
oled.text("Esperando...", 10, 20)
oled.show()

print("Receptor listo")

while True:

    if uart.any():

        dato = uart.read(1)

        if dato:
            caracter = dato.decode()

            print("Recibido:", caracter)

            # Mostrar carácter recibido
            oled.fill(0)
            oled.text("RECIBIDO:", 20, 0)
            oled.text(caracter, 60, 25)
            oled.show()

            # LED encendido 5 segundos
            led.on()
            time.sleep(5)
            led.off()

            # Confirmación al transmisor
            uart.write("K")

            # Volver a esperar
            oled.fill(0)
            oled.text("RECEPTOR", 25, 0)
            oled.text("Esperando...", 10, 20)
            oled.show()