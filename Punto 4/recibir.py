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

print("RECEPTOR DE ARCHIVO")
print("Esperando datos...")

archivo = open("recibido.txt", "w")

buffer = ""
contador = 0
inicio = None

while True:

    if uart.any():

        datos = uart.read()

        if datos:

            # Iniciar cronometro cuando llegue el primer dato
            if inicio is None:
                inicio = time.ticks_ms()

            buffer += datos.decode()

            while "\n" in buffer:

                posicion = buffer.find("\n")

                linea = buffer[:posicion + 1]
                buffer = buffer[posicion + 1:]

                # Detectar final de transferencia
                if linea.strip() == "<<FIN>>":
                    
                    archivo.close()

                    fin = time.ticks_ms()

                    tiempo_total = time.ticks_diff(fin, inicio) / 1000

                    print("-----------------------------")
                    print("RECEPCION TERMINADA")
                    print("Lineas recibidas:", contador)
                    print("Tiempo total:", tiempo_total, "s")
                    print("-----------------------------")

                    while True:
                        time.sleep(1)

                # Guardar línea recibida
                archivo.write(linea)
                archivo.flush()

                contador += 1

                print("Recibido:", linea.strip())
