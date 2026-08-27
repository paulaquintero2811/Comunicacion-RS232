from machine import Pin, UART
import time

uart = UART(
    0,
    baudrate=9600,
    bits=8,
    parity=None,
    stop=1,
    tx=Pin(0),
    rx=Pin(1)
)

print("TRANSMISOR DE ARCHIVO")

# Leer el archivo completo
with open("alfabetos.txt", "r") as archivo:
    lineas = archivo.readlines()

print("Lineas a enviar:", len(lineas))

# Preguntar intervalo
while True:
    try:
        intervalo = float(input("Intervalo entre lineas (segundos): "))

        if intervalo >= 0:
            break

        print("El intervalo no puede ser negativo.")

    except:
        print("Ingrese un numero valido.")

print("Iniciando transmision...")

# Iniciar cronometro
inicio = time.ticks_ms()

# Enviar las líneas
for i, linea in enumerate(lineas):

    uart.write(linea)

    print("Enviado:", linea.strip())

    # Esperar solamente entre líneas
    if i < len(lineas) - 1:
        time.sleep(intervalo)

# Enviar indicador de final
uart.write("<<FIN>>\n")

# Esperar a que UART termine físicamente
uart.flush()

# Detener cronometro
fin = time.ticks_ms()

tiempo_total = time.ticks_diff(fin, inicio) / 1000

print("-----------------------------")
print("TRANSMISION TERMINADA")
print("Lineas enviadas:", len(lineas))
print("Intervalo:", intervalo, "s")
print("Tiempo total:", tiempo_total, "s")
print("-----------------------------")