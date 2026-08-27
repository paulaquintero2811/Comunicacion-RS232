import machine
import utime
from machine import Pin, UART
led = machine.Pin("LED", machine.Pin.OUT)
uart = UART(0, baudrate=600, bits=8, parity=None, stop=1, tx=Pin(0), rx=Pin(1))
while True:
led.on()
uart.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ABCDEFGHIJKLMNOPQRSTUVWX")
utime.sleep(1)
led.off()
utime.sleep(1)